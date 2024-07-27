
# YouTube Manager App with Database

This script is a simple YouTube video management application that uses SQLite for storing and managing video data. It allows users to list, add, update, and delete videos from a SQLite database.

## Modules Used

- `sqlite3`: This module is used to interact with SQLite databases in Python. It provides an SQL interface compliant with the DB-API 2.0 specification.

## Functionality

### 1. Creating the Database and Table

```python
import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
              id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL         
    )
''')
```

- `sqlite3.connect("youtube_videos.db")`: Establishes a connection to the SQLite database named `youtube_videos.db`. If the database does not exist, it will be created.
- `cursor.execute(...)`: Executes an SQL statement to create a table named `videos` if it does not already exist. The table has three columns: `id` (primary key), `name`, and `time`.

### 2. Listing Videos

```python
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
```

- `cursor.execute("SELECT * FROM videos")`: Executes an SQL query to select all records from the `videos` table.
- `cursor.fetchall()`: Fetches all rows of a query result and returns a list of tuples. Each tuple represents a row in the table.
- `print(row)`: Prints each row to the console.

### 3. Adding a Video

```python
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
```

- `cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))`: Executes an SQL statement to insert a new record into the `videos` table with the specified `name` and `time`.
- `conn.commit()`: Commits the current transaction, saving the changes to the database.

### 4. Updating a Video

```python
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
```

- `cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))`: Executes an SQL statement to update the `name` and `time` of the video with the specified `video_id`.
- `conn.commit()`: Commits the current transaction, saving the changes to the database.

### 5. Deleting a Video

```python
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
```

- `cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))`: Executes an SQL statement to delete the video with the specified `video_id`.
- `conn.commit()`: Commits the current transaction, saving the changes to the database.

### 6. Main Function

```python
def main():
    while True:
        print("\n YouTube Manager app with DB | Choose an option")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video details")
        print("4. Delete video")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice")

    conn.close()
```

- This function provides a simple command-line interface for the user to interact with the database.
- Depending on the user's choice, it calls the appropriate function to list, add, update, or delete videos.
- The loop continues until the user chooses to exit the application.

### 7. Entry Point

```python
if __name__ == "__main__":
    main()
```

- This ensures that the `main()` function is called only when the script is run directly, not when it is imported as a module.
