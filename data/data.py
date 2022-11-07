from dataclasses import dataclass


@dataclass
class Person:
    fullname: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
