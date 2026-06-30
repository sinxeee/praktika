from django.db import models

class ClientRequest(models.Model):
    STATUS_CHOICES = [
        ('new', 'новая'),
        ('in_progress', 'в работе'),
        ('closed', 'закрыта'),
    ]
    
    date = models.DateField(auto_now_add=True, verbose_name="дата")
    description = models.TextField(verbose_name="описание")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="статус")

    class Meta:
        db_table = 'requests' 
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'

    def __str__(self):
        return f"заявка #{self.id} ({self.status})"