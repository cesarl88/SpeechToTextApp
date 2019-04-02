from rest_framework.exceptions import ParseError
#from rest_framework.parsers import FileUploadParser
from rest_framework import generics, mixins
from rest_framework.response import Response
from SpeechToText.permissions import IsOwner, PublicEndpoint
from .serializers import FileSerializer, FileUpdateSerializer
from SpeechToText.models import File
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


class UploadedFileView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field            = 'id'
    serializer_class        = FileSerializer
    permission_classes      = [IsOwner]

    def get_queryset(self, *args, **kwargs):
        print('Here')
        print(self.request)
        print(self.kwargs)
        qs = File.objects.filter(User = self.request.user).prefetch_related('Type')
        if "id" in self.kwargs:
            print('ID')
            qs = qs.filter(id = int(self.kwargs["id"])).distinct()
        elif "q" in self.request.GET:
            print('search')
            qs = qs.filter(Name__icontains = self.request.GET['q']).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

class DeleteFileView(generics.DestroyAPIView):
    lookup_field            = 'id' 
    serializer_class        = FileSerializer
    permission_classes      = [IsOwner]
    queryset                = File.objects.all()
    

class InitTranscript(APIView):
    lookup_field            = 'id' 
    serializer_class        = FileSerializer
    permission_classes      = [IsOwner]
    queryset                = File.objects.all()
    

    def post(self, request):
        files = File.objects.filter(User = self.request.user)
        if(files):
            file = get_object_or_404(files, id = int(request.data['id']))
            offset = 0
            if('offset' in request.data):
                offset = int(request.data['offset'])

            if(file.IsAudio):
                print('Processing Audio File')
            elif(file.IsVideo):
                print('Processing Video File')
            elif(file.IsMic):
                print('Processing Microphonee File')
            
            status_code = file.TranscriptFile(offset)

            return Response(status= status_code, data = file.Transcript)
        return Response(status= 400)

#@csrf_exempt
class UpdateFileView(generics.UpdateAPIView):
    lookup_field            = 'id'
    serializer_class        = FileUpdateSerializer
    permission_classes      = [IsOwner]
    queryset                = File.objects.all()

    def update(self, request, *args, **kwargs):
        print(self.request.data)
        instance = self.get_object()
        print(instance.id)
        print(instance.Type)
        
        if(request.data.get("Name")):
            instance.Name = request.data.get("Name")

        if(request.data.get("Comment")):
            instance.Comment = request.data.get("Comment")

        
        if(request.data.get("Transcript") and instance.Type.id == 3):
            instance.Transcript = request.data.get("Transcript")
            print(request.data.get("Transcript"))
            print("saving   ")
        
        instance.save()

        #serializer = FileUpdateSerializer(instance)
        #serializer.is_valid(raise_exception=True)
        #self.perform_update(serializer)

        return Response(status = 200, data = request.data)

        
        
   