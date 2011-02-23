from jinjango import render_to_response
import time


def _generic_handler(template_name):
    def handler(request):
        return render_to_response(template_name)
    return handler

index = _generic_handler("index.html")
quotes = _generic_handler("quotes.html")

def sysconf(request):
    head = ("Product", "Location", "OS", "Gen", "Capacity")
    items = (("iPhone", "mobile", "iOS 4.2.1", "3gs", "8 GiB"),
             ("iPad", "next to bed", "iOS 4.2.1", "1", "16 GiB"),
             ("MacBook pro", "shlomi penner", "OS X 10.6", "7", "500 GiB"),
             ("MacBook air", "(future option)", "OS X 10.6", "2", "200 GiB"),
             ("Mac Mini", "home", "OS X 10.6", "", "320 GiB"),
             ("Mac Mini", "home", "OS x 10.6", "", "500 GiB"),
             ("Apple TV", "home", "ubuntu 10.10", "3", ""),
             ("Apple Time Capsule", "home", "", "2", "1 TiB"),
             ("Media Center", "home", "Windows 7", "", "1 TiB"))

    return render_to_response("sysconf.html", context=locals())

def testra(request):
    SUCCESS = '<font color="green">Success</font>'
    FAILURE =  '<font color="red">Failure</font>'
    head = ("Invocation", "Date", "Result")
    DATE = lambda t: time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(t))
    items = (("fiber switch automation", DATE(1263822195), SUCCESS),
             ("migration to power 9", DATE(1264822195), SUCCESS),
             ("take over IT", DATE(1266822195), SUCCESS),
             ("replace sysaid with jira", DATE(1278253354), SUCCESS),
             ("secretary in the 37th floor", DATE(1289301237), SUCCESS),
             ("wifi in toilets", DATE(1294967656), FAILURE))
    return render_to_response("testra.html", context=dict(head=head, items=items))


