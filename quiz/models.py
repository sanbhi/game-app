from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=100)
    wrong_answer1 = models.CharField(max_length=100)
    wrong_answer2 = models.CharField(max_length=100)
    wrong_answer3 = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text
