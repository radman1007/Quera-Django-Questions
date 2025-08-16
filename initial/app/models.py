from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class RoleType(models.IntegerChoices):
    MEMBER = 0, "member"
    OWNER = 1, "owner"


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children", null=True, blank=True)


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="projects", null=True)
    members = models.ManyToManyField(User, through="Membership")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        ordering = ("updated_at",)
    


class Membership(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, models.CASCADE)
    role = models.IntegerField(choices=RoleType.choices, default=RoleType.MEMBER)
    
    
    class Meta:
        unique_together = ("person", "project")
