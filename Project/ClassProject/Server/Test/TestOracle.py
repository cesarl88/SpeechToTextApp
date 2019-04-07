from rest_framework.test import APIClient

#account
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

#Registration
registration_mandatory_fields = ['username','password']
registration_responses = [200, 400]

#Login
login_mandatory_fields = ['username','password']
login_responses = [200, 400]

#File Testing
class TestOracle():

    def initAccountTesting(self):
        self.user_obj = User.objects.create_user(username = "cesar", password="1234", email="cls33@njit.edu")
        self.user_obj.save()

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