from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from  .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True) 
    
    # GET
    # def list(self, request, *args, **kwargs):
    #     return Response(
    #         {
    #             'teste': 'Sobrescrevendo GET'
    #         }
    #     )

    # POST
    # def create(self, request, *args, **kwargs):
    #     return Response(
    #         {
    #             'Hello': request.data['nome']
    #         }
    #     )

    # DELETE
    # def destroy(self, request, *args, **kwargs):
    # pass
    
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # PUT
    # def update(self, request, *args, **kwargs):
    #     pass

    # PATH
    # def partial_update(self, request, *args, **kwargs):
    #     pass