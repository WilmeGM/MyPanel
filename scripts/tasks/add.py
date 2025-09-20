def runAction(self, event):
    # Get input values from sibling components
    title = self.getSibling("TitleTextField").props.text
    description = self.getSibling("DescTextArea").props.text
    error_label = self.getSibling("ErrorLabel")
    
    # Validate that the task title is provided
    if not title:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Task title is required"
        return
    
    # Get the current session username
    username = self.session.custom.username
    
    # Query the database to get the user ID based on the username
    result = system.db.runPrepQuery("SELECT id FROM Users WHERE username = ?", [username], "MyPanelDB")
    user_id = result[0][0]
    
    try:
        # Insert the new task into the Tasks table
        system.db.runPrepUpdate(
            "INSERT INTO Tasks (user_id, title, description) VALUES (?, ?, ?)", 
            [user_id, title, description], 
            "MyPanelDB"
        )
        
        # Show success message in green
        error_label.props.style["color"] = "green"
        error_label.props.text = "Task added successfully! Please refresh table"
        
        # Clear input fields after successful submission
        self.getSibling("TitleTextField").props.text = ""
        self.getSibling("DescTextArea").props.text = ""
    except Exception as e:
        # Show error message if task insertion fails
        error_label.props.style["color"] = "red"
        error_label.props.text = "Error adding task"
