from django.test import TestCase, RequestFactory
from django.core import mail
from django.contrib.auth.models import User
from django.http import Http404

from .models import Book


class TestBookModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', email='test@example.com')
        self.user.set_password('hello')

        self.book = Book.objects.create(
            isbn='4444',
            title='Feed the Cat',
            author='Sue Me',
            year='1992',
            user=self.user,
            )

        Book.objects.create(isbn='4344', title='Blarps', author='Wat Stick', year='1942', user=self.user,)
        Book.objects.create(isbn='4544', title='Wings are Wild', author='June Roth', year='1985', user=self.user,)

    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Feed the Cat')

    def test_book_detail(self):
        book = Book.objects.get(title='Blarps')
        self.assertEqual(book.author, 'Wat Stick')


class TestBookViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', email='test@example.com')
        self.user.set_password('hello')

        self.request = RequestFactory()

        self.book_1 = Book.objects.create(
            isbn='4444',
            title='Feed the Cat',
            author='Sue Me',
            year='1992',
            user=self.user,
            )

        self.book_2 = Book.objects.create(
            isbn='4544',
            title='Wings are Wild',
            author='June Roth',
            year='1985',
            user=self.user,
            )

    def test_book_detail_view(self):
        from .views import book_detail_view
        request = self.request
        request.user = self.user
        response = book_detail_view(request, f'{self.book_1.id}')
        self.assertIn(b'Feed the Cat', response.content)

    def test_book_detail_status(self):
        from .views import book_detail_view
        request = self.request
        request.user = self.user
        response = book_detail_view(request, f'{self.book_2.id}')
        self.assertEqual(200, response.status_code)

    def test_book_detail_view_fail_on_other_user(self):
        from .views import book_detail_view
        request = self.request
        request.user = User.objects.create(username='test2', email='another@test.com')
        request.user.set_password('4321')
        with self.assertRaises(Http404):
            response = book_detail_view(request, f'{self.book_1.id}')


class EmailTest(TestCase):
    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
            'djangosenderseattle@gmail.com', ['to@example.com'],
            fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
