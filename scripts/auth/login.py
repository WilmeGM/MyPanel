def runAction(self, event):
    # Get user input from sibling components
    username = self.getSibling("UsernameTextField").props.text
    password = self.getSibling("PasswordField").props.text
    
    # Reference to the error message label
    error_label = self.getSibling("ErrorLabel")
    
    # Validate that both fields are filled
    if not username or not password:
        error_label.props.text = "Username and password are required"
        return
    
    # Encrypt the entered password using SHA-256
    hashed_input = encryptPassword(password)
    
    # Query the database for the stored password of the entered username
    query = "SELECT password FROM Users WHERE username = ?"
    result = system.db.runPrepQuery(query, [username], "MyPanelDB")
    
    # If no user is found, show error
    if not result or len(result) == 0:
        error_label.props.text = "Username or password are incorrect"
        return
    
    # Extract stored password from query result
    stored_password = result[0][0]
    
    # Compare encrypted input with stored password
    if hashed_input == stored_password:
        # Store user info in session custom properties
        self.session.custom.username = username
        self.session.custom.email = system.db.runPrepQuery("SELECT email FROM Users WHERE username = ?", [username], "MyPanelDB")[0][0]
        self.session.custom.user_id = system.db.runPrepQuery("SELECT id FROM Users WHERE username = ?", [username], "MyPanelDB")[0][0]
        
        system.perspective.closePopup("LksxbhPL")
    else: 
        error_label.props.text = "Username or password are incorrect"

def encryptPassword(password):
    # Encrypt password using SHA-256 hashing
    from java.security import MessageDigest
    md = MessageDigest.getInstance("SHA-256")
    md.update(password.encode("utf-8"))
    hashedBytes = md.digest()
    # Convert hashed bytes to hexadecimal string
    return "".join(["%02x" % b for b in 
