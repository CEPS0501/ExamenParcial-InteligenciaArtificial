from sklearn.linear_model import LinearRegression
from os import system as system

#Datos de entrenamiento:
x_train = [[1],[2],[3],[4],[5],[6],[7],[8]]

#Etiquetas:
y_train = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

#Crear y entrenar el modelo de regresion lineal
model = LinearRegression()
model.fit(x_train, y_train)


km = int(input("Ingrese el valor en Kilometros: "))

#Realizar Predicciones
km_to_convert = [[km]]
predicted_m = model.predict(km_to_convert)

#imprimir resultado
print(f"{km} kilometros equivalentes aproximadamente a {predicted_m[0]} Metros")