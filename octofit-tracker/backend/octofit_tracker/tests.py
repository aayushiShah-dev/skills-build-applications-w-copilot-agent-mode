from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User", age=25)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.age, 25)

class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Team A")

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Team A")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test2@example.com", name="Test User 2", age=30)
        self.activity = Activity.objects.create(user=self.user, type="Running", duration=30, date="2025-04-08")

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, "Running")
        self.assertEqual(self.activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Team B")
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name="Workout A", description="Test workout", duration=45)

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Workout A")
        self.assertEqual(self.workout.duration, 45)
