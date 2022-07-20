
from rest_framework import generics
from .models import Code , Category
from .serializers import CodeSerializer,CategorySerializer


class CodeList(generics.ListAPIView):
    serializer_class=CodeSerializer
    
    def get_queryset(self):
        queryset = Code.objects.all()
        category= self.request.query_params.get("category")
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset
    
    def create(self,request):
        
        pass
    
    
    
    
    
    
    
    
    
    
class CodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Code.objects.all()
    serializer_class= CodeSerializer
    lookup_field="id"
    

class CategoryList(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer
    lookup_field="id"
    
    
