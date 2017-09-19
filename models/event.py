from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = create_engine('', echo=True)
Base = declarative_base()


class Notification(Base):
    id = Column(Integer, primary_key=True)
    note = Column(String)
    # TODO: addedBy = reference -> person
    dateAdded = Column(DateTime, default=datetime.now)
    type = Column(String)
    addressedTo = Column(String)


class ViewedNotifications(Base):
    # TODO: viewedBy = reference -> person
    dateViewed = Column(DateTime, default=datetime.now)
    # TODO: notification = reference -> notification


class Timetable(Base):
    # TODO: class = reference -> class
    date = Column(DateTime)
    timeFrom = Column(DateTime, datetime.now)
    duration = Column(Integer)
    # TODO: subject = reference -> subject
    # TODO: createdBy = reference -> person


class Event(Base):
    id = Column(Integer, primary_key=True)
    eventName = Column(String)
    dateDue = Column(String, default=datetime.now)
    # TODO: addedBy = reference -> administrator
    eventType = Column(String)
    venue = Column(String)
    description = Column(String)


class PhotoGallery(Base):
    id = Column(Integer, primary_key=True)
    galleryName = Column(String)
    # TODO: createdBy = reference -> administrator
    dateCreated = Column(DateTime, default=datetime.now)
    # TODO: lastModifiedBy = reference -> administrator


class Photo(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dateAdded = Column(DateTime, default=datetime.now)
    # TODO: gallery = reference -> gallery
    # TODO: fileUpload = reference -> fileUploads


class FileUpload(Base):
    id = Column(Integer, primary_key=True)
    fileName = Column(String)
    savedAS = Column(String)
    dateUploaded = Column(DateTime, default=datetime.now)
    fileType = Column(String)
    # TODO: uploadBy = reference -> person


class Message(Base):
    id = Column(Integer, primary_key=True)
    # TODO: from = reference -> person
    # TODO: to = reference -> person
    dateSent = Column(DateTime, default=datetime.now)
    viewed = Column(Boolean)
    dateViewed = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

