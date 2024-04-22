
def buscar_datos(*args, **kwargs):
    resultado = {}
    
    for key, data in kwargs.items():
        if sorted(data.values()) == sorted(args):
            resultado[key] = data  
            
    if resultado:
        print("Resultado encontrados:")
        for key, value in resultado.items():
            print(key)
            for k, v in value.items():
                print(f"\t{k}: {v}")
        
    return resultado

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
    "persona3": {
        "primer_nombre": "Juan", 
        "segundo_nombre": "Roman",
        "primer_apellido": "Riquelme",
        "segundo_apellido": "Velazquez"
    },
}


