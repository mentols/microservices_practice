from beanie import Document


class Page(Document):
    id: str
    page_id: int
    task_amount: int
    resolved: int
    unresolved: int
    resolution_percentage: float

