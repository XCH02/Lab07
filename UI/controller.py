import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        #aggiungo opzione nessun filtro
        self._view.filtraggio_biblioteca.options.append(ft.DropdownOption("Nessun filtro"))
        #prendo il contenitore di biblioteche
        biblioteche = self._model.get_biblioteche()
        #itero biblioteca su biblioteche e appendo il nome della biblioteca
        for b in biblioteche:
            self._view.filtraggio_biblioteca.options.append(ft.DropdownOption(b.nome))
        #stessa cosa qui
        self._view.filtraggio_genere.options.append(ft.DropdownOption("Nessun filtro"))

        generi= self._model.get_generi()
        for g in generi:
            self._view.filtraggio_genere.options.append(ft.DropdownOption(g))

        self._view.update()


    # CALLBACKS DROPDOWN
    # TODO
    #richiamo della funzione per salvare la scelta dell'utente
    def sel_biblioteca(self,e):
        self.biblioteca_selezionata = (self._view.filtraggio_biblioteca.value)
    def sel_genere(self,e):
        self.genere_selezionato = (self._view.filtraggio_genere.value)

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self,e):
        self._view.list_view.controls.clear()

        libri= self._model.get_libri_filtrati(self.biblioteca_selezionata,
                                             self.genere_selezionato)
        if libri is None or len(libri) == 0:
            self._view.show_alert("Nessun libro trovato")
        for l in libri:
            self._view.list_view.controls.append(ft.Text(f"{l}"))

        self._view.update()


