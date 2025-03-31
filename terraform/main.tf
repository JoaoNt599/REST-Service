terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.91.0"
    }
  }
  backend "local" {
    path = "/terraform_data/terraform.tfstate"
  }
}

provider "aws" {
  # Configuration options
  region = "us-east-2"
}

# VPC
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "my-vpc"
  }
}

# SUBNET
resource "aws_subnet" "my_subnet" {
  vpc_id     = aws_vpc.my_vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-2a"

  tags = {
    Name = "my-subnet"
  }
}

# INTERNET GATEWAY
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.my_vpc.id

  tags = {
    Name = "gw"
  }
}

# ROUTE TABLE
resource "aws_route_table" "my_rt" {
  vpc_id = aws_vpc.my_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "my-rt"
  }
}

# ROUTE TABLE ASSOCIATION
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.my_subnet.id
  route_table_id = aws_route_table.my_rt.id
}

# KEY PAIR
resource "aws_key_pair" "my_key_pair" {
  key_name   = "my-key-pair-tst"
 public_key = file("~/.ssh/id_rsa.pub")  
}

# SECURITY GROUP
resource "aws_security_group" "my_sg" {
  name        = "my-sg"
  description = "Total Access"
  vpc_id      = aws_vpc.my_vpc.id

  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1" 
    cidr_blocks = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port = 0
    to_port   = 0
    protocol  = "-1" 
    cidr_blocks = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_tls"
  }
}

# INSTANCE
resource "aws_instance" "my_ec2" {
  ami           = "ami-0cb91c7de36eed2cb"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.my_subnet.id
  associate_public_ip_address = true
  key_name = aws_key_pair.my_key_pair.key_name
  vpc_security_group_ids = [aws_security_group.my_sg.id]
    
  tags = {
    Name = "my-ec2"
  }
}

output "ec2_ip" {
  value = aws_instance.my_ec2.public_ip
}