from django.shortcuts import render , redirect , HttpResponseRedirect
from django.contrib.auth.hashers import  check_password
from shop.models.customers import Customer
from django.views import  View


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, "login.html")

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        customer = Customer.get_customer(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                customer.update_time(email)
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('index')
            else:
                error_msg = "密碼錯誤"
        else:
            error_msg = "您並未註冊"
        return render(request, "login.html", {'error': error_msg})


def logout(request):
    request.session.clear()
    return redirect('login')