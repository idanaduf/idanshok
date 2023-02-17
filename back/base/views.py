from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http import JsonResponse, HttpResponse
from .models import Product, Client   
from .Serializer import ProductSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .Serializer import TaskSerializer
from .models import Task
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
####### login #######
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        # ...
        return token        
####### login #######

###### logout #######
class LogoutAPIView(APIView):
    def post(self, request):
        refresh_token = RefreshToken(request.data.get('refresh'))
        refresh_token.blacklist()
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
###### logout #######

###### #refresh token ######
class RefreshTokenView(generics.GenericAPIView):
    serializer_class = TokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
###### refresh token ######


###### register ######
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return JsonResponse("new user motherfuc*er", safe=False)
###### register ######


########### client ############
@api_view(['GET','POST'])
def clients(request):
    print(request)
    tempAr=[]
    for cli in Client.objects.all():
        tempAr.append({"age":cli.age,"name":cli.cName,"id":cli.id})
    return JsonResponse(tempAr,safe=False)
########### client #############


#################### authenticate ################
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])

############################ authenticate ################################

############################ pages #############################
def index(req):
    return JsonResponse('hello', safe=False)

def about(req):
    return JsonResponse('about', safe=False)    

def myProducts(req):
    all_products = ProductSerializer(Product.objects.all(), many=True).data
    return JsonResponse(all_products, safe=False)

def index(req):
    return JsonResponse('hello', safe=False)
############################ pages #############################

############################ image #############################
### image upload / display ###
# return all images to client (without serialize)
@api_view(['GET'])
def getImages(request):
    res=[] #create an empty list
    for img in Task.objects.all(): #run on every row in the table...
        res.append({"title":img.title,
                "description":img.description,
                "completed":False,
               "image":str( img.image)
                }) #append row by to row to res list
    return Response(res) #return array as json response


# upload image method (with serialize)
class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=TaskSerializer(data=request.data)
       
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

############### image upload / display ################
