import tensorflow as tf
import numpy as np

# Datos de entrenamiento
celsius = np.array([-45.94, -42.04,  -7.73,  17.74, -22.95,  39.66, -45.10,  -2.61,   8.11,   9.52,
 -31.95,   8.62,  30.96,  47.24,  15.25, -24.13,  -7.18,  -8.79,  49.36, -33.72,
 -19.96, -48.09, -26.40,  49.45,  31.63,   9.99,  33.40, -44.31,  46.14,  -8.43,
 -39.35, -23.43, -29.58, -14.01, -29.43, -24.23,  -5.72,  -0.17,   0.90,  11.01,
 -12.82,  16.81, -24.39,  44.92, -44.92,   8.05, -39.19,   8.87, -41.63, -23.63,
 -49.95, -21.82, -19.15,  31.07,   4.35,  42.53,   6.34,  -3.01,  12.18,  24.76,
 -12.00, -35.70,  36.28, -49.79, -23.97,  30.18, -30.14,  49.92,   9.83, -47.55,
 -26.49,  18.75, -30.44,  -7.55, -37.76, -36.55,   1.04, -34.65, -42.45,  -0.18,
  47.40, -17.88,  17.01,   8.52, -36.44, -11.10, -23.10,  15.47, -16.77, -33.57,
   9.79,  49.28,  -8.50,  -3.48, -20.86,  30.89,   5.38,  -0.77, -42.42, -13.66]
, dtype=float)

kelvin = np.array([227.21, 231.11, 265.42, 290.89, 250.20, 312.81, 228.05, 270.54, 281.26, 282.67,
 241.20, 281.77, 304.11, 320.39, 288.40, 249.02, 265.97, 264.36, 322.51, 239.43,
 253.19, 225.06, 246.75, 322.60, 304.78, 283.14, 306.55, 228.84, 319.29, 264.72,
 233.80, 249.72, 243.57, 259.14, 243.72, 248.92, 267.43, 272.98, 274.05, 284.16,
 260.33, 289.96, 248.76, 318.07, 228.23, 281.20, 233.96, 282.02, 231.52, 249.52,
 223.20, 251.33, 254.00, 304.22, 277.50, 315.68, 279.49, 270.14, 285.33, 297.91,
 261.15, 237.45, 309.43, 223.36, 249.18, 303.33, 243.01, 323.07, 282.98, 225.60,
 246.66, 291.90, 242.71, 265.60, 235.39, 236.60, 274.19, 238.50, 230.70, 272.97,
 320.55, 255.27, 290.16, 281.67, 236.71, 262.05, 250.05, 288.62, 256.38, 239.58,
 282.94, 322.43, 264.65, 269.67, 252.29, 304.04, 278.53, 272.38, 230.73, 259.49]
, dtype=float)

# Configuración del modelo
neurons = int(input("Neurons: "))

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=neurons, activation='relu'),
    tf.keras.layers.Dense(units=1)
])

# Compilación del modelo
precision = float(input("Precision of the model: "))

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=precision),
    loss='mean_squared_error'
)

# Entrenamiento del modelo
epochs = int(input("Number of epochs: "))

print("Training initialized...")
historial = model.fit(celsius, kelvin, epochs=epochs, verbose=2)
print("Model trained!")

# Predicciones
celsius_entries = np.array([-11, 100, 30, 0, 43], dtype=float)
results = model.predict(celsius_entries)

# Mostrar resultados
for index in range(len(results)):
    correct_answer = celsius_entries[index] + 273.15
    accuracy = (results[index] / correct_answer) * 100
    print(f"Celsius: {celsius_entries[index]} - Predicted Kelvin: {results[index][0]:.2f}")
    print(f"Accuracy: {accuracy[0]:.2f} %\n")
