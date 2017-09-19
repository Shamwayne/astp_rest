from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('', echo=True)
Base = declarative_base()


class Subject(Base):
    id = Column(Integer, primary_key=True)
    dateAdded = Column(DateTime, default=datetime.now)
    # TODO: taughtBy = reference -> teacher
    # TODO: addedBy  = reference -> person
    # TODO: modifiedBY = reference -> person


class Class(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # TODO: formTeacher = reference -> teacher
    dateAdded = Column(DateTime, default=datetime.now)
    # TODO: addedBy = reference -> teacher
    # TODO: modifiedBY = reference -> person
    dateModified = Column(DateTime, default=datetime.now)


class CurriculumLevel(Base):
    id = Column(Integer, primary_key=True)
    dateAdded = Column(DateTime, default=datetime.now)
    # TODO: addedBy = reference -> person
    # TODO: modifiedBY = reference -> person


class Notes(Base):
    id = Column(Integer, primary_key=True)
    # TODO: addedBy = reference -> teacher
    # TODO: subject = reference -> subject
    notes = Column(String)
    lastModified = Column(DateTime, default=datetime.now)
    # TODO: lastModifiedBy = reference -> teacher


class Homework(Base):
    id = Column(Integer, primary_key=True)
    dateAdded = Column(DateTime, default=datetime.now)
    dateDue = Column(DateTime, default=datetime.now)
    content = Column(String)
    # TODO: addedBy = reference -> teacher
    # TODO: subject = reference -> subject
    submissionType = Column(String)
    status = Column(Boolean)


class HomeworkSubmissions(Base):
    id = Column(Integer, primary_key=True)
    # TODO: submittedBy = reference -> student
    # TODO: homework = reference -> homework
    dateOfSubmission = Column(DateTime, default=datetime.now)


class AcademicResults(Base):
    id = Column(Integer, primary_key=True)
    # TODO: student = reference -> student
    # TODO: subject = reference -> subject
    result = Column(Float)
    total = Column(Float)
    resultFor = Column(Float)
    dateAdded = Column(DateTime, default=datetime.now)
    # TODO: addedBy = reference -> teacher
    dateLastModfied = Column(DateTime, default=datetime.now)
    comment = Column(String)
    # TODO: grade = reference -> grade


class Grade(Base):
    id = Column(Integer, primary_key=True)
    gradeName = Column(String)
    symbol = Column(String(2))
    grade_from = Column(Float)
    grade_to = Column(Float)
    # TODO: addedBy = reference -> person
    dateAdded = Column(DateTime, default=datetime.now)
    description = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
