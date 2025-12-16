import json

equipos = [
    {"nombre": "Melgar", "pais": "Peru", "nivelAtaque": 78, "nivelDefensa": 74},
    {"nombre": "Universitario", "pais": "Peru", "nivelAtaque": 80, "nivelDefensa": 79},
    {"nombre": "River Plate", "pais": "Argentina", "nivelAtaque": 85, "nivelDefensa": 83},
    {"nombre": "Flamengo", "pais": "Brasil", "nivelAtaque": 86, "nivelDefensa": 82},
    {"nombre": "Colo-Colo", "pais": "Chile", "nivelAtaque": 77, "nivelDefensa": 75},
]

json_str = json.dumps(equipos, ensure_ascii=False, indent=4)
print(json_str)


