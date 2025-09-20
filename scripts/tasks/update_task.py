def runAction(self, event):
    # Get the new value from the cell edit event
    new_value = event.value
    
    # Get the task ID from the edited row
    task_id = self.props.data[event.row]["id"]
    
    # Check which column was edited
    if event.column == "is_completed":
        # Convert boolean to integer for database storage
        new_value_int = 1 if new_value else 0
        
        try:
            # Update the completion status in the database
            system.db.runPrepUpdate(
                "UPDATE Tasks SET is_completed = ? WHERE id = ?", 
                [new_value_int, task_id], 
                "MyPanelDB"
            )
            
            # Show success message and update local data
            self.getSibling("MessageLabel").props.style["color"] = "green"
            self.getSibling("MessageLabel").props.text = "Task updated nicely!"
            self.props.data[event.row][event.column] = event.value
            
        except Exception as e:
            # Show error message if update fails
            self.getSibling("MessageLabel").props.style["color"] = "red"
            self.getSibling("MessageLabel").props.text = "An error occurred updating!"
    
    elif event.column == "description":
        try:
            # Update the task description in the database
            system.db.runPrepUpdate(
                "UPDATE Tasks SET description = ? WHERE id = ?", 
                [new_value, task_id], 
                "MyPanelDB"
            )
            
            # Show success message and update local data
            self.getSibling("MessageLabel").props.style["color"] = "green"
            self.getSibling("MessageLabel").props.text = "Task updated nicely!"
            self.props.data[event.row][event.column] = event.value
            
        except Exception as e:
            # Show error message if update fails
            self.getSibling("MessageLabel").props.style["color"] = "red"
            self.getSibling("MessageLabel").props.text = "An error occurred updating!"
    
    else:
        try:
            # Update the task title in the database
            system.db.runPrepUpdate(
                "UPDATE Tasks SET title = ? WHERE id = ?", 
                [new_value, task_id], 
                "MyPanelDB"
            )
            
            # Show success message and update local data
            self.getSibling("MessageLabel").props.style["color"] = "green"
            self.getSibling("MessageLabel").props.text = "Task updated nicely!"
            self.props.data[event.row][event.column] = event.value
            
        except Exception as e:
            # Show error message if update fails
            self.getSibling("MessageLabel").props.style["color"] = "red"
            self.getSibling("MessageLabel").props.text = "An error occurred updating!"
