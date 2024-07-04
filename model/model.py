from database.DAO import DAO
import networkx as nx

from geopy import distance
import copy


class Model:
    def __init__(self):
        # self._valori_fissi = None
        # self.get_valori_fissi()

        self._graph = nx.Graph()
        self._digraph = nx.DiGraph()
        # self._map_valori = {} MapId (associa all'id un oggetto con cui poi puntare al grafo)

        # self.output_ricorsione = None #Da adattare in base all'ouput desiderato



    #def get_valori_fissi:
    #    self._valore_fisso = DAO.get_valore_fisso()

    #@property
    #def valori_fissi(self):
        #return self._valori_fissi

    def get_neighbors(self):
        return DAO.get_all_neighbors()

    def get_sightings(self):
        return DAO.get_all_sightings()

    def get_states(self):
        return DAO.get_all_states()


    def crea_grafo(self):
        self._graph.clear()

        # temp_nodi = get_valori

        # for n in temp_nodi:
        #     self._map_nodi[n.id] = n
        # self._graph.add_nodes_from(self._map_nodi.keys(), weight = 0)


        # temp_relazioni = get_relazioni #deve restituire tupla di nodi
        # self._graph.add_edges_from(temp_relazioni[0], temp_relazioni[1], weight = 0)


        # for e in self._graph.edges:
            # Permette di ciclare sui vertici, e[0] è un nodo, e[1] un altro, e[2][weight] è il peso

    def ricorsione_esterna(self):
        # 1) resetto i valori esterni della ricorsione:
        # self.output_ricorsione = None

        # SO DA DOVE VOGLIO PARTIRE
        # 2) setto le a 0 le variabili parziali (None, 0, "", []) in base al caso
        # temp_output_ricorsione = None
        # temp_oggetti_visitati = None
        # temp_variabile_interna = None

        # 2a) chiamo la ricorsione
        # self._ricorsione(ogg_da_cui_partire, ogg_da_visitare, temp_ogg_visitati, temp_variabile_interna, temp_output_ricorsione)

        # NON M INTERESSA DA DOVE PARTO

        # 3b) non so da dove voglio partire
        # for o in oggetti_da_cui_partire:
            # SETTA A 0 LE VARIABILI PARZIALI
            # self._ricorsione(o, ogg_da_visitare, temp_ogg_visitati, temp_variabile_interna, temp_output_ricorsione)

    def _ricorsione(self, o, ogg_da_visitare, ogg_visitati, variabile_interna, temp_output_ricorsione):
        if self._condizione_di_uscita(valori):
            if self._condizione_ottima(valori):
                self.output_ricorsione = temp_output_ricorsione #ATTENZIONE: passare per valore non per riferimento
            return
        else:
            for o in ogg_da_visitare:
                if _condizione_di_validita(valori):
                    #Modifica variabili
                    self.ricorsione(o, variabili_modificate)
                    #ripristina variabili

                #else: Brutto, meglio evitare tutta sta roba sotto
                #    if sum(temp_distanze) > sum(self.distanze):
                #        self.distanze = copy.deepcopy(temp_distanze)
                #        self.percorso = copy.deepcopy(temp_percorso)
                #        self.costi = copy.deepcopy(temp_costi)


    # def _condizione_di_X(dati_input): #Uguale per tutte le condizioni
    #     if dati_input rispetta condizione:
    #         return True
    #     else:
    #         return False

    def get_nodes(self):
        return self._graph.nodes()

    def get_edges(self):
        return list(self._graph.edges(data=True))


    def get_num_of_nodes(self):
        return self._graph.number_of_nodes()

    def get_num_of_edges(self):
        return self._graph.number_of_edges()


    def get_comp_connessa_grafo(self, v):
        return nx.connected_components(v)

    def get_num_comp_connesse(self):
        return nx.number_connected_components(self._graph)

    def get_ver_confinanti(self, v):
        return list(self._graph.neighbors(v))


    def getRaggiungibiliDFS(self, v):
        tree = nx.dfs_tree(self._graph, v)
        temp_raggiungibili = list(tree.nodes)
        temp_raggiungibili.remove(v)
        return temp_raggiungibili



