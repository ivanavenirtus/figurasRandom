import json

# Función para cargar y parsear el JSON
def lectorJson():
    # JSON de entrada
    json_data = '''{
        "geometricas": [
            {"circulo": {"radio": 50, "color": "rojo", "x": 50, "y": 45}},
            {"trianguloEquilatero": {"lado": 50, "x": 150, "y": 5}},
            {"pentagono": {"lado": 10, "color": "verde", "x": 50, "y": 45}},
            {"circulo": {"radio": 60, "x": 0, "y": 0}}
        ]
    }'''

    data = json.loads(json_data)

    # Iteramos sobre las figuras y las interpretamos
    for item in data['geometricas']:
        for key, value in item.items():
            print(f"Figura: {key}")
            for parametro, param_value in value.items():
                print(f"  {parametro}: {param_value}")

# Llamamos a la función para cargar e interpretar el JSON
lectorJson()

