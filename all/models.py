import os
from sqlalchemy import(Column, INTEGER, ForeignKey, String, BigInteger, BINARY, func, Enum, VARCHAR)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
# from passlib.hash import bcrypt
from werkzeug.security import generate_password_hash
import sys

sys.path.append(r"C:\!Ilona\3 semestr\Programing\OnlineCourses")

dbUrl = os.getenv("dbUrl", "mysql+mysqlconnector://root:tomcat@localhost/onlinecourses")
engine = create_engine(dbUrl)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

baseModel = declarative_base()
baseModel.query = session.query_property()

class User(baseModel):
    __tablename__ = "user"

    id_user = Column(INTEGER, primary_key=True, nullable=False)
    first_name = Column(VARCHAR(128), nullable=False)
    last_name = Column(VARCHAR(128), nullable=False)
    user_name = Column(VARCHAR(128), nullable=False)
    password = Column(VARCHAR(128), nullable=False)
    email = Column(VARCHAR(128), nullable=False)
    status = Column(Enum('Teacher', 'Student'), nullable=False)

    def __init__(self, **kwargs):
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.user_name = kwargs.get('user_name')
        self.password = generate_password_hash(kwargs.get('password'))
        self.email = kwargs.get('email')
        self.status = kwargs.get('status')

    def __str__(self):
        return f"User id: {self.id_user}\n" \
               f"First name: {self.first_name}\n" \
               f"Last name: {self.last_name}\n" \
               f"User name: {self.user_name}\n" \
               f"Password: {self.password}\n" \
               f"Email: {self.email}\n" \
               f"Status: {self.status}\n"

class Course(baseModel):
    __tablename__ = "course"

    id_course = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(VARCHAR(128), nullable=False)
    theme = Column(VARCHAR(128), nullable=False)
    details = Column(VARCHAR(128), nullable=False)
    id_teacher = Column(INTEGER, ForeignKey('user.id_user'), nullable=False)

    def __str__(self):
        return f"Course id: {self.id_course}\n" \
               f"Name: {self.name}\n" \
               f"Theme: {self.theme}\n" \
               f"Details: {self.details}\n" \
               f"Teacher id: {self.id_teacher}\n"

class User_and_Course(baseModel):
    __tablename__ = "user_and_course"

    id = Column(INTEGER, primary_key=True, nullable=False)
    user_id = Column(INTEGER, ForeignKey('user.id_user'), nullable=False)
    id_courses = Column(INTEGER, ForeignKey('course.id_course'), nullable=False)

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"User id: {self.user.id}\n" \
               f"Name: {self.all_courses}\n"

class RequestForCourse(baseModel):
    __tablename__ = "request_for_course"

    id = Column(INTEGER, primary_key=True, nullable=False)
    id_user = Column(INTEGER, ForeignKey('user.id_user'), nullable=False)
    id_course = Column(INTEGER, ForeignKey('course.id_course'), nullable=False)

    def __str__(self):
        return f"Id: {self.id}\n" \
               f"Id_user: {self.id_user}\n" \
               f"Id_course: {self.id_course}\n"