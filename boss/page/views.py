from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Call, Birthday, Reception
from .forms import CallForm


@login_required
def index(request):
    calls = Call.objects.all()
    birthdays = Birthday.objects.all()
    receptions = Reception.objects.all()
    
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на главную страницу после успешного сохранения
    else:
        form = CallForm()

    context = {
        'calls': calls,
        'birthdays': birthdays,
        'receptions': receptions,
        'form': form,
    }
    return render(request, 'index.html', context)



def create_call(request):
    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CallForm()
    return render(request, 'create_call.html', {'form': form})