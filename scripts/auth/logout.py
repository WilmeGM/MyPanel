def runAction(self, event):
    # Clear user session data
    self.session.custom.username = None
    self.session.custom.email = None
    self.session.custom.user_id = None
    
    # Close the active popup (logout confirmation)
    system.perspective.closePopup("w-RvzoGi")
    
    # Redirect the user to the home page
    system.perspective.navigate("/")
