from jinjango import render_to_response



def _generic_handler(template_name):
    def handler(request):
        return render_to_response(template_name)
    return handler

index = _generic_handler("index.html")
quotes = _generic_handler("quotes.html")

def sysconf(request):
    head = ("Product", "Location", "OS", "Gen", "Capacity")
    items = (("iphone", "mobile", "iOS 4.1", "3gs", "8 GiB"),
             ("ipad", "mobile", "iOS 4.2", "1", "16 GiB"),
             ("mac book pro", "mobile", "OS X 10.6", "", "500 GiB"),
             ("mac mini", "home", "OS X 10.6", "", "320 GiB"),
             ("mac mini", "home", "OS x 10.6", "", "500 GiB"),
             ("apple tv", "home", "ubuntu 10.10", "", ""),
             ("airport extreme", "home", "", "", ""),
             ("media center", "home", "Windows 7", "", "1 TiB"))

    return render_to_response("sysconf.html", context=locals())

def testra(request):
    SUCCESS = '<font color="green">Success</font>'
    FAILURE =  '<font color="red">Failure</font>'
    head = ("Invocation", "Date", "Result")
    items = (("fiber switch automation", "", SUCCESS),
             ("migration to power 9", "", SUCCESS),
             ("take over IT", "", SUCCESS),
             ("replace sysaid with jira", "", SUCCESS),
             ("secretary in the 37th floor", "", SUCCESS),
             ("wifi in toilets", "", FAILURE))
    return render_to_response("testra.html", context=dict(head=head, items=items))


