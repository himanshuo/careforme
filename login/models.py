from django.db import models




class User(models.Model):
    name = models.CharField(max_length=100)
    fb_id = models.CharField(max_length=100)

    def __str__(self):
        return self.name+":"+self.fb_id




class Compliment(models.Model):
    compliment = models.TextField()
    compliment_by = models.ForeignKey(User, null=True, related_name='compliment_by')
    compliment_for = models.ForeignKey(User, null=True, related_name='compliment_for')
    def __str__(self):
        return self.compliment+":for "+self.compliment_for+" by "+self.compliment_by









#a = User()


#a.toString()      ======      str(a)