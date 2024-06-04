from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Departamento, Empleado, PuestoTrabajo
from .permissions import ReadOnlyPermission
from .serializers import DepartamentoSerializer, EmpleadoSerializer, PuestoTrabajoSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class DepartamentoListApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    #permission_classes = {"get": [permissions.AllowAny], "post": [permissions.IsAuthenticated]}
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the departamento items
        '''
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    @swagger_auto_schema(request_body=DepartamentoSerializer)
    def post(self, request, *args, **kwargs):
        '''
        Create the Departamento with given data
        '''
        #Opcion1:
        # data = {
        #     'nombre': request.data.get('nombre'),
        #     'telefono': request.data.get('telefono'),
        # }
        # serializer = DepartamentoSerializer(data=data)
        #Opcion2:
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartamentoDetailApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    def get_object(self, departamento_id):
        '''
        Helper method to get the object with given id
        '''
        try:
            return Departamento.objects.get(id=departamento_id)
        except Departamento.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, departamento_id, *args, **kwargs):
        '''
        Retrieves the Departamento with given departamento id
        '''
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id  does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = DepartamentoSerializer(departamento_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    @swagger_auto_schema(request_body=DepartamentoSerializer)
    def put(self, request, departamento_id, *args, **kwargs):
        '''
        Updates the departamento item with given id if exists
        '''
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nombre': request.data.get('nombre'),
            'telefono': request.data.get('telefono')
        }
        serializer = DepartamentoSerializer(instance = departamento_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, departamento_id, *args, **kwargs):
        '''
        Deletes the departamento item with given id
        '''
        departamento_instance = self.get_object(departamento_id)
        if not departamento_instance:
            return Response(
                {"res": "Object with departamento id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        departamento_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )



class PuestoTrabajoListApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    #permission_classes = {"get": [permissions.AllowAny], "post": [permissions.IsAuthenticated]}
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the puestosTrabajos items
        '''
        puestosTrabajos = PuestoTrabajo.objects.all()
        serializer = PuestoTrabajoSerializer(puestosTrabajos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    @swagger_auto_schema(request_body=PuestoTrabajoSerializer)
    def post(self, request, *args, **kwargs):
        '''
        Create the PuestoTrabajo with given data
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'departamento': request.data.get('departamento'),
        }
        serializer = PuestoTrabajoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PuestoTrabajoDetailApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    def get_object(self, puestoTrabajo_id):
        '''
        Helper method to get the object with given id
        '''
        try:
            return PuestoTrabajo.objects.get(id=puestoTrabajo_id)
        except PuestoTrabajo.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, puestoTrabajo_id, *args, **kwargs):
        '''
        Retrieves the PuestoTrabajo with given departamento id
        '''
        puestoTrabajo_instance = self.get_object(puestoTrabajo_id)
        if not puestoTrabajo_instance:
            return Response(
                {"res": "El objeto con habilidad_id no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PuestoTrabajoSerializer(puestoTrabajo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    @swagger_auto_schema(request_body=PuestoTrabajoSerializer)
    def put(self, request, puestoTrabajo_id, *args, **kwargs):
        '''
        Updates the puestoTrabajo item with given id if exists
        '''
        puestoTrabajo_instance = self.get_object(puestoTrabajo_id)
        if not puestoTrabajo_instance:
            return Response(
                {"res": "El objeto con id de puestoTrabajo no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nombre': request.data.get('nombre'),
        }
        serializer = PuestoTrabajoSerializer(instance = puestoTrabajo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, puestoTrabajo_id, *args, **kwargs):
        '''
        Deletes the puestoTrabajo item with given id
        '''
        puestoTrabajo_instance = self.get_object(puestoTrabajo_id)
        if not puestoTrabajo_instance:
            return Response(
                {"res": "Oobjeto con id de puestoTrabajo no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        puestoTrabajo_instance.delete()
        return Response(
            {"res": "¡Objeto eliminado!"},
            status=status.HTTP_200_OK
        )


class EmpleadoListApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    #permission_classes = {"get": [permissions.AllowAny], "post": [permissions.IsAuthenticated]}
    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the empleados items
        '''
        empleados = Empleado.objects.all()
        serializer = EmpleadoSerializer(empleados, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    @swagger_auto_schema(request_body=EmpleadoSerializer)
    def post(self, request, *args, **kwargs):
        '''
        Create the Empleado with given data
        '''
        data = {
            'nombre': request.data.get('nombre'),
            'fecha_nacimiento':request.data.get('fecha_nacimiento'),
            'antiguedad':request.data.get('antiguedad'),
            'departamento':request.data.get('departamento'),
            'puestoTrbajo':request.data.get('puestoTrabajo'),
        }
        serializer = EmpleadoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmpleadoDetailApiView(APIView):
    # add permission to check if user is authenticated
    authentication_classes = [JWTAuthentication]
    permission_classes = [ReadOnlyPermission]
    def get_object(self, empleado_id):
        '''
        Helper method to get the object with given id
        '''
        try:
            return Empleado.objects.get(id=empleado_id)
        except Empleado.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, empleado_id, *args, **kwargs):
        '''
        Retrieves the Empleado with given id
        '''
        empleado_instance = self.get_object(empleado_id)
        if not empleado_instance:
            return Response(
                {"res": "Object with empleado_id  does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EmpleadoSerializer(empleado_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    @swagger_auto_schema(request_body=EmpleadoSerializer)
    def put(self, request, empleado_id, *args, **kwargs):
        '''
        Updates the empleado item with given id if exists
        '''
        empleado_instance = self.get_object(empleado_id)
        if not empleado_instance:
            return Response(
                {"res": "Object with empleado id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nombre': request.data.get('nombre'),
        }
        serializer = EmpleadoSerializer(instance = empleado_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, empleado_id, *args, **kwargs):
        '''
        Deletes the empleado item with given id
        '''
        empleado_instance = self.get_object(empleado_id)
        if not empleado_instance:
            return Response(
                {"res": "Object with empleado id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        empleado_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )