from database.DB_connect import DBConnect

from model.neighbor import Neighbor
from model.sighting import Sighting
from model.state import State


class DAO():
    @staticmethod
    def get_all_neighbors():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM neighbor"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(
                Neighbor(row["state1"], row["state2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_sightings():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM sighting"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(
                Sighting(row["id"], row["datetime"], row["city"], row["state"], row["country"], row["shape"], row["duration"], row["duration_hm"], row["comments"], row["dateposted"], row["latitude"], row["longitude"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_states():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM state"""

        cursor.execute(query, ())

        for row in cursor:
            result.append(
                State(row["id"], row["Name"], row["Capital"], row["Lat"], row["Lng"], row["Area"], row["Population"], row["Neighbors"]))

        cursor.close()
        conn.close()
        return result


