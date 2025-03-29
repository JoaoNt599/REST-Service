from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core.models import PontoTuristico
from  .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):
    
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True) 
    
    @action(methods=['post', 'get'], detail=True) #, permission_classes=[IsAtuthenticated]
    def denunciar(self, request, pk=None):
        atracao = self.get_object()
        return Response(
            {
                'mensagem': f'Atração {atracao.nome} denunciada com sucesso!'
            }
        )
    
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

   