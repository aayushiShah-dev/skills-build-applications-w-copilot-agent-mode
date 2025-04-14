import os
import django

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_tracker.models import User

def test_djongo_query():
    try:
        # Test creating a user
        user = User.objects.create(username='testuser', email='testuser@example.com', password='password')
        print(f"User created: {user}")

        # Test retrieving the user
        retrieved_user = User.objects.get(email='testuser@example.com')
        print(f"User retrieved: {retrieved_user}")

        # Test deleting the user
        retrieved_user.delete()
        print("User deleted successfully.")
    except Exception as e:
        print(f"Error during Djongo query test: {e}")

if __name__ == "__main__":
    test_djongo_query()