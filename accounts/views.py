from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from accounts.forms import RegisterForm, LoginForm
from accounts.utils import login_required


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('books:book_list')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})



def login_(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # login formadagi username
            password = form.cleaned_data.get('password')  # login formadagi password

            # authenticate qilamiz
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # foydalanuvchi tizimga kiradi
                return redirect('books:book_list')
            else:
                # noto‘g‘ri username yoki password
                return render(request, 'accounts/login.html', {
                    'form': form,
                    'error': 'Username yoki password noto‘g‘ri'
                })
        else:
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_(request):
    logout(request)
    return redirect('accounts:login')