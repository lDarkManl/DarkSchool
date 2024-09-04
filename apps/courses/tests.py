from django.test import TestCase, Client
from django.urls import reverse

from courses import models as cm
from tasks import models as tm
from accounts import models as am
from courses import views


class TestCourses(TestCase):
    def setUp(self):
        self.discipline = cm.Discipline.objects.create(title='Математика')
        self.task = tm.Task.objects.create(discipline=self.discipline, text='Текст задачи', answer='Ответ на задачу')
        self.teacher = am.TeacherAccount.objects.create(name='Дмитрий', age=20, info='Информация', discipline=self.discipline)
        self.course = cm.Course.objects.create(title='Курс 1', price=200, teacher=self.teacher, discipline=self.discipline)
        self.lesson = cm.Lesson.objects.create(title='Урок 1', video='https://www.youtube.com/watch?v=w4nrT7emiVc&t=935s', course=self.course)
        self.lesson.tasks.add(self.task)
        self.webinar = cm.Webinar.objects.create(title='Вебинар 1', video='https://www.youtube.com/watch?v=w4nrT7emiVc&t=935s', course=self.course)
        self.webinar.tasks.add(self.task)
        self.answer_lesson = cm.StudentAnswerLesson.objects.create(answer='Ответ на задачу', task=self.task, lesson=self.lesson)
        self.answer_webinar = cm.StudentAnswerWebinar.objects.create(answer='Ответ не на задачу', task=self.task, webinar=self.webinar)
        self.client = Client()

    def test_course(self):
        self.assertEqual(str(self.course), 'Курс 1')

    def test_lesson(self):
        self.assertEqual(str(self.lesson), 'Урок 1')

    def test_webinar(self):
        self.assertEqual(str(self.webinar), 'Вебинар 1')

    def test_answer(self):
        self.assertEqual(str(self.answer_lesson), 'Ответ на задачу')

    def test_check_answer_true(self):
        self.assertEqual(self.answer_lesson.check_answer(), True)

    def test_check_answer_false(self):
        self.assertEqual(self.answer_webinar.check_answer(), False)

    def test_courses_views(self):
        response = self.client.get(reverse('courses:courses'))

        self.assertEquals(response.status_code, 200)

    def test_course_views(self):
        response = self.client.get(reverse('courses:course', args=[self.course.id]))

        self.assertEquals(response.status_code, 200)

    def test_lesson_view(self):
        response = self.client.get(reverse('courses:lesson', args=[self.lesson.id]))

        self.assertEquals(response.status_code, 200)

    def test_webinar_view(self):
        response = self.client.get(reverse('courses:webinar', args=[self.webinar.id]))

        self.assertEquals(response.status_code, 200)
