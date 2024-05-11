import mysql.connector

class Publisher:
    def __init__(self) -> None:
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="oopdb"
        )
        self.cur = self.con.cursor()
        
    def addToTable(self, pub_name, pub_address,pub_phone):
        self.sql = "INSERT INTO publisher (pub_name,pub_address,pub_phone) values (%s,%s,%s)"
        self.values = (str(pub_name), str(pub_address), str(pub_phone))
        self.cur.execute(self.sql, self.values)
        print(self.cur.fetchall())
        self.con.commit()


    def updateTable(self, id,pub_name, pub_address,pub_phone):
        self.sql = "UPDATE publisher SET pub_name = %s, pub_address = %s, pub_phone = %s WHERE pub_id = %s"
        self.values = (str(pub_name), str(pub_address),str(pub_phone), int(id))
        self.cur.execute(self.sql, self.values)
        print("Updated: ", self.cur.fetchall())
        self.con.commit()

    def deleteDataFromTable(self, id):
        self.sql = "DELETE FROM publisher WHERE pub_id = %s"
        self.values = (int(id))
        print("TYPE: ", type(int(id)), "value: ", int(id))
        self.cur.execute(self.sql, self.values)
        print(self.cur.fetchall())
        self.con.commit()

    def getAllData(self):
        self.cur.execute("SELECT * FROM publisher")
        result = self.cur.fetchall()
        print(result)
        self.con.commit()
        return result
    
    
    

