from django.test import TestCase
from django.urls import reverse_lazy
from task.models.task import *
from django.contrib.auth.models import User
from .factories import *
# Create your tests here.

class TestTaskList(TestCase):
    def test_task_list_should_success(self):
        for i in range(3):
            task_obj = TestTaskFactory(name=f"test task number {i}")

        created_by = MentorFactory(
            user=task_obj.created_by
        )

        response = self.client.get(reverse_lazy("task:list"))        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test task number 0")
        self.assertContains(response, "test task number 1")
        self.assertContains(response, "test task number 2")

class TestTaskDetail(TestCase):
    def test_one_task_via_factory_boy(self):
        task_object = TestTaskFactory()
        response = self.client.get(f'/api/task/detail/{task_object.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, task_object.name)

class TestAnswerList(TestCase):
    def test_answer_list_should_success(self):
        for i in range(3):
            answer_obj = TestAnswerFactory(txt=f"test answer number {i}")

        # profile = ProfileFactory(
        #     # user=answer_obj.profile
        # )
        student = StudentFactory()
        response = self.client.get(reverse_lazy("answer:list"))        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test answer number 0")
        self.assertContains(response, "test answer number 1")
        self.assertContains(response, "test answer number 2")
        print(answer_obj.txt)

class TestAnswerDetail(TestCase):
    def test_one_answer_via_factory_boy(self):
        answer_obj = TestAnswerFactory()
        response = self.client.get(f'/api/answer/detail/{answer_obj.id}/')
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, answer_obj.txt)