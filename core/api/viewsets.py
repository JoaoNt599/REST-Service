from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from  .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True) 
    