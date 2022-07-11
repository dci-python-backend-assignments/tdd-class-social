from datetime import datetime
from typing import Optional, List, Union


from pydantic import BaseModel


class User(BaseModel):
    id: str
    username: str
    password: str
    email: str
    created_on: datetime
    is_active: bool
    name: str
    address: str
    role: str
    website: Optional[str]
    connections: Optional[List['User']]
    about: Optional[str]
    role: Optional[str]


class Person(User):
    date_of_birth: datetime
    gender: str
    phone_number: str


class Student(Person):
    current_courses: Optional[List['Course']]
    completed_courses: Optional[List['Course']]
    institution: Optional['Institution']
    interests: Optional[List[str]]


class Teacher(Person):
    courses_in_progress: Optional[List['Course']]
    old_courses: Optional[List['Course']]
    future_courses: Optional[List['Course']]
    institution: Optional['Institution']
    interests: Optional[List[str]]


class Institution(User):
    phone_numbers: List[str]
    associates: Optional[List[Union[Student, Teacher]]]
    head_of_organization: str
    research_institution: bool
    education_institution: bool
    research_projects: Optional[List[str]]
    active_courses: Optional[List['Course']]
    inactive_courses: Optional[List['Course']]
    offers: Optional[List['Course']]


User.update_forward_refs()


class Course(BaseModel):
    title: str
    starting_date: datetime
    end_date: datetime
    starting_time: datetime
    end_time: datetime
    teacher: Optional[Teacher]


class Post(BaseModel):
    title: str
    body: str
    creator: User
    creation_date: datetime
    comments_on_this_post: Optional[List[str]]
    likes_for_this_post: Optional[List[Union[Student, Teacher, Institution]]]
    shares_for_this_post: Optional[List[Union[Student, Teacher, Institution]]]
    type_of_post: str

# -----------Authentication------- #20_begin
class UserAuthenticate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

# -----------End Authentication------- #20_end
