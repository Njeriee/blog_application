from django.db import models

class Authors(models.Model):
    first_name = models.CharField(max_length= 30, null=False)
    middle_name = models.CharField(max_length= 30)
    sur_name = models.CharField(max_length= 30)

class Articles(models.Model):
    article_id = models.AutoField(primary_key= True)
    author = models.ForeignKey(Authors, on_delete= models.CASCADE, null=False)
    title = models.CharField(max_length= 100)
    body = models.TextField

    def __str__(self):
        return self.title , self.author