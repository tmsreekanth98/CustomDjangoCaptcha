# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Info(models.Model):
	name = models.CharField(max_length=100)
	roll_no = models.CharField(max_length=100)

	def __str__(inf):
		return str(inf.name) + "-" + str(inf.roll_no)