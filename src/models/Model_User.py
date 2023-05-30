from db.db import get_connection
from .entities.User import User


class Model_User():

    @classmethod
    def get_all_users(self):
        try:
            connection = get_connection()
            users = []
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM users")
                resultset = cursor.fetchall()
                print(resultset)
                for row in resultset:
                    user = User(row[0],row[1],row[3],row[2],row[4])
                    users.append(user.to_Json())

                connection.close()
                return users
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_for_name(self, name):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                    
                cursor.execute('SELECT * FROM users WHERE name = %s', (name,))
                row = cursor.fetchone()
                
                user = None
                if row != None:
                    user = user = User(row[0],row[1],row[3],row[2],row[4])
                    user = user.to_Json()
                
                return user
        except Exception as ex:
            raise Exception(ex)
   
    @classmethod
    def get_for_id(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                    
                cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
                row = cursor.fetchone()
                
                user = None
                if row != None:
                    user = user = User(row[0],row[1],row[3],row[2],row[4])
                    user = user.to_Json()
                
                return user
        except Exception as ex:
            raise Exception(ex)    
        
    @classmethod
    def login(self ,name, password):
        name = name
        user = self.get_for_name(name)
        if not password == user["password"]:
            user = None
        return user
    
    @classmethod
    def add_user(self,user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO users (id,name,password,soccer_team)
                               VALUES (%s,%s,%s,%s)""" , (user.id,user.name,user.password,user.soccer_team))
                affected_row = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_row
        
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def delete_user(self,user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                
                cursor.execute("DELETE from users WHERE id = %s",(user.id,))
                affected_row = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_row

        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update(self,user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("UPDATE users SET name= %s , password = %s ,soccer_team = %s WHERE id = %s",
                               (user.name, user.password, user.soccer_team, user.id ))
                affected_row = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_row
        
        except Exception as ex:
            raise Exception(ex)
        
            
            

