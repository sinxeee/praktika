from .models import ClientRequest

def add_request(description):
    """Добавление новой заявки"""
    return ClientRequest.objects.create(description=description, status='new')

def edit_request(request_id, new_status):
    """Редактирование статуса заявки по ID"""
    try:
        req = ClientRequest.objects.get(id=request_id)
        req.status = new_status
        req.save()
        return True
    except ClientRequest.DoesNotExist:
        return False

def delete_request(request_id):
    """Удаление заявки по ID"""
    deleted_count, _ = ClientRequest.objects.filter(id=request_id).delete()
    return deleted_count > 0

# --- БЛОК РЕФАКТОРИНГА (Пункт 5 ТЗ) ---

# БЫЛО (Плохой код: загрузка всего в память и фильтрация в Python):
# def search_requests_bad(status):
#     all_requests = ClientRequest.objects.all()
#     result = []
#     for req in all_requests:
#         if req.status == status:
#             result.append(req)
#     return result

# СТАЛО (Хороший код: фильтрация на уровне SQL через ORM):
def search_requests_by_status(status):
    """Поиск заявок по статусу. Оптимизированный вариант."""
    return ClientRequest.objects.filter(status=status)