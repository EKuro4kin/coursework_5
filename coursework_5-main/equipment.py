import random
from dataclasses import dataclass, field
from typing import List
from random import uniform
import marshmallow_dataclass
import marshmallow
import json


@dataclass
class Armor:
    id: int
    name: int
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return random.uniform(self.min_damage, self.max_damage)


@dataclass
class EquipmentData:
    armors: list[Armor] = field(default_factory=list)
    weapons: list[Weapon] = field(default_factory=list)


class Equipment:

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        #return next(filter(lambda weapon: weapon.name == weapon_name, self.equipment.weapons))
        for weapon in self.equipment.weapons:
            if weapon_name == weapon.name:
                return weapon

    def get_armor(self, armor_name) -> Armor:
        return next(filter(lambda armor: armor.name == armor_name, self.equipment.armors))

    def get_weapons_names(self) -> list:
        return [weapon.name for weapon in self.equipment.weapons]

    def get_armors_names(self) -> list:
        return [armor.name for armor in self.equipment.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:
        # TODO этот метод загружает json в переменную EquipmentData
        equipment_file = open("./data/equipment.json", encoding='utf-8')
        data = json.load(equipment_file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        #сделали дата класс с валидацией с помощью маршмаллоу_датакласс
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError
