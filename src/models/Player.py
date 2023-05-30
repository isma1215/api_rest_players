from db.db import get_connection
from .entities.Player import Player


class ModelPlayer():

    @classmethod
    def get_players(self):
        try:
            connecion = get_connection()
            players = []

            with connecion.cursor() as cursor:
                cursor.execute('SELECT * FROM players ORDER BY birthday')
                resultset = cursor.fetchall()

                for row in resultset:
                    player = Player(row[0], row[1], row[2],
                                    row[3], row[4], row[5], row[6])
                    players.append(player.to_Json())
                connecion.close()
                return players

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_player_by_id(self,id):
        try:
            connecion = get_connection()
            player = {}
            with connecion.cursor() as cursor:
                cursor.execute('SELECT soccer_team FROM players WHERE id = %s',(id,))
                row = cursor.fetchone()

                player["soccer_team"] = row[0]
                connecion.close()
                return player
            
        except Exception as ex:
            return Exception(ex)

            
    @classmethod
    def get_one_player(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM players WHERE id = %s", (id,))
                row = cursor.fetchone()

                player = None
                if row != None:
                    player = Player(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    player = player.to_Json()
            connection.close()
            return player
            
        except Exception as ex:
            return Exception(ex)

        
    @classmethod
    def get_players_my_team(self,user):
        try:
            connecion = get_connection()
            players = []
            
            with connecion.cursor() as cursor:
                cursor.execute("SELECT * FROM players WHERE soccer_team = %s " , (user["soccer_team"],))
                resultset = cursor.fetchall()
                
                for row in resultset:
                    player = Player(row[0], row[1], row[2],
                                    row[3], row[4], row[5], row[6])
                    players.append(player.to_Json())
                connecion.close()
                return players

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_player(self, player):
        try:
            connecion = get_connection()
            with connecion.cursor() as cursor:
                cursor.execute("""INSERT INTO players (id,name,last_name,jersey_number,birthday,photo_url,soccer_team)
                VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                (player.id, player.name, player.last_name, player.jersey_number, player.birthday, player.photo_url, player.team_soccer))

                affected_row = cursor.rowcount
                connecion.commit()

            connecion.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_player(self, player):
        try:
            connecion = get_connection()
            with connecion.cursor() as cursor:
                cursor.execute("UPDATE players SET name = %s WHERE id = %s",(player.name, player.id))

                affected_row = cursor.rowcount
                connecion.commit()

            connecion.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_player(self,player):
        try:
            connecion = get_connection()
            with connecion.cursor() as cursor:
                cursor.execute("DELETE from players WHERE id = %s",(player.id,))
               
                affected_row = cursor.rowcount
                connecion.commit()
            connecion.close()
            return affected_row
        
        except Exception as ex:
            raise Exception(ex)
