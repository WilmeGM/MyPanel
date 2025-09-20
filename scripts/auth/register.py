def runAction(self, event):
    # Retrieve user input from sibling components
    username = self.getSibling("UsernameTextField").props.text
    email = self.getSibling("EmailTextField").props.text
    password = self.getSibling("PasswordField").props.text
    bio = self.getSibling("BioTextArea").props.text
    
    # Reference to the error label component
    error_label = self.getSibling("ErrorLabel")
    
    # Validate required fields
    if not username or not email or not password:
        error_label.props.text = "Required fields are missing"
        return
    
    # Validate email format
    if not isValidEmail(email):
        error_label.props.text = "Invalid email format"
        return
        
    # Clear any previous error messages
    error_label.props.text = ""
    
    # Check if the username already exists in the database
    existing_user = system.db.runPrepQuery(
        "SELECT COUNT(1) FROM Users WHERE username = ?", 
        [username], 
        "MyPanelDB"
    )[0][0]
    if existing_user and existing_user > 0:
        error_label.props.text = "Username already exists"
        return
    
    # Check if the email is already registered
    existing_email = system.db.runPrepQuery(
        "SELECT COUNT(1) FROM Users WHERE email = ?", 
        [email], 
        "MyPanelDB"
    )[0][0]
    if existing_email and existing_email > 0:
        error_label.props.text = "Email already registered"
        return
    
    # Encrypt the password using SHA-256
    pssword_haashed = encryptPassword(password)
    
    # SQL query to insert the new user into the database
    query = """ 
    INSERT INTO Users (username, email, password, bio)
    VALUES (?, ?, ?, ?)
    """
    
    try:
        # Execute the insert query
        system.db.runPrepUpdate(query, [username, email, pssword_haashed, bio], "MyPanelDB")
        
        # Show success message in green
        self.getSibling("ErrorLabel").props.style["color"] = "green"
        self.getSibling("ErrorLabel").props.text = "User registered successfully!"
        
        # Clear input fields after successful registration
        self.getSibling("UsernameTextField").props.text = ""
        self.getSibling("EmailTextField").props.text = ""
        self.getSibling("PasswordField").props.text = ""
        self.getSibling("BioTextArea").props.text = ""
    except Exception as e:
        self.getSibling("ErrorLabel").props.text = "An error occurred registering the user..." + str(e)

def encryptPassword(password):
    # Encrypt password using SHA-256 hashing
    from java.security import MessageDigest
    md = MessageDigest.getInstance("SHA-256")
    md.update(password.encode("utf-8"))
    hashedBytes = md.digest()
    # Convert hashed bytes to hexadecimal string
    return "".join(["%02x" % b for b in hashedBytes])

def isValidEmail(email):
    # Basic email format validation
    email = email.strip()
    
    if email.count("@") != 1:
        return False
    
    if " " in email:
        return False
    
    return True
