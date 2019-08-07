from django.shortcuts import render, redirect
# Create your views here.
from .models import student, users


def students(request):
    stu = student.objects.all()
    return render(request, 'myapp/student.html', {"student": stu})


def index(request):
    Name = request.session.get("user", "游客")
    return render(request, 'myapp/main.html', {"name": Name})


def main(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "所有字段都必须填写！"
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = users.objects.get(username=username)
                if user.password == password:
                    request.session["user"] = username
                    name = request.session.get("user", "请登录")
                    return redirect('/main/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在！"
        return render(request, 'myapp/login.html', {"message": message})
    return redirect('/')


def login(request):
    return render(request, 'myapp/login.html')


def logout(request):
    request.session.flush()
    return redirect('/')


def regist(request):
    # if request.session.get('is_login', None):
        #  登录状态不允许注册。你可以修改这条原则！
    #  return redirect("/")
    if request.method == "POST":
        uname = request.POST.get('username', None)
        pwd = request.POST.get('password', None)
        if uname and pwd:
            try:
                 user = users.objects.get(username=uname)
                 message = "用户名已经存在！"
                 return render(request, 'myapp/regist.html', {"message": message})
            except:
                new_user = users.objects.create()
                new_user.username = uname
                new_user.password = pwd
                new_user.save()
                return redirect("/")
    return render(request, 'myapp/regist.html')
