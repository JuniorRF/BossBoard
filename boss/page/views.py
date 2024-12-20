from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
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



@login_required
def delete_call(request, call_id):
    call = get_object_or_404(Call, id=call_id)
    if request.method == 'POST':
        call.delete()
        return redirect('index')
    # return render(request, 'confirm_delete.html', {'call': call})


@login_required
def edit_call(request, call_id):
    call = get_object_or_404(Call, id=call_id)
    if request.method == 'POST':
        form = CallForm(request.POST, instance=call)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на главную страницу после успешного сохранения
    else:
        form = CallForm(instance=call)

    context = {
        'form': form,
        'call': call,
    }
    return render(request, 'edit_call.html', context)