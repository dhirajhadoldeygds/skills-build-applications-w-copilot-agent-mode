from pymongo import MongoClient

def populate():
    client = MongoClient("mongodb://localhost:27017")
    db = client["octofit_db"]

    # Users
    users = [
        {"name": "Dhiraj", "email": "dhiraj@example.com"},
        {"name": "Alex", "email": "alex@example.com"},
    ]
    db.users.insert_many(users)

    # Teams
    teams = [
        {"name": "Team Alpha", "members": ["Dhiraj"]},
        {"name": "Team Beta", "members": ["Alex"]},
    ]
    db.teams.insert_many(teams)

    # Activities
    activities = [
        {"user": "Dhiraj", "activity": "Running", "duration": 30},
        {"user": "Alex", "activity": "Cycling", "duration": 45},
    ]
    db.activities.insert_many(activities)

    # Workouts
    workouts = [
        {"user": "Dhiraj", "type": "Strength", "sets": 3},
        {"user": "Alex", "type": "Cardio", "sets": 4},
    ]
    db.workouts.insert_many(workouts)

    # Leaderboard
    leaderboard = [
        {"user": "Dhiraj", "points": 150},
        {"user": "Alex", "points": 120},
    ]
    db.leaderboard.insert_many(leaderboard)

    print("Database populated with test data.")

if __name__ == "__main__":
    populate()