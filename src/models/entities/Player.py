class Player():
    def __init__(self, id , name = None, last_name = None , jersey_number = None, birthday = None, photo_url = None , team_soccer = None) -> None:
        self.id = id
        self.name = name
        self.last_name = last_name
        self.jersey_number = jersey_number
        self.birthday = birthday
        self.photo_url = photo_url
        self.team_soccer = team_soccer 
    
    def to_Json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'last_name':self.last_name,
            'jersey_number':self.jersey_number,
            'birthday':self.birthday,
            'photo_url' : self.photo_url,
            'team_soccer': self.team_soccer
        }