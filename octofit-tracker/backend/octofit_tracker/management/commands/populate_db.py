from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from djongo import models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data by dropping collections using PyMongo
        from pymongo import MongoClient
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.workouts.drop()
        db.leaderboard.drop()

        # Create teams
        marvel = Team(name='Marvel')
        marvel.save()
        dc = Team(name='DC')
        dc.save()

        # Create users
        spiderman = User(name='Spider-Man', email='spiderman@marvel.com', team=marvel)
        spiderman.save()
        ironman = User(name='Iron Man', email='ironman@marvel.com', team=marvel)
        ironman.save()
        wonderwoman = User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)
        wonderwoman.save()
        batman = User(name='Batman', email='batman@dc.com', team=dc)
        batman.save()

        # Create workouts
        cardio = Workout(name='Cardio Blast', description='High intensity cardio workout', difficulty='Medium')
        cardio.save()
        strength = Workout(name='Strength Training', description='Full body strength workout', difficulty='Hard')
        strength.save()

        # Create activities
        Activity(user=spiderman, type='Running', duration=30, calories=300).save()
        Activity(user=ironman, type='Cycling', duration=45, calories=400).save()
        Activity(user=wonderwoman, type='Swimming', duration=60, calories=500).save()
        Activity(user=batman, type='Yoga', duration=40, calories=200).save()

        # Create leaderboard
        Leaderboard(team=marvel, points=700).save()
        Leaderboard(team=dc, points=600).save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
