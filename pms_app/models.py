from django.db import models


# ================= STUDENT MODEL =================
class Student(models.Model):
    COURSE_CHOICES = [
        ('BTECH', 'B.Tech'),
        ('MBA', 'MBA'),
        ('MCA', 'MCA'),
        ('BSC', 'B.Sc'),
        ('MSC', 'M.Sc'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    branch = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15, blank=True, null=True)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES, blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# ================= COMPANY MODEL =================
class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# ================= JOB MODEL =================
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    role = models.CharField(max_length=100)
    package = models.IntegerField(help_text="Package in LPA")

    eligibility = models.CharField(max_length=200,blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    job_mode = models.CharField(max_length=50,blank=True, null=True)

    def __str__(self):
        return f"{self.company.name} - {self.role}"
     
# ================= APPLICATION MODEL =================
class Application(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="Applied")

    def __str__(self):
        return f"{self.student.name} - {self.job.role}"