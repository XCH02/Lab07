from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    # TODO

    def tot_libri(self):


        cnx=DBConnect.get_connection()
        #gestisco errore connesione
        if cnx is None:
            print("Connessione non stabilita")
        else:
            #creo la connesione
            cursor=cnx.cursor(dictionary=True)
            query= "SELECT * FROM libro"
            cursor.execute(query)

            risultato_libri=[]

            for row in cursor:
                libri=Libro(row["id"],
                            row["titolo"],
                            row["autore"],
                            row["genere"],
                            row["anno_pubblicazione"],
                            row["id_biblioteca"])
                risultato_libri.append(libri)

            cursor.close()
            cnx.close()
            return risultato_libri

