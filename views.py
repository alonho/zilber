from jinjango import render_to_response

def index(request):
    return render_to_response("index.html")

def main(request):
    return render_to_response("main.html")
