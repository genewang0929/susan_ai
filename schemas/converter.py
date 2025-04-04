from schemas.estimate_room import Estimate_Room
from models import Room
from schemas.item import Item
from schemas.estimate import Estimate
from schemas.insured import Insured
from schemas.assignment import Assignment
from schemas.category import Category

from typing import List

class Converter():
    assignment: Assignment
    insured: Insured
    estimate_room: List[Estimate_Room]
    estimate: Estimate
    categories: List[Category]
    items: List[Item]
    rooms: List[Room]


    def __init__(self):
        self.estimate_room = []
        self.rooms = []
        self.items = []
        self.categories = []
