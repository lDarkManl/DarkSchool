from django.test import TestCase, Client
from django.urls import reverse

from courses import models as cm
from accounts import models as am
from courses import views


class TestCourses(TestCase):
    def setUp(self):
        self.discipline = cm.Discipline.objects.create(title='Математика')
        self.task = cm.Task.objects.create(discipline=self.discipline, text='Текст задачи', answer='Ответ на задачу')
        self.user = am.User.objects.create_user(username='testuser', password='12345', is_teacher=True)
        self.teacher = am.TeacherAccount.objects.create(name='Дмитрий', age=20, info='Информация', discipline=self.discipline, user=self.user)
        self.student = am.StudentAccount.objects.create(name='Дмитрий', age=20, info='Информация', user=self.user)
        self.course = cm.Course.objects.create(title='Курс 1', price=200, teacher=self.teacher, discipline=self.discipline)
        self.lesson = cm.Lesson.objects.create(title='Урок 1', video='https://www.youtube.com/watch?v=w4nrT7emiVc&t=935s', type=cm.Lesson.types[0][0])
        self.lesson.courses.add(self.course)
        self.lesson.tasks.add(self.task)
        self.answer_lesson = cm.StudentAnswerLesson.objects.create(answer='Ответ на задачу', task=self.task, lesson=self.lesson, student=self.student)
        self.client = Client()

    def test_course(self):
        self.assertEqual(str(self.course), 'Курс 1')

    def test_lesson(self):
        self.assertEqual(str(self.lesson), 'Урок 1')

    def test_answer(self):
        self.assertEqual(str(self.answer_lesson), 'Ответ на задачу')

    def test_check_answer_true(self):
        self.assertEqual(self.answer_lesson.check_answer(), True)

    def test_courses_views(self):
        response = self.client.get(reverse('courses:courses'))

        self.assertEquals(response.status_code, 200)

    def test_course_views(self):
        response = self.client.get(reverse('courses:course', args=[self.course.id]))

        self.assertEquals(response.status_code, 200)

    def test_lesson_view(self):
        response = self.client.get(reverse('courses:lesson', args=[self.lesson.id]))

        self.assertEquals(response.status_code, 200)

