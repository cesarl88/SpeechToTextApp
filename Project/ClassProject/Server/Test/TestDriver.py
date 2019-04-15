
from django.contrib.auth.models import User
from SpeechToText.models import File, FileType

def transcript_wav_first_30_sec():
    test_input  = { "test_case" : "transcript_wav_first_30_sec", "File" : File.objects.get(id = 1)}
    return test_input

def transcript_wav_middle_file():
    test_input  = { "test_case" : "transcript_wav_middle_file", "File" : File.objects.get(id = 1), "offset" : 60 }
    return test_input

def transcript_wav_end_file():
    test_input  = { "test_case" : "transcript_wav_final_30_sec", "File" : File.objects.get(id = 1), "offset" : 120 }
    return test_input


def transcript_video_first_30_sec():
    test_input  = { "test_case" : "transcript_video_first_30_sec", "File" : File.objects.get(id = 2)}
    return test_input

def transcript_video_middle_file():
    test_input  = { "test_case" : "transcript_video_middle_file", "File" : File.objects.get(id = 2), "offset" : 60 }
    return test_input

def transcript_video_end_file():
    test_input  = { "test_case" : "transcript_video_final_30_sec", "File" : File.objects.get(id = 2), "offset" : 120 }
    return test_input

def file_length():
    test_input  = { "test_case" : "file_length", "File" : File.objects.get(id = 2)}
    return test_input

def file_convert_to_wav():
    test_input  = { "test_case" : "file_convert_to_wav", "File" : File.objects.get(id = 2)}
    return test_input
    