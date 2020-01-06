from django.db import models

# Create your models here.
class NewCategory(models.Model):
    title = models.CharField(max_length=100)
    taglist = models.TextField()

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'newcategory'


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news/')
    taglist = models.TextField()
    date = models.DateField()
    newscateogry = models.ForeignKey(NewCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.title