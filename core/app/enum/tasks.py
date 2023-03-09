import enum


class CompleteStatus(str, enum.Enum):
    in_progress = 'in_progress'
    done = 'done'
