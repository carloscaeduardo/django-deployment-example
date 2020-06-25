from django.shortcuts import render

# Create your views here.
def index(request):
    """
    Parameters
    ----------
    request : request
    Returns the rendered index.html page.
    -------

    """
    context_dict = {'text':'This it the index page, be careufull', 'number':'your number is 123456, never forget it'}
    return render(request,'basic_app/index.html', context_dict)

def other(request):
    """
    Parameters
    ----------
    request : request
    Returns the rendered other.html page.
    -------

    """
    return render(request,'basic_app/other.html')

def relative(request):
    """
    Parameters
    ----------
    request : request
    Page with examples of the relative pathes.
    Returns the rendered relative_url_templates.html page.
    -------

    """
    return render(request,'basic_app/relative_url_templates.html')