from rest_framework.test import APIClient

#File
from SpeechToText.models import File, FileType
import os
from django.core.files import File as djFile
from django.core.files.uploadedfile import SimpleUploadedFile

#account
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#Registration
registration_mandatory_fields = ['username','password']
registration_responses = [200, 400]

#Login
login_mandatory_fields = ['username','password']
login_responses = [200, 400]

#PostFile
post_file_mandatory_fields = ['audio',]
post_file_responses = [201, 400, 401]

#File Testing
class TestOracle():

    def initAccountTesting(self):
        self.user_obj = User.objects.create_user(username = "cesar", password="1234", email="cls33@njit.edu")
        self.user_obj.save()
    
    def initFileTesting(self):
        self.user_obj_1 = User.objects.create_user(username = "cesar_1", password="1234", email="cls33@njit.edu")
        self.user_obj_1.save()

        self.user_obj_2 = User.objects.create_user(username = "cesar_2", password="1234", email="cls33@njit.edu")
        self.user_obj_2.save()

        self.audio_type = FileType.objects.create(id = 1, Name='Audio')
        self.audio_type.save()
        self.video_type = FileType.objects.create(id = 2, Name='Video')
        self.video_type.save()

        audio_path = os.getcwd() + '/Test/TestFiles/test_audio_1.wav'
        f = open(audio_path, 'rb')
        audiotest1 = djFile(f)
        file_obj_Audio = File.objects.create(Name='Audio File', Type = self.audio_type, User = self.user_obj_1)
        file_obj_Audio.Content = audiotest1
        file_obj_Audio.save()

    def registration_endPoint(self, data):
        expected_response = registration_responses[0]
        if not all(key in data for key in registration_mandatory_fields):
            expected_response = registration_responses[1]

        cl = APIClient()
        response = cl.post('/account/register/', data=data)
        print(response.status_code)
        print(expected_response)
        return response.status_code == expected_response

    def login_endPoint(self, data):
        expected_response = registration_responses[1]

        if not 'username' in data or not 'password' in data:
            expected_response = registration_responses[1]
        elif data['username'] == self.user_obj.username and data['password'] == "1234":
            expected_response = registration_responses[0]
        
        cl = APIClient()
        response = cl.post('/account/login/', data=data)
        
        print(response.status_code)
        print(expected_response)
        print(data)

        print(self.user_obj.username)
        print(self.user_obj.password)
        return response.status_code == expected_response

    def File_UploadEndPoints(self, Type, path, Token):
        expected_response = post_file_responses[0]
        content_type = 'undefined'
        if(Type == 1):
            if(path.endswith('.wav')):
                content_type = 'audio/wav'
            elif(path.endswith('.mp3')):
                content_type = 'audio/mp3'
        elif(Type == 2):
            content_type = 'audio/mp4'

        print(content_type)

        if(content_type == 'undefined'): 
            expected_response = post_file_responses[1]

        if(not Token):
            expected_response = post_file_responses[2]
            Token = ''

        audio_path = os.getcwd() + path#'/Test/TestFiles/test_video_1.mp3'
        f = open(audio_path, 'rb')
        audio = SimpleUploadedFile(audio_path, content = f.read(), content_type=content_type)
        #Preparing data
        data = { 'Type' : Type, 'Name' : 'Test' +  str(int), 'Content' : audio}
        
        #Authenticating user
        cl = APIClient()
        cl.credentials(HTTP_AUTHORIZATION='Token ' + Token)
        #Calling endPoint
        response = cl.post('/account-files/files/', data=data)

        print(content_type)
        print(response.status_code)
        print(path)

        return response.status_code == expected_response