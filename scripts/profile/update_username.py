def runAction(self, event):
    # Get the new username from the input field
    new_username = self.getSibling("UsernameTextField").props.text
    
    # Reference to the error label component
    error_label = self.getSibling("ErrorLabel")
    
    # Validate that the username is not empty
    if not new_username:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Username cannot be empty"
        return
        
    # Check if the new username is the same as the current one (based on email)
    same_user = system.db.runPrepQuery(
        "SELECT COUNT(1) FROM Users WHERE username = ? AND email = ?", 
        [new_username, self.session.custom.email], 
        "MyPanelDB"
    )[0][0]
    
    if same_user > 0:
        error_label.props.style["color"] = "red"
        error_label.props.text = "It is the same, right?"
        return
    
    # Check if the new username is already taken by another user
    existing_user = system.db.runPrepQuery(
        "SELECT COUNT(1) FROM Users WHERE username = ?", 
        [new_username], 
        "MyPanelDB"
    )[0][0]
    
    if existing_user > 0:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Username already taken"
        return
    
    try:
        # Update the username in the database using the user's email as reference
        system.db.runPrepUpdate(
            "UPDATE Users SET username = ? WHERE email = ?", 
            [new_username, self.session.custom.email], 
            "MyPanelDB"
        )
        
        # Update the session with the new username
        self.session.custom.username = new_username
        
        # Show success message
        error_label.props.style["color"] = "green"
        error_label.props.text = "Username updated successfully!"
    except Exception as e:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Error updating username"
