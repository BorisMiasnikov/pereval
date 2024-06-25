from django.shortcuts import render


class ImegesViewset(viewsets.ModelViewSet):
    queryset = Imeges.objects.all()
    serializer_class = ImegesSerializer