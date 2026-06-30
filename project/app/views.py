from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ClientRequest
from .forms import ClientRequestForm


def index(request):
    """Главная страница: список заявок + форма добавления"""
    # Фильтр по статусу (если передан в GET-параметре ?status=...)
    status_filter = request.GET.get('status', '')
    
    if status_filter:
        requests_list = ClientRequest.objects.filter(status=status_filter)
    else:
        requests_list = ClientRequest.objects.all().order_by('-id')
    
    form = ClientRequestForm()
    
    context = {
        'requests_list': requests_list,
        'form': form,
        'status_filter': status_filter,
        'status_choices': ClientRequest.STATUS_CHOICES,
    }
    return render(request, 'app/index.html', context)


def add_request(request):
    """Обработчик добавления заявки"""
    if request.method == 'POST':
        form = ClientRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка успешно добавлена!')
    return redirect('index')


def edit_request_view(request, pk):
    """Редактирование заявки"""
    req = get_object_or_404(ClientRequest, pk=pk)
    if request.method == 'POST':
        form = ClientRequestForm(request.POST, instance=req)
        if form.is_valid():
            form.save()
            messages.success(request, f'Заявка #{pk} обновлена!')
    return redirect('index')


def delete_request_view(request, pk):
    """Удаление заявки"""
    if request.method == 'POST':
        req = get_object_or_404(ClientRequest, pk=pk)
        req.delete()
        messages.success(request, f'Заявка #{pk} удалена!')
    return redirect('index')