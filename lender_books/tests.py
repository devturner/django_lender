from django.test import TestCase, RequestFactory
from .models import Book


class TestBookModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(isbn='4444', title='Feed the Cat', author='Sue Me', year='1992')
        Book.objects.create(isbn='4344' title='Blarps', author='Wat Stick', year='1942')
        Book.objects.create(isbn='4544' title='Wings are Wild', author='June Roth', year='1985')


     def test_book_titles(self):
        self.assertEqual(self.book.title, 'Feed the cat')


     def test_book_detail(self):
        book = Bote.objects.get(title='Blarps')
         self.assertEqual(book.author, 'Wat Stick')


#  class TestNoteViews(TestCase):
#     def setUp(self):
#         self.request = RequestFactory()
#         self.note_one = Note.objects.create(title='blarp', description='wat stick')
#         self.note_two = Note.objects.create(title='Gnarf', description='wat dat')
#      def test_note_detail_view(self):
#         from .views import notes_detail_view
#         request = self.request.get('')
#         response = notes_detail_view(request, f'{self.note_one.id}')
#         self.assertIn(b'wat stick', response.content)
#      def test_note_detail_status(self):
#         from .views import notes_detail_view
#         request = self.request.get('')
#         response = notes_detail_view(request, f'{self.note_one.id}')
#         self.assertEqual(200, response.status_code)
