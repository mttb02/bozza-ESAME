import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._list_valori_dd = []
        self._valore_dd = None


    def fillDD(self):

        self._list_valori_dd # = self._model.

        for v in self._list_valori_dd:
            self._view.NOMEDD.options.append(ft.dropdown.Option(key=v.id, text=v.__str__, data=v, on_click=self.read_valore_dd))

        self._view.update_page()

    def read_valore_dd(self, e):
        #self._valore_dd = e.control.key
        self._valore_dd = e.control.data


    def handle_graph(self, e):
        # Controllo sui dati del tipo:
        # self._valore._DD is not None
        # self._view._txtBox.value != ""
        # analisi sui valori ammissibili
        # SE CI SONO PROBLEMI:
        #1) self._view.create_alert("I dati devono essere bla bla")
        #2) return

        c = "condizione"

        self._model.crea_grafo(c)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.get_num_of_nodes()} Numero di archi: {self._model.get_num_of_edges()}"))

        self._view.update_page()

    def handle_path(self, e):
        # Controllo sui dati del tipo:
        # self._valore._DD is not None
        # self._view._txtBox.value != ""
        # analisi sui valori ammissibili
        # SE CI SONO PROBLEMI:
        # 1) self._view.create_alert("I dati devono essere bla bla")
        # 2) return

        self._view.update_page()