from datetime import datetime
import uuid
from models import TaskStatus
from controller import TaskController
from view import TaskView


def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M")


def parse_uuid(id_str: str) -> uuid.UUID:
    return uuid.UUID(id_str.strip())


def main():
    controller = TaskController()
    view = TaskView()

    while True:
        print("=== МЕНЮ TODO LIST ===")
        print("1. Створити задачу")
        print("2. Змінити статус задачі (InProgress / Done)")
        print("3. Видалити задачу")
        print("4. Змінити задачу (опис та час)")
        print("5. Показати всі задачі")
        print("6. Відфільтрувати задачі за статусом")
        print("7. Знайти задачу за ID")
        print("0. Вихід")

        choice = input("\nОберіть дію: ").strip()

        try:
            if choice == "1":
                desc = input("Введіть опис задачі: ")
                date_input = input("Введіть дату та час (РРРР-ММ-ДД ГГ:ХХ): ")
                schedule_dt = parse_date(date_input)
                task = controller.create_task(desc, schedule_dt)
                view.show_message(f"Задачу створено! ID: {task.id}")

            elif choice == "2":
                task_id = parse_uuid(input("Введіть ID задачі: "))
                status_input = input("Новий статус (1 - InProgress, 2 - Done): ").strip()
                if status_input == "1":
                    new_status = TaskStatus.IN_PROGRESS
                elif status_input == "2":
                    new_status = TaskStatus.DONE
                else:
                    view.show_message("Невірний вибір статусу.")
                    continue

                if controller.update_status(task_id, new_status):
                    view.show_message("Статус успішно оновлено!")
                else:
                    view.show_message("Задачу не знайдено.")

            elif choice == "3":
                task_id = parse_uuid(input("Введіть ID задачі для видалення: "))
                if controller.delete_task(task_id):
                    view.show_message("Задачу видалено!")
                else:
                    view.show_message("Задачу не знайдено.")

            elif choice == "4":
                task_id = parse_uuid(input("Введіть ID задачі для редагування: "))
                new_desc = input("Введіть новий опис: ")
                new_date = parse_date(input("Введіть нову дату та час (РРРР-ММ-ДД ГГ:ХХ): "))
                if controller.update_task(task_id, new_desc, new_date):
                    view.show_message("Задачу оновлено!")
                else:
                    view.show_message("Задачу не знайдено.")

            elif choice == "5":
                tasks = controller.get_all_tasks()
                view.show_tasks(tasks)

            elif choice == "6":
                st = input("Оберіть статус (1 - ToDo, 2 - InProgress, 3 - Done): ").strip()
                status_map = {
                    "1": TaskStatus.TODO,
                    "2": TaskStatus.IN_PROGRESS,
                    "3": TaskStatus.DONE
                }
                if st in status_map:
                    filtered = controller.filter_by_status(status_map[st])
                    view.show_tasks(filtered)
                else:
                    view.show_message("Невірний статус.")

            elif choice == "7":
                task_id = parse_uuid(input("Введіть ID задачі: "))
                task = controller.get_task_by_id(task_id)
                view.show_single_task(task)

            elif choice == "0":
                view.show_message("Роботу завершено.")
                break

            else:
                view.show_message("Невідома команда, спробуйте ще раз.")

        except ValueError:
            view.show_message("Помилка формату даних (перевірте правильність ID або дати).")


if __name__ == "__main__":
    main()