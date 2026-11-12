from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import uuid


class TaskStatus(Enum):
    TODO = "ToDo"
    IN_PROGRESS = "InProgress"
    DONE = "Done"


@dataclass
class Task:
    description: str
    schedule_for: datetime
    status: TaskStatus = TaskStatus.TODO
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now)