from datetime import datetime
from typing import List, Optional
import uuid
from models import Task, TaskStatus


class TaskController:
    def __init__(self):
        self.tasks: List[Task] = []

    def create_task(self, description: str, schedule_for: datetime) -> Task:
        new_task = Task(description=description, schedule_for=schedule_for)
        self.tasks.append(new_task)
        return new_task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_task_by_id(self, task_id: uuid.UUID) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def filter_by_status(self, status: TaskStatus) -> List[Task]:
        return [task for task in self.tasks if task.status == status]

    def update_status(self, task_id: uuid.UUID, new_status: TaskStatus) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task.status = new_status
            return True
        return False

    def update_task(self, task_id: uuid.UUID, new_description: str, new_schedule: datetime) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task.description = new_description
            task.schedule_for = new_schedule
            return True
        return False

    def delete_task(self, task_id: uuid.UUID) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False