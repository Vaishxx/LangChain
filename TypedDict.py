from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int

new_person: Person ={ 'name': "Vaish", 'age': 22}  
print(new_person)
