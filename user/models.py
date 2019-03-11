from django.db import models
 
class Questions(models.Model):
    text = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    from_id = models.IntegerField()
    to_id = models.IntegerField()

class Followers(models.Model):
    from_id = models.IntegerField()
    to_id = models.IntegerField()

class Likes(models.Model):
    question_id = models.IntegerField()
    user_id = models.IntegerField()
