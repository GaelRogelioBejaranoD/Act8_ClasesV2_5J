print(" Clases v2 Bejarano Dominguez")
                                                # zona de clase
class Datos:
                                                # el constructor 
    def __init__(self, peso, estatura):
        self.bw = peso
        self.altura = estatura          
        
    def mostrarD (self):
        print(f"Estatura:{self.altura}(mts), Peso {self.bw}(kg)")
# Tupla 
    def RgrTuple(self):
        print("Una tupla de mis colores de piel favoritos:")
        RgrTupla = ("Top 1: blanco","Top 2: Café","Top 3: Negro")
        for v1 in RgrTupla:
            print(v1)
# Lista 
    def mi_lista (self):
        celulares = ["S23 Ultra (Samsung)", "iPhone 15 PRO (Apple),","Nothing Phone 2 (quien sabe)"]
        print(celulares)
        for i in celulares:
            print(i)
# Set 
    def SetEj(self):
        print("A continuacion uso de set para describirme")
        RgrDesc = {"Alto","Gordo","Negro","120 en banca"}
        for v1 in RgrDesc:
            print(v1)
# Diccionario 
    def Dikkionario(self):
        print("A continuacion mis cosas favoritas en esta vida (Diccionario): ")
        kciD = {
        "AFav" : "jim",
        "CLFav" : "Negro mate",
        "JFav" : "Minecraft" }
        for i in kciD:
            print(kciD[i])
                                                # creacion de objetos
Roger = Datos("102","1.80")
                                                # utilizando el objeto
Roger.mostrarD()
print("Mi lista de celulares incluye lo siguiente (Rogelio Bejarano):")
Roger.mi_lista()
Roger.RgrTuple()
Roger.Dikkionario()
Roger.SetEj()



