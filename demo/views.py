from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


def index(request):
    """
    视图：函数视图
    :param request:请求对象，包含了请求信息的一个请求对象
    :return: response   响应对象
    """
    name = 'haha'

    return render(request, 'index.html', {'name': name})


def about(request):
    return HttpResponse('随便')


def gethtml(request):
    html = """
    <html>
        <head>
        </head>
        <body>
            <h1>哈哈哈哈<h1>
            <img src="C:\\Users\ibm\Desktop\新建文件夹\\1.jpg" >
        </body>
    </html>

    """
    return HttpResponse(html)


from django.shortcuts import render_to_response


def abs(request):
    return render_to_response('about.html')


from django.template.loader import get_template


def abc(requets):
    template = get_template('about.html')
    name = 'hello'
    result = template.render({'name': name})
    return HttpResponse(result)


def test(request):
    class Say(object):
        def say(self):
            return 'hello word'

    spk = Say()
    spk = spk.say()
    # return render(request,'test.html',locals())
    template_obj = Template('test.html')
    result = Context(spk)
    result = template_obj.render(result)
    return HttpResponse(result)
    # return HttpResponse('test.html', locals())
    # return HttpResponse('test.html',locals())

def haha(request):
    return render(request,'index.html')