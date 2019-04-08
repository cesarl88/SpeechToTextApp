import pytest
import unittest
from django.contrib.auth.models import User
from SpeechToText.models import File, FileType
from django.core.files import File as djFile
from django.core.files.base import ContentFile
import os
import requests
#from rest_framework.authtoken.models import Token
from knox.models import AuthToken

import json
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test.client import BOUNDARY, MULTIPART_CONTENT, encode_multipart, Client, RequestFactory
from rest_framework.test import APIClient


from  TestOracle import TestOracle as T_Oracle

@pytest.fixture(autouse=True)
def cleanup_files():
    pass

@pytest.fixture()
def get_audio_file():
    pass
    #files = []
        # monkeypatch.setattr(builtins, 'open', patch_open(builtins.open, files))
        # monkeypatch.setattr(io, 'open', patch_open(io.open, files))
        # yield
        # for file in files:
        #     os.remove(file)

@pytest.mark.django_db
class TestFiles:

    def setup(self):
        self.TestOracle = T_Oracle()
        self.TestOracle.initFileTesting()
        # user_obj = User.objects.create_user(username = "cesar_1", password="1234", email="cls33@njit.edu")
        # user_obj.save()

        # user_obj_2 = User.objects.create_user(username = "cesar_2", password="1234", email="cls33@njit.edu")
        # user_obj_2.save()

        # audio_type = FileType.objects.create(id = 1, Name='Audio')
        # audio_type.save()
        # video_type = FileType.objects.create(id = 2, Name='Video')
        # video_type.save()

        # audio_path = os.getcwd() + '/Test/TestFiles/test_video_1.mp3'
        # f = open(audio_path, 'rb')
        # audiotest1 = djFile(f)
        # file_obj_Audio = File.objects.create(Name='Audio File', Type = audio_type, User = user_obj)
        # file_obj_Audio.Content = audiotest1
        # file_obj_Audio.save()


    def teardown_method(self, method):
        file_obj_Audios = File.objects.all()

        #Cleaingin files
        for f in file_obj_Audios:
            f.delete()

    def test_PostAudioFileMp3(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        passes = self.TestOracle.File_UploadEndPoints(1, '/Test/TestFiles/test_video_1.mp3', token)
        assert passes == True
        #Get Audio file mp3
        # audio_path = os.getcwd() + '/Test/TestFiles/test_video_1.mp3'
        # f = open(audio_path, 'rb')
        # audio = SimpleUploadedFile(audio_path, content = f.read(), content_type="audio/mp3")
        # #Preparing data
        # data = { 'Type' : 1, 'Name' : 'Tes1', 'Content' : audio}
        
        # #Authenticating user
        # cl = APIClient()
        # cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        # #Calling endPoint
        # response = cl.post('/account-files/files/', data=data)
        # assert response.status_code == 201

    def test_PostAudioFileWav(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        passes = self.TestOracle.File_UploadEndPoints(1, '/Test/TestFiles/test_audio_1.wav', token)
        assert passes == True

    def test_GetAudioFileList(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/')
        
        assert len(response.data) == File.objects.count()


    def test_GetAudioFileByID(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/' + str(id) + "/")
        assert response.data[0]['id'] == id

    def test_DeleteAudioFileByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.first())
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.delete('/account-files/files-delete/' + str(id) + "/")
        assert response.status_code == 204


    def test_GetAudioFileByID_WrongUser(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_2"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/' + str(id) + "/")
        
        assert response.status_code == 200 and not response.data

    
    def test_UpdateFileByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Name" : "Test1Modified",
        	"Comment": "Comment 12",
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        response_get_file = cl.get('/account-files/files/' + str(id) + "/")

        data_Res = response_get_file.data[0]
        assert response.status_code == 200 and (data_Res['Name'] == "Test1Modified" and  data_Res['Comment'] == "Comment 12")

    #Update By Owner
    def test_UpdateFileNameByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Name" : "Test1Modified"
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        response_get_file = cl.get('/account-files/files/' + str(id) + "/")

        data_Res = response_get_file.data[0]
        assert response.status_code == 200 and (data_Res['Name'] == "Test1Modified")

    def test_UpdateFileNameAndCommentByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #print(token)
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Name" : "Test1Modified",
            "Comment" : "CommentModified"
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        response_get_file = cl.get('/account-files/files/' + str(id) + "/")

        data_Res = response_get_file.data[0]
        #print(data_Res)
        assert response.status_code == 200 and (data_Res['Name'] == "Test1Modified" and data_Res['Comment'] == "CommentModified")

    def test_UpdateFileCommentByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #print(token)
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Comment" : "CommentModified"
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        response_get_file = cl.get('/account-files/files/' + str(id) + "/")

        data_Res = response_get_file.data[0]
        #print(data_Res)
        assert response.status_code == 200 and (data_Res['Name'] == "Audio File" and data_Res['Comment'] == "CommentModified")

    def test_TryUpdateFileContentByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Content" : "ContentModified"
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        response_get_file = cl.get('/account-files/files/' + str(id) + "/")

        data_Res = response_get_file.data[0]
        assert response.status_code == 200 and (data_Res['Content'] != "ContentModified")
    
    def test_TryUpdateFileTranscriptByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Transcript" : "TranscriptModified"
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        response_get_file = cl.get('/account-files/files/' + str(id) + "/")

        data_Res = response_get_file.data[0]
        assert response.status_code == 200 and (data_Res['Transcript'] != "TranscriptModified")

        
    def test_TryUpdateFileTypeByID_ByOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_1"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Type" : "Type"
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        response_get_file = cl.get('/account-files/files/' + str(id) + "/")

        data_Res = response_get_file.data[0]
        assert response.status_code == 200 and (data_Res['Type'] == 1)

    #Update By Owner
    def test_UpdateFileNameByID_ByNotOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_2"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Name" : "Test1Modified",
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        print(response.status_code)
        assert response.status_code == 403 

    #Update By Owner
    def test_UpdateFileCommentByID_ByNotOwner(self, client):
        #get Token
        token = AuthToken.objects.create(User.objects.get(username = "cesar_2"))
        
        id  = File.objects.first().id
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        data = {
            "Comment" : "TCommentModified",
        }
        response = cl.put('/account-files/files-update/' + str(id) + "/", data = data)
        print(response.status_code)
        assert response.status_code == 403 

    #integration Test
    def test_Login_List_GetFile(self, client):
        #login
        response = client.post('/account/login/', {
            "username": "cesar_1",
            "password": "1234",
        })
        assert response.status_code == 200

        token = response.data['token']
        #list files
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/')
        
        assert len(response.data) == File.objects.count()

        
        first_id = response.data[0]['id']
        print(first_id)
        #Getting file by Id
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
        #Calling EndPoint
        response = cl.get('/account-files/files/' + str(first_id) + "/")
        assert response.status_code == 200

    #unit

    def test_transcript_first30_seconds(self):
        file = File.objects.first()
        print(file)
        result = file.TranscriptFile(0)
        assert result == 200
        

    # #integration Test
    # def test_Login_List_GetFile(self, client):
    #     #login
    #     response = client.post('/account/login/', {
    #         "username": "cesar_1",
    #         "password": "1234",
    #     })
    #     assert response.status_code == 200

    #     token = response.data['token']
    #     #list files
    #     cl = APIClient()
    #     cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
    #     #Calling EndPoint
    #     response = cl.get('/account-files/files/')
        
    #     assert len(response.data) == File.objects.count()

        
    #     first_id = response.data[0]['id']
    #     print(first_id)
    #     #Getting file by Id
    #     cl = APIClient()
    #     cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
    #     #Calling EndPoint
    #     response = cl.get('/account-files/files/' + str(first_id) + "/")
    #     assert response.status_code == 200

    def test_Login_List_GetFile_transcript_first30_seconds(self, client):
        #login
        response = client.post('/account/login/', {
            "username": "cesar_1",
            "password": "1234",
        })
        assert response.status_code == 200

        token = response.data['token']
        #list files
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/')
        
        assert len(response.data) == File.objects.count()

        
        first_id = response.data[0]['id']
        print(first_id)
        #Getting file by Id
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
        #Calling EndPoint
        response = cl.get('/account-files/files/' + str(first_id) + "/")
        assert response.status_code == 200

        data = { 'id': first_id, 'offset':  0}
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
        #Calling EndPoint
        response = cl.post('/account-files/files-transcript/' + str(first_id) + "/", data=data)
        assert response.status_code == 200   

    def test_Login_List_GetFile_transcript(self, client):
        #login
        response = client.post('/account/login/', {
            "username": "cesar_1",
            "password": "1234",
        })
        assert response.status_code == 200

        token = response.data['token']
        #list files
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        #Calling EndPoint
        response = cl.get('/account-files/files/')
        
        assert len(response.data) == File.objects.count()

        
        first_id = response.data[0]['id']
        print(first_id)
        #Getting file by Id
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        
        #Calling EndPoint
        response = cl.get('/account-files/files/' + str(first_id) + "/")
        assert response.status_code == 200

        offset = 0
        data = { 'id': first_id, 'offset':  offset}
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + token)
        status_code = 200
        #Calling EndPoint
        while (status_code == 200):
            response = cl.post('/account-files/files-transcript/' + str(first_id) + "/", data=data)
            status_code = response.status_code 
            offset += 30
            data = { 'id': first_id, 'offset':  offset}

        assert status_code == 201

