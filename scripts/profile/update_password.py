def runAction(self, event):
    # Get current and new password input from sibling components
    current_password = self.getSibling("CurrentPasswordField").props.text
    new_password = self.getSibling("NewPasswordField").props.text
    
    # Reference to the error label component
    error_label = self.getSibling("ErrorLabel")
    
    # Validate that both fields are filled
    if not current_password or not new_password:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Both fields are required"
        return
    
    # Retrieve the stored password hash from the database using the session email
    stored_password = system.db.runPrepQuery(
        "SELECT password FROM Users WHERE email = ?", 
        [self.session.custom.email], 
        "MyPanelDB"
    )[0][0]
    
    # Compare the encrypted current password with the stored hash
    if encryptPassword(current_password) != stored_password:
        error_label.props.style["color"] = "red"
        error_label.props.text = "Current password is incorrect"
        return
    
    try:
        # Encrypt the new password
        new_password_hashed = encryptPassword(new_password)
        
        # Update the password in the database
        system.db.runPrepUpdate(
            "UPDATE Users SET password = ? WHERE email = ?", 
            [new_password_hashed, self.session.custom.email], 
            "MyPanelDB"
        )
        
        # Show success message and clear input fields
        error_label.props.style["color"] = "green"
        error_label.props.text = "Password updated successfully!"
        self.getSibling("CurrentPasswordField").props.text = ""
        self.getSibling("NewPasswordField").props.text = ""
    except Exception as e:
        # Show error message if update fails
        error_label.props.style["color"] = "red"
        error_label.props.text = "Error updating password "

def encryptPassword(password):
    # Encrypt password using SHA-256 hashing
    from java.security import MessageDigest
    md = MessageDigest.getInstance("SHA-256")
    md.update(password.encode("utf-8"))
    hashedBytes = md.digest()
    # Convert hashed bytes to hexadecimal string
    return "".join(["%02x" % b for b in hashedBytes])
