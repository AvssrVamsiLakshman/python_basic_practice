"""
Task Objective:
Create a dictionary named shot_tracker containing nested dictionaries for individual shots.
Store shot-specific details like artist, status, and frame_range.
Modify the nested dictionary for an existing shot by updating values.
Add a new shot to the tracker with the same structure.
Print the updated dictionary.
Safely access a key that doesn't exist using the get() method.

📝 Instructions:
• Define a dictionary named shot_tracker with three shots: shot_001, shot_002, and shot_003.
  - Each should include the keys: artist, status, and frame_range.
• Update the artist and status for shot_003.
• Add a new shot named shot_004 with the same key structure.
• Print the entire shot_tracker dictionary.
• Use the get() method to access the artist of a non-existent shot (shot_005) and return "Unassigned" if it's missing.

💡 Sample Output:

Updated shot_003: {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)}  
Added shot_004: {'artist': 'Diana', 'status': 'Not Started', 'frame_range': (401, 500)}  

Full Shot Tracker:  
{'shot_001': {'artist': 'Alice', 'status': 'In Progress', 'frame_range': (100, 200)},  
 'shot_002': {'artist': 'Bob', 'status': 'Not Started', 'frame_range': (201, 300)},  
 'shot_003': {'artist': 'Charlie', 'status': 'In Progress', 'frame_range': (301, 400)},  
 'shot_004': {'artist': 'Diana', 'status': 'Not Started', 'frame_range': (401, 500)}}  

Artist for shot_005: Unassigned
"""

print("=" * 80)
print("VFX SHOT TRACKER SYSTEM")
print("=" * 80)

# Step 1: Define shot_tracker dictionary with three shots
print("\nSTEP 1: Creating Shot Tracker with Initial Shots")
print("-" * 80)

shot_tracker = {
    "shot_001": {
        "artist": "Alice",
        "status": "In Progress",
        "frame_range": (100, 200)
    },
    "shot_002": {
        "artist": "Bob",
        "status": "Not Started",
        "frame_range": (201, 300)
    },
    "shot_003": {
        "artist": "Eve",  # Will be updated to Charlie
        "status": "Not Started",  # Will be updated to In Progress
        "frame_range": (301, 400)
    }
}

print("Initial Shot Tracker:")
for shot_id, details in shot_tracker.items():
    print(f"  {shot_id}: {details}")


# Step 2: Update the artist and status for shot_003
print("\n" + "=" * 80)
print("STEP 2: Updating shot_003")
print("-" * 80)

shot_tracker["shot_003"]["artist"] = "Charlie"
shot_tracker["shot_003"]["status"] = "In Progress"

print(f"Updated shot_003: {shot_tracker['shot_003']}")


# Step 3: Add a new shot named shot_004
print("\n" + "=" * 80)
print("STEP 3: Adding shot_004")
print("-" * 80)

shot_tracker["shot_004"] = {
    "artist": "Diana",
    "status": "Not Started",
    "frame_range": (401, 500)
}

print(f"Added shot_004: {shot_tracker['shot_004']}")


# Step 4: Print the entire shot_tracker dictionary
print("\n" + "=" * 80)
print("STEP 4: Full Shot Tracker")
print("-" * 80)

print("\nFull Shot Tracker:")
for shot_id, details in shot_tracker.items():
    print(f"{shot_id}: {details}")


# Step 5: Use get() method to safely access non-existent shot
print("\n" + "=" * 80)
print("STEP 5: Safe Access Using .get() Method")
print("-" * 80)

# Accessing a non-existent shot (shot_005)
artist_shot_005 = shot_tracker.get("shot_005", {"artist": "Unassigned"})["artist"]
print(f"\nArtist for shot_005: {artist_shot_005}")


# Additional demonstrations
print("\n" + "=" * 80)
print("BONUS: Additional Operations")
print("-" * 80)

# Count shots by status
print("\nShot Count by Status:")
status_count = {}
for shot_id, details in shot_tracker.items():
    status = details["status"]
    status_count[status] = status_count.get(status, 0) + 1

for status, count in status_count.items():
    print(f"  {status}: {count} shot(s)")

# List all artists
print("\nAll Artists:")
artists = [details["artist"] for shot_id, details in shot_tracker.items()]
print(f"  {', '.join(artists)}")

# Find shots by artist
print("\nShots assigned to Charlie:")
charlie_shots = [shot_id for shot_id, details in shot_tracker.items() 
                 if details["artist"] == "Charlie"]
print(f"  {', '.join(charlie_shots)}")


print("\n" + "=" * 80)
print("PROGRAM COMPLETED SUCCESSFULLY")
print("=" * 80)
