from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        result=[]
        libri= self._libro_dao.tot_libri()
        biblioteche = self._biblioteca_dao.tot_biblioteche()
        if biblioteche is not None and libri is not None:
            for b in biblioteche:
                for l in libri:
                    #tutti i libri
                    if biblioteca == "Nessun filtro" and genere == "Nessun filtro":
                        if l not in result:
                            result.append(l)
                    #solo libri per biblioteca
                    elif biblioteca == b.nome and genere == "Nessun filtro":
                        #libri solo di una biblioteca scelta
                        if b.id == l.id_biblioteca:
                            if l not in result:
                                result.append(l)
                    #solo libri di un genere
                    elif biblioteca =="Nessun filtro" and genere ==l.genere:
                        if l not in result:
                            result.append(l)

                    #libri di un genere in un biblioteca
                    elif b.nome ==biblioteca and l.genere == genere and b.id==l.id_biblioteca:
                        if l not in result:
                            result.append(l)
            return result
        else:
            return None


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        #prendo la lista dei libri dal dao
        lista_libri=[]
        libri= self._libro_dao.tot_libri()
        if libri is not None:
            for libro in libri:
                if libro.genere not in lista_libri:
                    lista_libri.append(libro.genere)
            return lista_libri
        else:
            return None


    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        # predo i dati dal dao e li restituisco direttamente perché sono già come in lista

        biblioteche= self._biblioteca_dao.tot_biblioteche()

        return biblioteche


