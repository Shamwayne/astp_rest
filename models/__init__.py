from .academic import Subject, Class, CurriculumLevel, Note, Homework, HomeworkSubmissions, AcademicResult, Grade
from .user import Teacher, Administrator, Principal, Guardian, Student, Account, Transactions, Qualifications
from .event import Notification, ViewedNotifications, Timetable, Event, PhotoGallery, Photo, FileUpload, Message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///model.sqlite', echo=True)

Session = sessionmaker(bind=engine)
session = Session()
#
