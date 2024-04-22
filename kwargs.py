def buscar_datos(*args, **kwargs):
    datos_localizados = []
    
    if "database" in kwargs:
        database = kwargs["database"]
        for arg in args:
            found = False
            for data in database.values():
                if arg in data.values():
                    datos_localizados.append(arg)
                    found = True
                    break 
            if not found:
                print(f"La palabra '{arg}' no está en la base de datos.")
    print("Datos localizados en la base de datos:", datos_localizados)

database = {
    "persona1": {
        "primer_nombre": "Lionel",
        "segundo_nombre": "Andres",
        "primer_apellido": "Messi",
        "segundo_apellido": "Cuccittini"
    },
    
    "persona2": {
        "primer_nombre": "Santiago",
        "segundo_nombre": "Alberto",
        "primer_apellido": "Ortega",
        "segundo_apellido": "Flores"
    },

}

buscar_datos("Santiago","Messi","Franco","Picasso","Juan","Lautaro","Marcos", database=database)

