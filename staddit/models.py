# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Comment(models.Model):
    id = models.TextField(primary_key=True)
    body = models.TextField(blank=True, null=True)
    created_utc = models.TextField(blank=True, null=True)
    gilded = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)
    controversiality = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class PostedBy(models.Model):
    author = models.TextField(blank=True, null=True)
    id = models.ForeignKey(Comment, models.DO_NOTHING, db_column='id', primary_key=True)

    class Meta:
        managed = False
        db_table = 'posted_by'


class PostedIn(models.Model):
    id = models.ForeignKey(Comment, models.DO_NOTHING, db_column='id', primary_key=True)
    subreddit = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posted_in'


class Redditor(models.Model):
    author = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'redditor'


class Subreddit(models.Model):
    subreddit = models.TextField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'subreddit'
