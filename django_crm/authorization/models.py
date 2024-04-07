from django.contrib.auth.models import User, Group, Permission
from django.db import models


# def profile_avatar_directory_path(instance: "Profile" ,filename: str) -> str:
#     return f"profile/profile_{instance.pk}/avatar/{filename}"

# class Role(models.Model):
#     class Meta:
#         verbose_name = "Role"
#         verbose_name_plural = "Roles"
#
#     name = models.TextField(max_length=50, blank=False)
#     description = models.TextField(max_length=300, blank=True)
#     group_permissions = models.ManyToManyField(Group, related_name="roles")
#
#
# class UserRole(models.Model):
#     class Meta:
#         verbose_name = "User-Role"
#         verbose_name_plural = "Users-Roles"
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.ManyToManyField(Group, related_name="userrole")


# new_groups = Group(name = models.CharField(_("name"), max_length=150, unique=True)
#     permissions = models.ManyToManyField()








# class Operator(models.Model):
#     class Meta:
#         verbose_name = "Operator"
#         verbose_name_plural = "Operators"
#
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     role = models.TextField(max_length=50, blank=False)
#     group_permissions = models.ManyToManyField(Group, related_name="operators")
#
#
# class MarketingSpecialist(models.Model):
#     class Meta:
#         verbose_name = "Marketing Specialist"
#         verbose_name_plural = "Marketing Specialists"
#
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     role = models.TextField(max_length=50, blank=False)
#     group_permissions = models.ManyToManyField(Group, related_name="marketingspecialists")
#
#
# class SalesManager(models.Model):
#     class Meta:
#         verbose_name = "Sales Manager"
#         verbose_name_plural = "Sales Managers"
#
#     user = models.ForeignKey(User, on_delete=models.PROTECT)
#     role = models.TextField(max_length=50, blank=False)
#     group_permissions = models.ManyToManyField(Group, related_name="salesmanagers")
