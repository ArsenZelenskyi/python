import unittest
from datetime import datetime
from models import TaskStatus
from controller import TaskController


class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.controller = TaskController()
        self.date = datetime(2026, 11, 15, 14, 30)
        self.task = self.controller.create_task("Зробити лабу", self.date)

    def test_create_and_get(self):
        self.assertEqual(len(self.controller.get_all_tasks()), 1)
        self.assertEqual(self.task.description, "Зробити лабу")
        self.assertEqual(self.task.status, TaskStatus.TODO)
        self.assertEqual(self.controller.get_task_by_id(self.task.id), self.task)

    def test_update_status(self):
        self.controller.update_status(self.task.id, TaskStatus.IN_PROGRESS)
        self.assertEqual(self.task.status, TaskStatus.IN_PROGRESS)

    def test_update_task(self):
        new_date = datetime(2026, 12, 1, 10, 0)
        self.controller.update_task(self.task.id, "Новий опис", new_date)
        self.assertEqual(self.task.description, "Новий опис")
        self.assertEqual(self.task.schedule_for, new_date)

    def test_filter_by_status(self):
        task2 = self.controller.create_task("Друга задача", self.date)
        self.controller.update_status(task2.id, TaskStatus.DONE)

        done_tasks = self.controller.filter_by_status(TaskStatus.DONE)
        self.assertEqual(len(done_tasks), 1)
        self.assertEqual(done_tasks[0].id, task2.id)

    def test_delete_task(self):
        self.controller.delete_task(self.task.id)
        self.assertEqual(len(self.controller.get_all_tasks()), 0)


if __name__ == "__main__":
    unittest.main()