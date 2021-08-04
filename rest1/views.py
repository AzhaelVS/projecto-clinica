from django.shortcuts import render
from rest1.models import *
from rest1.serializers import *
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from django.http.response import HttpResponseNotAllowed
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
#from rest_framework.authentication import TokenAuthentication

class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer
    filter_backends= (DjangoFilterBackend,SearchFilter,OrderingFilter)
    search_fields=('name','address','data_sheet__descripcion')
    filter_fields = ('name',)
    ordering_fields='__all__'
    ordering=('id')
#    authentication_classes=[TokenAuthentication,]
    #lookup_field='name'

    def get_queryset(self):
        customers = Customer.objects.all()
        address =self.request.query_params.get('address',None)

        if self.request.query_params.get('active') == False:
            status =False
        else:
            status=True

        if address:
            customer= Customer.objects.filter(address__icontains=address, active=status)
        else :
            customer= Customer.objects.filter(active=status)

        return customer

    #def list(self,request, *args, **kwarg):
    #    customer= self.get_queryset()
    #    serializer = CustomerSerializer(customer, many=True)
    #    return Response(serializer.data)

    def retrieve(self,request, *args, **kwarg):
        customer = self.get_object()
        serializer = CustomerSerializer(customer)
        return Response(serializer)
        #return HttpResponseNotAllowed('Not allowed')

    def Create(self, request , *args, **kwargs):
        data = request.data
        customer= Customer.objects.create(
        name = data['name'], address= data['address'],data_sheet_id= data['data_sheet']
        )
        profession=Profession.objects.get(id=data['profession'])
        customer.profession.add(profession)
        Customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def update(self,request, *arg, **kwarg):
        customer = self.get_object()
        data= request.data
        customer.name =data['name']
        customer.address =data['address']
        customer.data_sheet_id = data['data_sheet']

        profession = Profession.objects.get(id=data['profession'])

        for p in customer.profession.all():
            customer.profession.remove(p)

        customer.profession.add(profession)
        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.name = request.data.get('name', customer.name)
        customer.address = request.data.get( 'address' , customer.address)
        customer.data_sheet_id= request.data.get('data_sheet', customer.data_sheet_id)

        customer.save()
        serializer= CustomerSerializer(customer)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.delete()
        return Response('objects remove')


    @action(detail=True)
    def deactivate(self,request, *args, **kwargs):
        customer = self.get_object()
        customer.active = False
        serializer= CustomerSerializer(customer)
        return Response(serializer.data)

    @action(detail=False)
    def deactivate_all(self,request, *args, **kwargs):
        customer = self.get_queryset()
        customer.update(active=False)

        serializer= CustomerSerializer(customer,many=True)
        return Response(serializer.data)

    @action(detail=True)
    def activate(self,request, *args, **kwargs):
        customer =self.get_object()
        customer.active = True
        serializer= CustomerSerializer(customer)
        return Response(serializer.data)

    @action(detail=False)
    def activate_all(self,request, *args, **kwargs):
        customer = Customer.objects.all()
        customer.update(active=True)

        serializer= CustomerSerializer(customer,many=True)
        return Response(serializer.data)

    @action(detail=False, methods= ['POST'])
    def change_status(self,request,**kwargs):
        status=True if request.data['active']== 'True' else False

        customer= self.get_queryset()
        customer.update(active=status)

        serializer=CustomerSerializer(customer, many=True)
        return Response(serializer.data)

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset= Profession.objects.all()
    serializer_class = ProfessionSerializer
#    authentication_classes=[TokenAuthentication,]

class DataSheetViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer
#    authentication_classes=[TokenAuthentication,]
class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
#    authentication_classes=[TokenAuthentication,]
