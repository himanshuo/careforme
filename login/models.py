from django.db import models

"""
class User(models.Model):
    name = models.CharField(max_length=100)
    fb_id = models.CharField(max_length=100)
    def __str__(self):
        return self.name+":"+self.fb_id



class Compliments(models.Model):
    compliment = models.TextField()
    for_user_id = models.ForeignKey(User)    #Foreign Key
    written_by_id = models.ForeignKey(User)  #Foreign Key
    def __str__(self):
        return self.compliment

"""

#a = User()


#a.toString()      ======      str(a)