from django.test import TestCase
from .models import ClientRequest
from .services import add_request, edit_request, search_requests_by_status, delete_request

class RequestSystemTests(TestCase):
    
    def test_1_add_and_search(self):
        add_request("Не работает принтер")
        add_request("Установить Windows")
        
        new_requests = search_requests_by_status('new')
        self.assertEqual(new_requests.count(), 2)
        self.assertEqual(new_requests[0].description, "Не работает принтер")

    def test_2_edit_request(self):
        req = add_request("Починить сервер")
        self.assertEqual(req.status, 'new')
        
        success = edit_request(req.id, 'in_progress')
        self.assertTrue(success)
        
        updated_req = ClientRequest.objects.get(id=req.id)
        self.assertEqual(updated_req.status, 'in_progress')

    def test_3_delete_request(self):
        req = add_request("Лишняя заявка")
        req_id = req.id
        
        success = delete_request(req_id)
        self.assertTrue(success)
        
        exists = ClientRequest.objects.filter(id=req_id).exists()
        self.assertFalse(exists)