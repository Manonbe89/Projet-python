class Fight_action : 

    def __init__(self, user, action_type, target):
        self.user = user
        self.action_type = action_type
        self.target = target

    def _get_user(self):
        return self.user
    
    def _get_action_type(self):
        return self.action_type
    
    def _get_target(self):
        return self.target