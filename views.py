from jinjango import render_to_response



def _generic_handler(template_name):
    def handler(request):
        return render_to_response(template_name)
    return handler

index = _generic_handler("index.html")

HEAD = ("Product", "Location", "OS", "Gen", "Capacity")
PRODUCTS = (("iphone", "mobile", "iOS 4.1", "3gs", "8 GiB"),
            ("ipad", "mobile", "iOS 4.2", "1", "16 GiB"),
            ("mac book pro", "mobile", "OS X 10.6", "", "500 GiB"),
            ("mac mini", "home", "OS X 10.6", "", "320 GiB"),
            ("mac mini", "home", "OS x 10.6", "", "500 GiB"),
            ("apple tv", "home", "ubuntu 10.10", "", ""),
            ("airport extreme", "home", "", "", ""),
            ("media center", "home", "Windows 7", "", "1 TiB"))

def sysconf(request):
    return render_to_response("sysconf.html", context=dict(head=HEAD,
                                                           products=PRODUCTS))

testra = _generic_handler("testra.html")
quotes = _generic_handler("quotes.html")

