#!/bin/sh

k3d cluster create --servers 2 --agents 2

sleep 5

kubectl apply -f deployment.yaml

tail -f /dev/null
