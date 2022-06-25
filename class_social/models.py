from datetime import datetime
from pydantic import BaseModel


# "A permission is a set of booleans that determine what a user can do."
# The above class is a model of the permissions that a user can have
class Permission(BaseModel):

    # regarding posts
    view_post: bool
    create_post: bool
    edit_post: bool
    delete_post: bool
    comment_on_post: bool
    like_post: bool
    share_post: bool

    # regarding education
    create_curriculum: bool
    edit_curriculum: bool

    create_classroom: bool
    edit_classroom: bool

    create_course: bool
    edit_course: bool

    create_assignment: bool
    edit_assignment: bool
    correct_assignment: bool

    create_discussion_blog: bool

    # regarding research
    create_research_project: bool
    edit_research_project: bool
    close_research_project: bool

    # database access
    import_data: bool
    export_data: bool


# A User is a person who has a username, password, email, first name, last name, id number, gender, phone number, address,
# creation date, permissions, association, created posts, research projects, prospective status, and active status.
class User(BaseModel):

    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    id_number: str
    gender: str
    phone_number: str
    address: str
    creation_date: datetime     # Date User was created in system
    permissions: Permission
    association: []
    created_posts: []
    research_projects: []
    prospective: bool
    active: bool


# `A user can be a researcher, student, teacher, or mentor.`
# 
# This is a good start, but it's not enough. We need to know more about the relationships between these classes
class Researcher(User):

    leading_research_projects: []


class Student(User):

    current_courses: []
    previous_courses: []


class Teacher(User, Researcher):

    courses_in_progress: []
    previous_courses: []


class Mentor(User):

    courses_in_progress: []


# It's a class that defines the attributes of an organization.
class Organization(BaseModel):

    name: str
    address: str
    email_addresses: []
    phone_numbers: []
    url: str
    description: str
    reference_number: int
    associates: []
    head_of_organization: str
    research_institution: bool
    education_institution: bool
    research_projects: []
    courses: []
    offers: []


# > This class is a model for the type of post
# It's a class that defines the attributes of a post.
class TypeOfPost(BaseModel):

    internship_offer: bool
    job_offer: bool
    sponsorship_offer: bool
    scholarship_offer: bool
    discussion_blog: bool


# A post has a title, body, creator, creation date, type, comments, likes, and shares
# It's a class that defines the attributes of a post.
class Post(BaseModel):

    title: str
    body: []
    creator: User
    creation_date: datetime
    type: TypeOfPost
    comments_on_this_post: []
    likes_for_this_post: []
    shares_for_this_post: []


# `EducationObject` is a class that has an `organization`, a list of `members`, a `title`, and a `description`
# It's a class that defines the attributes of an education object.
class EducationObject(BaseModel):

    organization: Organization
    members: []
    title: str
    description: str


# A ResearchProject is an EducationObject that has a leader, a list of collaborators, and a url.
# It's a class that defines the attributes of a research project.
class ResearchProject(EducationObject):

    leader: Researcher
    collaborators: []
    url: str


# A Curriculum is an EducationObject that has a list of courses.
# It's a class that defines the attributes of a curriculum.
class Curriculum(EducationObject):

    courses: []


# A course is an education object that has a teacher, material, start date, end date, and assignments.
# It's a class that defines the attributes of a course.
class Courses(EducationObject):

    teacher: Teacher
    material: []
    start_date: datetime
    end_date: datetime
    assignments: []


# An Assignment is a education object that has a creator, a date, and a grades attribute
# It's a class that defines the attributes of an assignment.
class Assignment(EducationObject):

    creator: Teacher
    date: datetime
    # grades: {Student: int, Student: int}
    grades: []
