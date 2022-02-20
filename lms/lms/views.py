from git import Repo

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def update_pythonanywhere(request):
    if request.method == "POST":
        '''
        pass the path of the directory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo_path = "/home/bilard/Desktop/test_git/Django-LMS"
        repo = Repo(repo_path)
        origin = repo.remotes.origin
        origin.pull()

        return HttpResponse("Code has been updated on pythonanywhere", status= 200)
    else:
        return HttpResponse("Method not allowed", status=405)
