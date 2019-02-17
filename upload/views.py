from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import os
from mysite.settings import MEDIA_ROOT

def upload(request):
    if request.method == 'GET':
        return render(request, 'upload/upload.html')
    elif request.method == 'POST':
        file = request.FILES.get('file')
        print(file)
        file_path = os.path.join(MEDIA_ROOT, file.name)
        print(file_path)
        with open(file_path, 'wb')as f:
            for i in file.chunks():
                f.write(i)

        return HttpResponse('上传成功')

