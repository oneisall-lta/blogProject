import os

from django.shortcuts import render

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Create your views here.
def upload(request):
    if request.method == 'GET':
        return render(request, 'myload.html')
    else:
        # 获取上传文件对象
        upload_obj = request.FILES.get('myfile')
        # 拼接上传的文件地址
        dest_file = os.path.join(BASE_DIR, 'practiceapp','uploads', 'uploadings', upload_obj.name)
        print(dest_file)
        print(type(dest_file))
        with open(dest_file, 'wb') as f:  # 以’wb'模式打开上传目标文件，准备写入
            for chunk in upload_obj.chunks():  # 对上传文件进行分块写入
                f.write(chunk)

        imgpath = 'uploadings/' + upload_obj.name  # 获取刚才上传文件的网址
        return render(request, 'success.html', {'imgpath': imgpath})
