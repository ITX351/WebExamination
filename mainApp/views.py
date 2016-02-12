from django.shortcuts import render_to_response


def test(request):
    return render_to_response('mainApp/index.html')
