import pytest
import unittest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from  TestOracle import TestOracle as T_Oracle
@pytest.mark.django_db
class TestAccount:
    def setup(self):
        self.TestOracle = T_Oracle()
        self.TestOracle.initAccountTesting()
        # user_obj = User.objects.create_user(username = "cesar", password="1234", email="cls33@njit.edu")
        # user_obj.save()

    def test_noAuthenticated(self, client):
        response = client.get('/test/NotAuthenticatedTest', follow = True)
        assert response.status_code == 200

    def test_authenticated(self, client):
        response = client.get('/test/AuthenticatedTest', follow = True)
        assert response.status_code == 401

    def test_register(self, client):

        passes = self.TestOracle.registration_endPoint({
            "username": "cls33",
            "password": "Cesartest",
            "email" : "cls33@njit.edu",
            "first_name" : "Cesar",
            "last_name" : "Salazar"
        })

        assert passes == True
        # response = client.post('/account/register/', {
        #     "username": "cls33",
        #     "password": "Cesartest",
        #     "email" : "cls33@njit.edu",
        #     "first_name" : "Cesar",
        #     "last_name" : "Salazar"
        # })
        # assert response.status_code == 200

    def test_register_no_user_name(self, client):
        passes = self.TestOracle.registration_endPoint({
            #"username": "cls33",
            "password": "Cesartest",
            "email" : "cls33@njit.edu",
            "first_name" : "Cesar",
            "last_name" : "Salazar"
        })

        assert passes == True

        # response = client.post('/account/register/', {
        #     #"username": "cls33",
        #     "password": "Cesartest",
        #     "email" : "cls33@njit.edu",
        #     "first_name" : "Cesar",
        #     "last_name" : "Salazar"
        # })
        # assert response.status_code == 400

    def test_register_no_user_password(self, client):
        passes = self.TestOracle.registration_endPoint({
            "username": "cls33",
            #"password": "Cesartest",
            "email" : "cls33@njit.edu",
            "first_name" : "Cesar",
            "last_name" : "Salazar"
        })

        assert passes == True
        # response = client.post('/account/register/', {
        #     #"username": "cls33",
        #     "password": "Cesartest",
        #     "email" : "cls33@njit.edu",
        #     "first_name" : "Cesar",
        #     "last_name" : "Salazar"
        # })
        # assert response.status_code == 400

    def test_login(self, client):
        passes = self.TestOracle.login_endPoint({
            "username": "cesar",
            "password": "1234",
        })

        assert passes == True

        # response = client.post('/account/login/', {
        #     "username": "cesar",
        #     "password": "1234",
        # })
        # assert response.status_code == 200

    def test_login_wrong_username(self, client):
        passes = self.TestOracle.login_endPoint({
            "username": "cesarl",
            "password": "1234",
        })

        assert passes == True
        
        # response = client.post('/account/login/', {
        #     "username": "cesarl",
        #     "password": "1234",
        # })
        # assert response.status_code == 400

    def test_login_wrong_password(self, client):
        passes = self.TestOracle.login_endPoint({
            "username": "cesar",
            "password": "123ddsd",
        })

        assert passes == True

        # response = client.post('/account/login/', {
        #     "username": "cesar",
        #     "password": "123433",
        # })
        # assert response.status_code == 400

    def test_login_wrong_credentials(self, client):
        passes = self.TestOracle.login_endPoint({
            "username": "cesar",
            "password": "123ddsd",
        })

        assert passes == True
        # response = client.post('/account/login/', {
        #     "username": "cesar2",
        #     "password": "123433",
        # })
        # assert response.status_code == 400

