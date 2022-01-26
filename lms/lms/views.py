import git

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
        repo = git.Repo(search_parent_directories=True)
        print(repo)
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Code has been updated on pythonanywhere", status= 200)
    else:
        return HttpResponse("Method not allowed", status=405)
