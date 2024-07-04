from dataclasses import dataclass


@dataclass
class Neighbor:
    _id1: str
    _id2: str


    @property
    def id1(self):
        return self._id1

    @property
    def id2(self):
        return self._id2

    def __hash__(self):
        return hash(self.id1+self.id2)

    def __str__(self):
        return f"Nome: {self.id1} - {self.id2}"