from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from rest_framework.reverse import reverse as api_reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from .validators import validate_file_extension
import speech_recognition as sr
from os import path

# Create your models here.

def get_upload_path(instance, filename):
    return './Files/user_' + str(instance.owner.id) + '/' + filename

def scramble_uploaded_filename(instance, filename):
    """
    Scramble / uglify the filename of the uploadedfile, but keep the files extension (e.g., .jpg or .png)
    :param instance:
    :param filename:
    :return:
    """
    extension = filename.split(".")[-1]
    
    print(instance.owner.id)
    name = get_upload_path(instance, "{}.{}".format(uuid.uuid4(), extension))
    print(name)
    return name#"{}.{}".format(name, extension)

class FileType(models.Model):
    """High-level FileType"""
    Name = models.CharField(max_length=20)


class File(models.Model):
    """High-level File"""
    Name = models.CharField(max_length=50)
    Type = models.ForeignKey(FileType, on_delete = models.CASCADE)
    Transcript = models.TextField(null=True)
    UploadedDate = models.DateTimeField(default = timezone.now)
    Content =models.FileField("UploadedFiles", upload_to=scramble_uploaded_filename, validators=[validate_file_extension], blank=True, null=True)
    User = models.ForeignKey(User, on_delete = models.CASCADE)

    @property
    def owner(self):
        return self.User

    def get_api_url(self, request=None):
        return api_reverse("account-file-api:Files-View", kwargs={'pk': self.pk}, request=request)

    @property
    def IsAudio(self):
        print(self.Type.id)
        return (self.Type.id == 1)

    @property
    def IsVideo(self):
        return self.Type.id == 2

    @property
    def IsMic(self):
        return self.Type.id == 3

    def TranscriptFile(self):
        print('About to Transcript')

        self.Transcript = 'Just transcripted'

        
        AUDIO_FILE = os.getcwd() + self.Content.path
        print(AUDIO_FILE)

        r = sr.Recognizer()
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)  # read the entire audio file

        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            self.Transcript = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + self.Transcript)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        self.save()

@receiver(post_delete, sender=File)
def submission_delete(sender, instance, **kwargs):
    instance.Content.delete(False) 


#class User(models.Model):
 #   """High-level user model"""
  #  Token = models.CharField(max_length=50)
  #  FirstName = models.CharField(max_length=50)
  #  LastName = models.CharField(max_length=50)
  #  Email = models.CharField(max_length=50)
  #  Password = models.CharField(max_length=50)
  #  CreatedDate = models.DateTimeField(default=timezone.now)
  #  ModifiedDate = models.DateTimeField(default=timezone.now)
