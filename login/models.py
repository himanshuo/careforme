from django.db import models




class User(models.Model):
    name = models.CharField(max_length=100, null=True)

    fb_id = models.CharField(max_length=100,null=True)
    fb_token = models.CharField(max_length=300, null=True)



    def __str__(self):
        return self.name+":"+self.fb_id

class Friend(models.Model):
    fb_id=models.CharField(max_length=100,null=True)
    friend_fb_id=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.fb_id+":"+self.friend_fb_id



class Compliment(models.Model):
    compliment = models.TextField()

    compliment_by = models.CharField(max_length=100,null=True)#based on fb_id
    compliment_for = models.CharField(max_length=100,null=True)#based on fb_id

    unlocked = models.BooleanField(default=False)
    def __str__(self):
        return self.compliment+":for "+self.compliment_for+" by "+self.compliment_by









#a = User()


#a.toString()      ======      str(a)