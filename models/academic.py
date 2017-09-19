from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .user import Person, Teacher, Student

engine = create_engine('sqlite:///model.sqlite', echo=True)
Base = declarative_base()


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

Base.metadata.create_all(engine)