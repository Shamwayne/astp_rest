# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, backref, relationship
from datetime import datetime

"""
Assumptions and Issues:
- can't figure out the 1-m relationship between Students and Parents
- can't figure out the 1-m relationship between Account and Student
- which class is Qualifications linking to and how?
- MISSING: class reference for Student class
- MISSING: Qualifications class
- INCOMPLETE: Account
"""

engine = create_engine('sqlite:///test1.sqlite', echo=True)

Base = declarative_base()


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
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }

    def __repr__(self):
        rstring = "<Person name='{}' surname='{}' username='{}' active='{}' >"
        return rstring.format(self.firstname, self.surname, self.username, self.active)


class Teacher(Person):
    __tablename__ = 'teacher'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    email = Column(String)
    phoneNumber = Column(String)
    teacherType = Column(String)
    status = Column(String)
    nationalID = Column(String, unique=True)

    __mapper_args__ = {
        'polymorphic_identity': 'teacher',
    }

    def __repr__(self):
        rstring = "<Teacher name='{}' surname='{}' type='{}', status='{}' >"
        return rstring.format(self.firstname, self.surname, self.type, self.status)


class Administrator(Person):
    __tablename__ = 'administrator'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    email = Column(String)
    phoneNumber = Column(String)
    nationalID = Column(String, unique=True)

    def __repr__(self):
        rstring = "<Admin name='{}' surname='{}' active='{}' email='{}' >"
        return rstring.format(self.firstname, self.surname, self.active, self.email)

    __mapper_args__ = {
        'polymorphic_identity': 'administrator',
    }


class Principal(Person):
    __tablename__ = 'administrator'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    email = Column(String)
    phoneNumber = Column(String)
    nationalID = Column(String, unique=True)

    def __repr__(self):
        rstring = "<Principal name='{}' surname='{}' active='{}' >"
        return rstring.format(self.firstname, self.surname, self.active)

    __mapper_args__ = {
        'polymorphic_identity': 'principal',
    }


class Parent(Person):
    __tablename__ = 'administrator'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    email = Column(String)
    phoneNumber = Column(String)
    nationalID = Column(String, unique=True)
    child_id = Column(Integer, ForeignKey('student.id'))

    def __repr__(self):
        rstring = "<Parent name='{}' surname='{}' email='{}' >"
        return rstring.format(self.firstname, self.surname, self.email)

    __mapper_args__ = {
        'polymorphic_identity': 'parent',
    }


class Student(Person):
    __tablename__ = 'student'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    studentID = Column(String, unique=True)
    bcNumber = Column(String)
    # TODO: <class reference -> Class here
    parents = relationship('Parent',
                           backref=backref('child_of', lazy='dynamic'))

    def __repr__(self):
        rstring = "<Student name='{}' surname='{}' email='{}' >"
        return rstring.format(self.firstname, self.surname, self.email)

    __mapper_args__ = {
        'polymorphic_identity': 'student',
    }


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)  # TODO: why is the id a string instead of int?
    accountID = Column(String, unique=True)
    # TODO: Complete Account and the rest after qualifications


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
