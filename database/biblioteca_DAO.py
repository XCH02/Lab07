from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO

    def tot_biblioteche(self):

        cnx=DBConnect.get_connection()

        if cnx is None:
            print("Connessione non stabilita")
            return None
        else:
            query= "SELECT * FROM biblioteca"

            cursor = cnx.cursor(dictionary = True)
            cursor.execute(query)
            risultato_biblioteche=[]
            for row in cursor:
                biblioteche=Biblioteca(row["id"], row["nome"], row["indirizzo"])
                risultato_biblioteche.append(biblioteche)

            cursor.close()
            cnx.close()
            return risultato_biblioteche


