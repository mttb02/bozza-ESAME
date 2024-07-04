from dataclasses import dataclass

#from datetime import datetime ALTERNATIVA

@dataclass
class Sighting:
    _id: int
    _datetime: str #ATTENZIONE: VALUTARE SE ADEGUATO IL TIPO DI DATO AL CONTESTO
    _city: str
    _state: str
    _country: str
    _shape: str
    _duration: int
    _duration_hm: str
    _comments: str
    _date_posted: str #ATTENZIONE: VALUTARE SE ADEGUATO IL TIPO DI DATO AL CONTESTO
    _latitude: float
    _longitude: float

    @property
    def id(self):
        return self._id

    @property
    def datetime(self):
        return self._datetime

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    @property
    def country(self):
        return self._country

    @property
    def shape(self):
        return self._shape

    @property
    def duration(self):
        return self._duration

    @property
    def duration_hm(self):
        return self._duration_hm

    @property
    def comments(self):
        return self._comments

    @property
    def date_posted(self):
        return self._date_posted

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"Nome: {self.id}"
