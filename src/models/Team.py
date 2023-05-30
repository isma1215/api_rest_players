from db.db import get_connection
from .entities.Soccer_Team import Soccer_Team


class Model_Team():

    @classmethod
    def get_teams(self):
        try:
            connection = get_connection()
            teams = []

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM soccer_teams WHERE club_name = %s", ("los Heros",))
                resultset = cursor.fetchall()

                for row in resultset:
                    team = Soccer_Team(row[0], row[1], row[2])
                    teams.append(team.to_Json())
                return teams

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_one_team(self, id):
        try:
            connection = get_connection()
            teams = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM soccer_teams WHERE id = %s", (id,))
                resultset = cursor.fetchall()

                if resultset != []:
                    for row in resultset:
                        team = Soccer_Team(row[0], row[1], row[2])
                        teams.append(team.to_Json())
                    return teams

                else:
                    return [{'message':'not found teams'}] 
        except Exception as ex:
            return Exception(ex)
