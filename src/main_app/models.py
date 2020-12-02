from django.db import models
# from django.contrib.auth.models import AbstractUser


# Create your models here.
class Direction(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=50)
    abbriviation = models.CharField(max_length=10)
    direction = models.ForeignKey(Direction, related_name="courses", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profession(models.Model):
    title = models.CharField(max_length=50)
    abbriviation = models.CharField(max_length=10)
    course = models.ManyToManyField(
        Course,
        related_name="profession",
    )

    def __str__(self):
        return self.title


class WebConference(models.Model):
    title = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()
    course = models.ManyToManyField(
        Course,
        related_name="webConference",
    )

    def __str__(self):
        return self.title


class Group(models.Model):
    title = models.CharField(max_length=50)
    course = models.ManyToManyField(
        Course,
        related_name="groups",
    )
    lecture = models.ManyToManyField(WebConference, related_name="group")

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, default="")  # отчество
    email = models.EmailField()
    group = models.ManyToManyField(
        Group,
        related_name="members",
    )
    expert_lecture = models.ManyToManyField(
        WebConference,
        related_name="experts",
    )
    coordinater = models.ManyToManyField(
        Course,
        related_name="coordinaters",
    )

    def __str__(self):
        if self.middle_name:
            name = self.last_name + " " + self.first_name + " " + self.middle_name
        else:
            name = self.last_name + " " + self.first_name
        return name

#
# class Expert(models.Model):
#     webConference = models.ManyToManyField(
#         WebConference,
#         related_name='experts',
#     )
#     person = models.ManyToManyField(
#         Person,
#         related_name='expert',
#     )
#
# class Coordinater(models.Model):
#     course = models.ManyToManyField(
#         Course,
#         related_name='coordinaters',
#     )
#     person = models.ManyToManyField(
#         Person,
#         related_name='coordinater',
#     )

# from main_app.models import Coordinater, Expert, Person, Group, WebConference, Profession, Course, Direction
