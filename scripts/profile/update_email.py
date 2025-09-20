def runAction(self, event):
    # Get the new email from the input field
    new_email = self.getSibling("EmailTextField").props.text
    
    # Reference to the error label component
    error_label = self.getSibling("ErrorLabel")
    
    # Validate that the email field is not empty
    if not new_email:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Email cannot be empty"
        return
    
    # Check if the new email is the same as the current one
    same_user = system.db.runPrepQuery(
        "SELECT COUNT(1) FROM Users WHERE email = ? AND username = ?", 
        [new_email, self.session.custom.username], 
        "MyPanelDB"
    )[0][0]
    
    if same_user > 0:
        error_label.props.style["color"] = "red"
        error_label.props.text = "It is the same, right?"
        return
    
    # Check if the email is already used by another user
    existing_user = system.db.runPrepQuery(
        "SELECT COUNT(1) FROM Users WHERE email = ?", 
        [new_email], 
        "MyPanelDB"
    )[0][0]
    
    if existing_user > 0:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Email already taken"
        return
    
    # Validate email format
    if not isValidEmail(new_email):
        error_label.props.style["color"] = "red"
        error_label.props.text = "Invalid email format"
        return
    
    try:
        # Update the email in the database
        system.db.runPrepUpdate(
            "UPDATE Users SET email = ? WHERE username = ?", 
            [new_email, self.session.custom.username], 
            "MyPanelDB"
        )
        
        # Update the session with the new email
        self.session.custom.email = new_email
        
        # Show success message
        error_label.props.style["color"] = "green"
        error_label.props.text = "Email updated successfully!"
    except Exception as e:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Error updating email"

def isValidEmail(email):
    # Basic email format validation
    email = email.strip()
    
    if email.count("@") != 1:
        return False
    
    if " " in email:
        return False
    
    return True
