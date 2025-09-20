def runAction(self, event):
    # Get the task ID from the label component
    task_id = self.getSibling("Label").props.text
    
    # Validate that a task ID is provided
    if not task_id:
        self.getSibling("MessageLabel").props.style["color"] = "red"
        self.getSibling("MessageLabel").props.text = "Please select one row before deleting"
        return
    
    try:
        # Prepare and execute the DELETE query
        query = "DELETE FROM Tasks WHERE id = ?"
        system.db.runPrepUpdate(query, [task_id], "MyPanelDB")
        
        # Clear the label and show success message
        self.getSibling("Label").props.text = ""
        self.getSibling("MessageLabel").props.style["color"] = "green"
        self.getSibling("MessageLabel").props.text = "Task deleted nicely! Please refresh table"
    except Exception as e:
        self.getSibling("MessageLabel").props.style["color"] = "red"
		    self.getSibling("MessageLabel").props.text = "Error deleting task"
