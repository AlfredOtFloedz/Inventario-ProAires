from django.shortcuts import redirect

def inicio_autenticado(request):
    if request.user.is_authenticated:
        return redirect('pos-index')
    else:
        return redirect('user-login')