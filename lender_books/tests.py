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


class TestBookViews(TestCase):
    def setup(self):
        self.request = RequestFactory()
        self.book_1 = Book.objects.create(isbn='4444', title='Feed the Cat', author='Sue Me', year='1992')
        self.book_2 = Book.objects.create(isbn='4544' title='Wings are Wild', author='June Roth', year='1985')

    def test_book_detail_view(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_1.id}')
        self.assertIn(b'Feed the Cat', response.content)

    def test_book_detail_status(self):
        from .views import books_detail_view
        request = self.request.get('')
        response = books_detail_view(request, f'{self.book_2.id}')
        self.assertEqual(200, response.status_code)
