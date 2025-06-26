import sqlite3

class DB:

 def __init__(self):
        # Conexão persistente (fora do 'with', senão fecha ao sair do bloco)
        self.con = sqlite3.connect("./database/ecommerce.db")
        self.cur = self.con.cursor()
        self.cur.execute("PRAGMA foreign_keys = ON")


class Users(DB):
    def __init__(self):
        super().__init__()
    
    def newuser(self):
        try:
            self.cur.execute("Insert into Users ")
        except sqlite3.Error as e:
            self.con.rollback()  # Desfaz qualquer alteração em caso de erro
            return(f"SQLite error occurred: {e}") 
        finally:
            self.con.close()

    def deluser(self,id):
        try:
            self.cur.execute("Delete From Users where id == ?",id)
        except sqlite3.Error as e:
            self.con.rollback()  # Desfaz qualquer alteração em caso de erro
            return(f"SQLite error occurred: {e}") 
        finally:
            self.con.close()
    def uodateuser(self,id):
        try:
            self.cur.execute("Update")
        except sqlite3.Error as e:
            self.con.rollback()  # Desfaz qualquer alteração em caso de erro
            return(f"SQLite error occurred: {e}") 
        finally:
            self.con.close()