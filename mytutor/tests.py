from django.test import TestCase
# from django.contrib.auth import custom_user_model
# from django.contrib.auth import AbstractUser
#from django.contrib.auth import get_user_model
from mytutor.models import Booking, User, Comment, Course, EnrolledCourse
from django.contrib.auth.hashers import make_password



class UserTests(TestCase):
    # Create your tests here.

    def test_create_user(self):
        #abstractUser = get_user_model()
        u = User.objects.create(first_name='test', last_name='surn', email='test@gmail.com',
                                             username='testUsername', password=make_password('qwerty'), role='student')
        u.save()
        self.assertEqual(u.username == 'testUsername', True)
        self.assertEqual(u.last_name=='surn', True)


    def test_user_booking(self):
        t = User.objects.create(first_name='testteach', last_name='surnteach',email='testteacher@gmail.com',
                                              username='testteachUsername', password=make_password('qwerty'),
                                              role='teacher')
        t.save()

        s = User.objects.create(first_name='test', last_name='surn', email='test@gmail.com',
                                     username='testUsername', password=make_password('qwerty'), role='student')
        s.save()
        booking_nums = len(Booking.objects.all())
        book1 = Booking.objects.create(teacher=t, student=s, is_accepted=False, date="2020-04-01", time="12:00")
        book1.save()
        self.assertEqual(len(Booking.objects.all()), booking_nums + 1)

    def test_user_comment(self):
        course = Course.objects.create(description = ' alg desc', title = ' algorithms', credit = 10)
        course.save()

        s = User.objects.create_user(first_name='test', last_name='surn', email='test@gmail.com',
                                     username='testUsername', password=make_password('qwerty'), role='student')
        s.save()

        comment_nums = len(Comment.objects.all())
        com1 = Comment.objects.create(user=s, content = 'test comment', course = course)
        com1.save()
        self.assertEqual(len(Comment.objects.all()), comment_nums + 1)


    def test_enrol(self):
        c = Course.objects.create(description=' alg desc', title=' algorithms', credit=10)
        c.save()

        s = User.objects.create_user(first_name='test', last_name='surn', email='test@gmail.com',
                                     username='testUsername', password=make_password('qwerty'), role='student')
        s.save()
        enrol_nums = len(EnrolledCourse.objects.all())
        e= EnrolledCourse.objects.create(user=s, course=c)

        self.assertEqual(len(EnrolledCourse.objects.all()), enrol_nums + 1)