from jinjango import render_to_response



def _generic_handler(template_name):
    def handler(request):
        return render_to_response(template_name)
    return handler

index = _generic_handler("index.html")
quotes = _generic_handler("quotes.html")
testra = _generic_handler("testra.html")
sysconf = _generic_handler("sysconf.html")
