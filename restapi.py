from models import Student, Guardian, Teacher, Administrator, Account
from models import Subject, Class, CurriculumLevel, Homework, Note, HomeworkSubmissions
from models import Notification, ViewedNotifications, Timetable, Event, PhotoGallery, Photo, Message
from models import session as db_session
import flask_restless


def add_api_endpoints(appname):
    manager = flask_restless.APIManager(appname, session=db_session)

    """
    This code hasn't yet undergone rigorous testing yet and needs a whole bunch of tests done on it to ensure maximum
    workiness.
    TODO:
    => Write up a coherent and consistent documentation for current version
    => Create Unit tests to check for broken/missing endpoints
    => Populate the Database with Mock Data
    => and for me to take a nap lol
    """
    # User API functions

    student_blueprint = manager.create_api(Student,
                                           methods=['GET', 'POST', 'PUT', 'DELETE'],
                                           collection_name='students')

    guardian_blueprint = manager.create_api(Guardian,
                                            methods=['GET', 'POST', 'PUT', 'DELETE'],
                                            collection_name='guardians')

    teacher_blueprint = manager.create_api(Teacher,
                                           methods=['GET', 'POST', 'PUT', 'DELETE'],
                                           collection_name='teachers')

    administrator_blueprint = manager.create_api(Administrator,
                                                 methods=['GET', 'POST', 'PUT', 'DELETE'],
                                                 collection_name='administrators')

    account_blueprint = manager.create_api(Account,
                                           methods=['GET', 'POST', 'PUT', 'DELETE'],
                                           collection_name='accounts')

    # Academic API functions

    subject_blueprint = manager.create_api(Subject,
                                           methods=['GET', 'POST', 'PUT', 'DELETE'],
                                           collection_name='subjects')

    class_blueprint = manager.create_api(Class,
                                         methods=['GET', 'POST', 'PUT', 'DELETE'],
                                         collection_name='classes')

    curriculum_blueprint = manager.create_api(CurriculumLevel,
                                              methods=['GET', 'POST', 'PUT', 'DELETE'],
                                              collection_name='curriculum')

    homework_blueprint = manager.create_api(Homework,
                                            methods=['GET', 'POST', 'PUT', 'DELETE'],
                                            collection_name='homework')

    note_blueprint = manager.create_api(Note,
                                        methods=['GET', 'POST', 'PUT', 'DELETE'],
                                        collection_name='notes')

    submissions_blueprint = manager.create_api(HomeworkSubmissions,
                                               methods=['GET', 'POST', 'PUT', 'DELETE'],
                                               collection_name='submissions')

    # Event API functions

    notifications_blueprint = manager.create_api(Notification,
                                                 methods=['GET', 'POST', 'PUT', 'DELETE'],
                                                 collection_name='notifications')

    viewed_notifications = manager.create_api(ViewedNotifications,
                                              methods=['GET', 'POST', 'PUT', 'DELETE'],
                                              collection_name='viewed_notifications')

    timetable_blueprint = manager.create_api(Timetable,
                                             methods=['GET', 'POST', 'PUT', 'DELETE'],
                                             collection_name='timetables')

    event_blueprint = manager.create_api(Event,
                                         methods=['GET', 'POST', 'PUT', 'DELETE'],
                                         collection_name='events')

    gallery_blueprint = manager.create_api(PhotoGallery,
                                           methods=['GET', 'POST', 'PUT', 'DELETE'],
                                           collection_name='gallery')

    photo_blueprint = manager.create_api(Photo,
                                         methods=['GET', 'POST', 'PUT', 'DELETE'],
                                         collection_name='photos')

    messages_blueprint = manager.create_api(Message,
                                            methods=['GET', 'POST', 'PUT', 'DELETE'],
                                            collection_name='messages')
