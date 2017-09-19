from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from .user import Person, Administrator
from .academic import Subject

engine = create_engine('sqlite:///model.sqlite', echo=True)
Base = declarative_base()


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
    timeFrom = Column(DateTime, datetime.now)
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