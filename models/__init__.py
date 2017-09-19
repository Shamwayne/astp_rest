from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship
from datetime import datetime

engine = create_engine('sqlite:///models.sqlite', echo=True)
Base = declarative_base()

"""
using classes from:
=> user.py
=> event.py
=> academic.py

"""


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    middlename = Column(String)
    surname = Column(String)
    physicalAddress = Column(String)
    dateOfBirth = Column(DateTime)
    avatar = Column(String)
    username = Column(String)
    password = Column(String)
    profileLastChanged = Column(DateTime)
    profileChangedBy = Column(Integer)
    active = Column(Boolean)
    reasonForDeactivation = Column(String)
    gender = Column(String(6))
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }

    def __repr__(self):
        rstring = "<Person name='{}' surname='{}' username='{}' active='{}' >"
        return rstring.format(self.firstname, self.surname, self.username, self.active)


class Employee(Person):
    __tablename__ = 'employee'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    email = Column(String)
    phoneNumber = Column(String)
    nationalID = Column(String, unique=True)

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
    }


class Teacher(Employee):
    __tablename__ = 'teacher'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    teacherType = Column(String)
    status = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'teacher',
    }

    def __repr__(self):
        rstring = "<Teacher name='{}' surname='{}' type='{}', status='{}' >"
        return rstring.format(self.firstname, self.surname, self.type, self.status)


class Administrator(Employee):
    __tablename__ = 'administrator'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)

    def __repr__(self):
        rstring = "<Admin name='{}' surname='{}' active='{}' email='{}' >"
        return rstring.format(self.firstname, self.surname, self.active, self.email)

    __mapper_args__ = {
        'polymorphic_identity': 'administrator',
    }


class Principal(Employee):
    __tablename__ = 'principal'
    id = Column(Integer, ForeignKey('employee.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'principal',
    }


class Guardian(Person):
    __tablename__ = 'guardian'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    email = Column(String)
    phoneNumber = Column(String)
    nationalID = Column(String, unique=True)

    def __repr__(self):
        rstring = "<Guardian name='{}' surname='{}' email='{}' >"
        return rstring.format(self.firstname, self.surname, self.email)

    __mapper_args__ = {
        'polymorphic_identity': 'guardian',
    }


class GuardianStudentRel(Base):
    __tablename__ = 'guardianStudentRel'
    id = Column(Integer, primary_key=True)
    guardian = Column(Integer, ForeignKey('guardian.id'))
    child_id = Column(Integer, ForeignKey('student.id'))


class Student(Person):
    __tablename__ = 'student'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    studentID = Column(String, unique=True)
    bcNumber = Column(String)
    class_id = Column(Integer, ForeignKey('class.id'))
    guardians = relationship('Guardian',
                             backref=backref('child_of', lazy='dynamic'))

    def __repr__(self):
        rstring = "<Student name='{}' surname='{}' email='{}' >"
        return rstring.format(self.firstname, self.surname, self.email)

    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    accountID = Column(String, unique=True)
    holder = Column(String, ForeignKey('student.id'))


class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    accountID = Column(String, ForeignKey('account.accountID'))
    dateAdded = Column(DateTime)
    amountPaid = Column(Float)
    datePaid = Column(DateTime)
    balance = Column(Float)
    paymentDescription = Column(String)
    receiptNumber = Column(String)
    dateLastModified = Column(DateTime)
    lastModifiedBy = Column(Integer, ForeignKey('person.id'))


# class Qualifications(Base):
#     # TODO: Implementation of Qualifications class
#     pass
#
# # TODO: linking qualifications class with teachers and school employees etc.

class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    dateAdded = Column(DateTime, default=datetime.now)
    taughtBy = Column(Integer, ForeignKey('teacher.id'))
    addedBy = Column(Integer, ForeignKey('person.id'))
    modifiedBy = Column(Integer, ForeignKey('person.id'))


class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    formTeacher = Column(Integer, ForeignKey('teacher.id'))
    dateAdded = Column(DateTime, default=datetime.now)
    addedBy = Column(Integer, ForeignKey('teacher.id'))
    modifiedBy = Column(Integer, ForeignKey('person.id'))
    dateModified = Column(DateTime, default=datetime.now)


class CurriculumLevel(Base):
    __tablename__ = 'curriculum_level'
    id = Column(Integer, primary_key=True)
    dateAdded = Column(DateTime, default=datetime.now)
    addedBy = Column(Integer, ForeignKey('person.id'))
    modifiedBy = Column(Integer, ForeignKey('person.id'))


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    addedBy = Column(Integer, ForeignKey('teacher.id'))
    subject = Column(Integer, ForeignKey('subject.id'))
    notes = Column(String)
    lastModified = Column(DateTime, default=datetime.now)
    lastModifiedBy = Column(Integer, ForeignKey('teacher.id'))


class Homework(Base):
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    dateAdded = Column(DateTime, default=datetime.now)
    dateDue = Column(DateTime, default=datetime.now)
    content = Column(String)
    addedBy = Column(Integer, ForeignKey('teacher.id'))
    subject = Column(Integer, ForeignKey('subject.id'))
    submissionType = Column(String)
    status = Column(Boolean)


class HomeworkSubmissions(Base):
    __tablename__ = 'homework_submissions'
    id = Column(Integer, primary_key=True)
    submittedBy = Column(Integer, ForeignKey('student.id'))
    homework = Column(Integer, ForeignKey('homework.id'))
    dateOfSubmission = Column(DateTime, default=datetime.now)


class AcademicResult(Base):
    __tablename__ = 'academic_results'
    id = Column(Integer, primary_key=True)
    student = Column(Integer, ForeignKey('student.id'))
    subject = Column(Integer, ForeignKey('subject.id'))
    result = Column(Float)
    total = Column(Float)
    resultFor = Column(Float)
    dateAdded = Column(DateTime, default=datetime.now)
    addedBy = Column(Integer, ForeignKey('teacher.id'))
    dateLastModified = Column(DateTime, default=datetime.now)
    comment = Column(String)
    grade = Column(Integer, ForeignKey('grade.id'))


class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    gradeName = Column(String)
    symbol = Column(String(2))
    grade_from = Column(Float)
    grade_to = Column(Float)
    addedBy = Column(Integer, ForeignKey('person.id'))
    dateAdded = Column(DateTime, default=datetime.now)
    description = Column(String)


class Notification(Base):
    __tablename__ = 'notifications'
    id = Column(Integer, primary_key=True)
    note = Column(String)
    addedBy = Column(Integer, ForeignKey('person.id'))  # ???
    dateAdded = Column(DateTime, default=datetime.now)
    type = Column(String)
    addressedTo = Column(String)


class ViewedNotifications(Base):
    __tablename__ = 'viewed_notifications'
    id = Column(Integer, primary_key=True)
    viewedBy = Column(Integer, ForeignKey('person.id'))  # ???
    dateViewed = Column(DateTime, default=datetime.now)
    notification = Column(Integer, ForeignKey('notifications.id'))


class Timetable(Base):
    __tablename__ = 'timetable'
    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey('class.id'))
    date = Column(DateTime)
    timeFrom = Column(DateTime, default=datetime.now)
    duration = Column(Integer)
    subject = Column(Integer, ForeignKey('subject.id'))
    createdBy = Column(Integer, ForeignKey('person.id'))


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    eventName = Column(String)
    dateDue = Column(String, default=datetime.now)
    addedBy = Column(Integer, ForeignKey('administrator.id'))
    eventType = Column(String)
    venue = Column(String)
    description = Column(String)


class PhotoGallery(Base):
    __tablename__ = 'photo_gallery'
    id = Column(Integer, primary_key=True)
    galleryName = Column(String)
    createdBy = Column(Integer, ForeignKey('administrator.id'))
    dateCreated = Column(DateTime, default=datetime.now)
    lastModifiedBy = Column(Integer, ForeignKey('administrator.id'))


class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dateAdded = Column(DateTime, default=datetime.now)
    gallery = Column(Integer, ForeignKey('photo_gallery.id'))
    fileUpload = Column(Integer, ForeignKey('file_uploads.id'))


class FileUpload(Base):
    __tablename__ = 'file_uploads'
    id = Column(Integer, primary_key=True)
    fileName = Column(String)
    savedAS = Column(String)
    dateUploaded = Column(DateTime, default=datetime.now)
    fileType = Column(String)
    uploadBy = Column(Integer, ForeignKey('person.id'))


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    from_person = Column(Integer, ForeignKey('person.id'))
    to_person = Column(Integer, ForeignKey('person.id'))
    dateSent = Column(DateTime, default=datetime.now)
    viewed = Column(Boolean)
    dateViewed = Column(DateTime, default=datetime.now)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
#
