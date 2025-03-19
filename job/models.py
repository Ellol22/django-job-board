from django.db import models 

# Create your models here.
JOB_TYPE=(
    ("Full_time","Full_time"),
    ("Part_Time","Part_Time")
)

class Job(models.Model):
    title = models.CharField(max_length=40)
    #location
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.CharField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.FloatField(default=0)
    # category
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title