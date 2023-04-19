from django.db import models

# Create your models here.

class questions(models.Model):
    question = models.CharField(max_length=2000,help_text="enter the question")
    op1 = models.CharField(max_length=100 , null=True)
    op2 = models.CharField(max_length=100,null=True)
    op3 = models.CharField(max_length=100,null=True)
    op4 = models.CharField(max_length=100,null=True)
    ans = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.question
    

