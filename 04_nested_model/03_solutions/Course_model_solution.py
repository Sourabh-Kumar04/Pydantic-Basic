from pydantic import BaseModel
from typing import List

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons
# Each lesson has a title and a description


class Lesson(BaseModel):
    lesson_id: int
    title: str
    description: str
    content: str

class Module(BaseModel):
    module_id: int
    title: str
    lessons: List[Lesson]
    content: str

class Course(BaseModel):
    course_id: int
    title: str
    module: List[Module]
    description: str
    content: str

lesson = Lesson(
    lesson_id = 1,
    title="Lesson",
    description="This is the first lesson",
    content="This is the content of the first lesson"
)

module = Module(
    module_id = 1,
    title="Module 1",
    lessons=[lesson],
    content="This is the content of the first module"
)

course = Course(
    course_id = 1,
    title="Course 1",
    module = [module],
    description = "This is the first course",
    content="This is the content of the first course"
)