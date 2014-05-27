# # importing models
# from django.db import models
# # importing the User model
# from django.contrib.auth.models import User

# # the player table
# class Player(models.Model):
# 	# player info
# 	playerInfo = models.ForeignKey(User) # this will include username & password
# 	# player name
# 	firstName = models.CharField(max_length=1000)
# 	lastName = models.CharField(max_length=1000)
# 	# date of birth 
# 	dateofbirth = models.CharField(max_length=1000)
# 	# profile picture
# 	profileImg = models.ImageField(upload_to="players", blank=True)
# 	# email 
# 	email = models.CharField(max_length=1000)
# 	# mobile number
# 	mobileN = models.IntegerField(max_length=1000)
# 	# number of matches played
# 	nMatchesPlayed = models.IntegerField(max_length=200)
# 	# height
# 	height = models.IntegerField(max_length=200)
# 	# weight of the player
# 	weight = models.IntegerField(max_length=200)
# 	# position
# 	position = models.CharField(max_length=200)
# 	# matches played
# 	matchesPlayed = models.IntegerField(max_length=200)
# 	# tournaments played
# 	tournPlayed = models.IntegerField(max_length=200)
# 	# goals scored 
# 	goals = models.IntegerField(max_length=200)
# 	# rating
# 	speed = models.IntegerField(max_length=200)
# 	shooting = models.IntegerField(max_length=200)
# 	teamWork = models.IntegerField(max_length=200)
# 	passing = models.IntegerField(max_length=200)

# 	def __unicode__(self):
# 		return self.playerInfo.username

# class Field(models.Model):
# 	# field name
# 	fieldName = models.CharField(max_length=200)
# 	# field image 
# 	fieldImage = models.ImageField(upload_to="fields")
# 	# avaliablity 
# 	avaliableTime = models.CharField(max_length=1000)
# 	#location
# 	location = models.CharField(max_length=1000)


# class Game(models.Model):
# 	# teams
# 	teams = models.CharField(max_length=2000)
# 	# fields
# 	field = models.ForeignKey(Field)
# 	#time/date
# 	timeDate = models.CharField(max_length=200)






# 		