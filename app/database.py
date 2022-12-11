# Import the sqlite3 package
import sqlite3

class Database:
    def __init__(self, path: str) -> None:
        # Open the SQLite database file
        self.path = path
        self.con = sqlite3.connect(self.path, check_same_thread=False)
        self.con.row_factory = sqlite3.Row

    def close(self):
        if self.con is not None:
            print('Closing database connection')
            self.con.close()
        
    def unpack(self, rows):
        """Returns data from an SQL query as a list of dicts."""
        try:
            unpacked = [{k: row[k] for k in row.keys()} for row in rows]
            return unpacked
        except Exception as e:
            print(e)
            return []

    def get_todos(self):
        # Execute the query
        try:
            cursor = self.con.execute("SELECT * FROM todos")
            rows = self.unpack(cursor.fetchall())
            cursor.close()
            # Return the todos as a list of dicts
            return rows
        except Exception as e:
            print(e)

    def create_todo(self, task: str, completed: bool = False) -> dict:
        try:
            # Insert the new todo into the database
            cursor = self.con.execute("INSERT INTO todos (task, completed) VALUES (?, ?)", (task, completed))
            self.con.commit()
            # Get the id of the new todo
            id = cursor.lastrowid
            cursor.close()
            # Return the new todo as a dict
            return {
                "id": id,
                "task": task,
                "completed": False
            }
        except Exception as e:
            print(e)

    def update_todo(self, id: int, task: str, completed: bool) -> dict:
        try:
            # Update the todo in the database
            cursor = self.con.execute("UPDATE todos SET task = ?, completed = ? WHERE id = ?", (task, completed, id))
            self.con.commit()
            cursor.close()
            # Return the updated todo as a dict
            return {
                "id": id,
                "task": task,
                "completed": completed
            }
        except Exception as e:
            print(e)
    
    def delete_todo(self, id: int) -> dict:
        try:
            # Delete the todo from the database
            cursor = self.con.execute("DELETE FROM todos WHERE id = ?", (id,))
            self.con.commit()
            cursor.close()
            # Return the deleted todo as a dict
            return "Todo deleted successfully"
        except Exception as e:
            print(e)
            
