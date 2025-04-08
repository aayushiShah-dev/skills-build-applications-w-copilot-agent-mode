from django.core.management.base import BaseCommand

from octofit_tracker.test_data import get_test_data
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):

        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Get test data
        test_data = get_test_data()

        # Insert test data into collections
        db.users.insert_many(test_data['users'])
        db.teams.insert_many(test_data['teams'])
        db.activities.insert_many(test_data['activities'])
        db.leaderboard.insert_many(test_data['leaderboard'])
        db.workouts.insert_many(test_data['workouts'])


        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
