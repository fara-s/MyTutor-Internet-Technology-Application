import os

import django
from django.contrib.auth.hashers import make_password


def create_user(first_name, last_name, username, email, password, role):
    user = User.objects.create(first_name=first_name, last_name=last_name, email=email, username=username,
                               password=make_password(password),
                               role=role)
    return user


def create_course(title, description, credit):
    course = Course.objects.create(title=title, description=description, credit=credit)
    return course


def create_course_teacher(teacher, course):
    course_teacher = CourseTeacher.objects.create(teacher=teacher, course=course)
    return course_teacher


def create_comment(course, user, content):
    comment = Comment.objects.create(course=course, user=user, content=content)
    return comment


def create_booking(teacher, student, date, time):
    booking = Booking.objects.create(teacher=teacher, student=student, date=date, time=time)
    return booking


def create_enrolled_course(user, course):
    course = EnrolledCourse.objects.create(user=user, course=course)
    return course


def populate():
    teacher_1 = create_user("john", "doe", "john", "john@email.com", "123456", "teacher")
    teacher_2 = create_user("johnd", "xerks", "xerks", "xerks@email.com", "123456", "teacher")
    user_1 = create_user("john", "iasoma", "iasoma", "iasoma@email.com", "123456", "student")
    user_2 = create_user("mohit", "kur", "mohit", "mohit@email.com", "123456", "student")

    course_1 = create_course("ALGORITHMIC FOUNDATIONS 2 COMPSCI2003",
                             "To introduce the foundational mathematics needed for Computing Science; To make students proficient in their use; "
                             "To show how they can be applied to advantage in understanding computational phenomena.",
                             5)

    course_2 = create_course("WEB APPLICATION DEVELOPMENT 2 COMPSCI2021",
                             "The aim of this course is to provide students with a comprehensive overview of web application development.",
                             6)

    course_3 = create_course("TEAM PROJECT 3 COMPSCI3004",
                             "This course gives students the experience of working on a substantial team based software project.",
                             5)

    create_course_teacher(teacher_1, course_1)
    create_course_teacher(teacher_2, course_2)
    create_course_teacher(teacher_1, course_2)

    now = datetime.datetime.now()

    create_booking(teacher_1, user_1, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"))
    create_booking(teacher_2, user_1, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"))
    create_booking(teacher_2, user_2, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"))

    create_comment(course_1, user_1, "First comment")
    create_comment(course_1, user_2, "Course was good")
    create_comment(course_2, user_1, "I learned a lot")
    create_comment(course_3, user_1, "I learned a lot of things")

    create_enrolled_course(user_1, course_1)
    create_enrolled_course(user_1, course_2)
    create_enrolled_course(user_2, course_2)
    create_enrolled_course(user_2, course_3)
    create_enrolled_course(user_2, course_1)


if __name__ == '__main__':
    print("Start populating..")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyTutorApplication.settings')
    django.setup()
    from mytutor.models import *

    populate()
