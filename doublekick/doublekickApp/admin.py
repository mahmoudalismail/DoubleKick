from django.contrib import admin
from doublekickApp.models import *

class Players(admin.ModelAdmin):
    fieldsets = [
             ('First Name', {'fields': ['firstName']}),
             ('Last Name', {'fields': ['lastName']}),
             ('Profile', {'fields': ['profileImg']})]
             
    list_display = ('firstName', 'lastName', 'profileImg') 
    
    list_filter = ['firstName']

class Fields(admin.ModelAdmin):
    fieldsets = [
             ('Field Name', {'fields': ['fieldName']}),
             ('Image', {'fields': ['fieldImage']}),
             ('Location', {'fields': ['location']}),]
             
    list_display = ('fieldName', 'fieldImage') 
    
    list_filter = ['fieldName']
# class Clubs(admin.ModelAdmin):
#     fieldsets = [
#              ('Club Name', {'fields': ['clubName']}),
#              ('Description', {'fields': ['description']}),
#              ('Year Initiated', {'fields': ['yearInit']}),
#              ('Upload Logo', {'fields': ['logo']})
#              ]
             
#     list_display = ('clubName', 'description', 'yearInit') 
    
#     list_filter = ['clubName']

# class ClubMembers(admin.ModelAdmin):
#     fieldsets = [
#              ('Club ID', {'fields': ['clubID']}),
#              ('Member ID', {'fields': ['memberID']}),
#              ('Rank', {'fields': ['rank']}),
#              ]
             
#     list_display = ('clubID', 'memberID', 'rank') 
    
#     # list_filter = ['clubName']
# class Budgets(admin.ModelAdmin):
#     fieldsets = [
#              ('Club ID', {'fields': ['clubID']}),
#              ('Year', {'fields': ['year']}),
#              ('Allocated Budget', {'fields': ['allocBudget']}),
#              ('Total Expenses', {'fields': ['totalExpenses']}),
#              ]
             
#     list_display = ('clubID', 'year', 'allocBudget', 'totalExpenses') 

# class Expenses1(admin.ModelAdmin):
#     fieldsets = [
#              ('Member Submitted', {'fields': ['memberSubmitted']}),
#              ('Budget ID', {'fields': ['budgetID']}),
#              ('Date', {'fields': ['date']}),
#              ('Amount', {'fields': ['amount']}),
#              ('Category of Purchase', {'fields': ['catOfPurchase']}),
#              ('Receipt', {'fields': ['receipt']}),
#              ]
             
#     list_display = ('memberSubmitted', 'budgetID', 'date', 'amount', 'catOfPurchase', "receipt")

#     list_filter = ['memberSubmitted']


admin.site.register(Player, Players)
admin.site.register(Field, Fields)
# admin.site.register(Club, Clubs)
# admin.site.register(Budget, Budgets)
# admin.site.register(ClubMember, ClubMembers)
# admin.site.register(Expenses, Expenses1)