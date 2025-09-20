def runAction(self, event):
    # Get the current user's ID from the session
    user_id = self.session.custom.user_id
    
    # SQL query to retrieve all tasks for the user, ordered by newest first
    query = """
        SELECT id, title, description, is_completed, created_at
        FROM Tasks
        WHERE user_id = ?
        ORDER BY id DESC
    """
    
    # Execute the query
    tasks = system.db.runPrepQuery(query, [user_id], "MyPanelDB")
    
    # Format the result into a list of dictionaries for the table component
    data = []
    for row in tasks:
        data.append({
            "id": row["id"],
            "title": row["title"],
            "description": row["description"],
            "is_completed": bool(row["is_completed"]),  # Convert to boolean
            "created_at": row["created_at"]
        })
  
    # Bind the formatted data to the TasksTable component
    self.getSibling("TasksTable").props.data = data
    
    # Clear any previous messages or selected task ID
    self.getSibling("MessageLabel").props.text = ""
    self.getSibling("Label").props.text = ""
