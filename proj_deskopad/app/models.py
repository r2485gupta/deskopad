from django.db import models
from django.contrib.auth.models import User

class location(models.Model):
	location_name = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)

class user_type(models.Model):
	type_name = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = model.DateTimeField(auto_now_add=True)

class user_details(models.Model):
	location = models.ForeignKey(location)
	user_type = models.ForeignKey(user_type)
	contact_number = models.IntegerField()
	verified = models.IntegerField(default=0)
	deleted = models.IntegerField(default=0)
	company_name = models.CharField(max_length=255)
	professional_headline = models.CharField(max_length=255)
	position = models.CharField(max_length=255)
	short_bio = models.CharField(max_length=1000)
	twitter_handle = models.CharField(max_length=255)
	facebook_url = models.CharField(max_length=255)
	linkedin_url = models.CharField(max_length=255)
	googleplus_url = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = model.DateTimeField(auto_now_add=True)

class space_category(models.Model):
	category_name = models.CharField(max_length=255)
	category_description = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)
	updated = model.DateTimeField(auto_now_add=True)

class space(models.Model):
	space_name = models.CharField(max_length=255)
	space_location = models.ForeignKey(location)
	landmark = models.CharField(max_length=255)
	owner = models.ForeignKey(User)
	space_description = models.CharField(max_length=1000)
	price_per_day = models.IntegerField()
	price_per_month = models.IntegerField()
	negotiable = models.IntegerField()
	category = models.ForeignKey(space_category)
	verified = models.IntegerField(default=0)
	deleted = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)
	updated = model.DateTimeField(auto_now_add=True)

class reviews(models.Model):
	space_id = models.ForeignKey(space)
	reviewer_id = models.ForeignKey(User)
	rating = models.IntegerField()
	verified = models.IntegerField(default=0)
	detailed_review = models.CharField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)
	updated = model.DateTimeField(auto_now_add=True)

class amenities(models.Model):
	space_id = models.ForeignKey(space)
	amenity_name = models.CharField(max_length=255)
	available = models.IntegerField()

class favourites(models.Model):
	space_id = models.ForeignKey(space)
	user_id = models.ForeignKey(User)

