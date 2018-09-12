from django.db import models


class Schedule(models.Model):
    ''' a model for a schedule that will be related to the user object
    This will make it possible to save data across group chats. '''

    title = models.CharField(max_length=400)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class SimpleUser(models.Model):
    ''' A model for a group me user so we can save data
    across group chats etc. We will avoid using the default
    django user model since the password/email authentication
    features are not helpful for us.
    '''
    username = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
