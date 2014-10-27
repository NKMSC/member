# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32L, blank=True)
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    memo = models.TextField(blank=True)
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'activity'
        

class Code(models.Model):
    id = models.IntegerField(primary_key=True)
    use = models.ForeignKey('User')
    code = models.CharField(max_length=16L, blank=True)
    type = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    effective = models.IntegerField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.code
    class Meta:
        db_table = 'code'

class Log(models.Model):
    id = models.IntegerField(primary_key=True)
    use = models.ForeignKey('User')
    content = models.TextField(blank=True)
    time = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.content
    class Meta:
        db_table = 'log'

class Section(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16L)
    profile = models.CharField(max_length=255L, blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'section'

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    sec = models.ForeignKey(Section)
    email = models.CharField(max_length=64L)
    password = models.CharField(max_length=32L)
    name = models.CharField(max_length=8L)
    sex = models.CharField(max_length=8L, blank=True)
    phone = models.CharField(max_length=16L, blank=True)
    school = models.CharField(max_length=16L, blank=True)
    college = models.CharField(max_length=32L, blank=True)
    major = models.CharField(max_length=32L, blank=True)
    entry_year = models.DateField(null=True, blank=True)
    grade = models.CharField(max_length=8L, blank=True)
    authority = models.BigIntegerField(null=True, blank=True)
    profile = models.CharField(max_length=255L, blank=True)
    position = models.CharField(max_length=16L, blank=True)
    open = models.BigIntegerField(null=True, blank=True)
    qq = models.CharField(max_length=16L, blank=True)
    province = models.CharField(max_length=16L, blank=True)
    city = models.CharField(max_length=16L, blank=True)
    area = models.CharField(max_length=16L, blank=True)
    effective = models.IntegerField(null=True, blank=True)
    campus = models.CharField(max_length=16L, blank=True)
    wechat = models.TextField(blank=True)
    love = models.CharField(max_length=8L, blank=True)
    dormitory = models.CharField(max_length=16L, blank=True)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'user'

class UserTakePartInActivity(models.Model):
    id = models.ForeignKey(Activity, db_column='id')
    use = models.ForeignKey(User)
    sign_in_time = models.DateTimeField(null=True, blank=True)
    def __unicode__(self):
        return self.id
    class Meta:
        db_table = 'user_take_part_in_activity'

