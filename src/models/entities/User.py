class User():
    def __init__(self, id, name=None, password=None, master=None , soccer_team=None) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.master = master
        self.soccer_team = soccer_team
    
    def to_Json(self):
        return {
            'id':self.id,
            'name':self.name,
            'password':self.password,
            'soccer_team': self.soccer_team,
            'master':self.master,
            
        }
