from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com", password="password123")

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")

class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Team A")

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Team A")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="activityuser", email="activity@example.com", password="password123")
        self.activity = Activity.objects.create(user=self.user, activity_type="Running", duration="01:00:00")

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.duration, "01:00:00")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="leaderboarduser", email="leaderboard@example.com", password="password123")
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(name="Workout A", description="Test workout")

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Workout A")
        self.assertEqual(self.workout.description, "Test workout")
