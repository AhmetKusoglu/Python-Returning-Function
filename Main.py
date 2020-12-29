import sqlite3


def user_database(name,surname,operation):
    connect=sqlite3.connect("Database1.db")
    cursor=connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_base(name TEXT,surname TEXT) """)

    def add_user():
        cursor.execute("INSERT INTO user_base VALUES(?,?)",(name,surname))
        connect.commit()
    
    def remove_user():
        cursor.execute( 'DELETE FROM user_base WHERE name=? ' ,(name,))
        connect.commit()
    
    
    if operation=="add_user":
        return add_user
    elif operation=="remove_user":
        return remove_user

user=user_database("Ahmet","Kusoglu","add_user")
user()

#user2=user_database("Ahmet","Kusoglu","remove_user")
#user2()


