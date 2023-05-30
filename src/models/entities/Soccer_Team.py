class Soccer_Team ():
    def __init__(self, id, club_name=None, url_shield=None) -> None:
        self.id = id
        self.club_name = club_name
        self.ulr_shield = url_shield
    
    def to_Json(self):
        return {
            'id' : self.id,
            'club_name' : self.club_name,
            'url_shield': self.ulr_shield
        }