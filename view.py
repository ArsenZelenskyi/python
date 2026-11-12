from typing import List, Optional
from models import Task


class TaskView:
    @staticmethod
    def show_tasks(tasks: List[Task]) -> None:
        if not tasks:
            print("\n[!] Список задач порожній.\n")
            return

        header = f"{'ID':<36} | {'Опис':<20} | {'Статус':<12} | {'Створено':<16} | {'Заплановано на':<16}"
        print("\n" + "=" * len(header))
        print(header)
        print("-" * len(header))

        for task in tasks:
            created = task.created_at.strftime("%Y-%m-%d %H:%M")
            scheduled = task.schedule_for.strftime("%Y-%m-%d %H:%M")
            desc = (task.description[:17] + "...") if len(task.description) > 20 else task.description
            print(f"{str(task.id):<36} | {desc:<20} | {task.status.value:<12} | {created:<16} | {scheduled:<16}")

        print("=" * len(header) + "\n")

    @staticmethod
    def show_single_task(task: Optional[Task]) -> None:
        if task is None:
            print("\n[!] Задачу з таким ID не знайдено.\n")
        else:
            TaskView.show_tasks([task])

    @staticmethod
    def show_message(message: str) -> None:
        print(f"\n>>> {message}")