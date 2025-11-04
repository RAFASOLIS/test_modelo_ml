### 2.3. Fichero `api.py`

import numpy as np
import joblib
from flask import Flask, request, jsonify

# 1. Inicializar la App Flask
app = Flask(__name__)

# 2. Cargar el modelo entrenado
# Este fichero .pkl debe existir (generado por el Notebook)
try:
    modelo = joblib.load('modelo_entrenado.pkl')
    print("Modelo cargado correctamente.")
except FileNotFoundError:
    print("Error: 'modelo_entrenado.pkl' no encontrado.")
    modelo = None

# 3. Definir el endpoint de predicción
@app.route('/predict', methods=['POST'])
def predict():
    if modelo is None:
        return jsonify({"error": "Modelo no cargado"}), 500

    try:
        # Obtener los datos JSON de la petición
        data = request.get_json(force=True)
        
        # Asegurarse de que los datos de entrada coinciden con las features
        # (Esto debe ser adaptado a las features reales del modelo)
        features = np.array(data['features']).reshape(1, -1)
        
        # 4. Realizar la predicción
        prediction = modelo.predict(features)
        
        # 5. Devolver la predicción
        return jsonify({'prediction': prediction[0]})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# 6. Punto de entrada para ejecutar el servidor
if __name__ == '__main__':
    # Usar host='0.0.0.0' para que sea accesible desde el contenedor Docker
    app.run(host='0.0.0.0', port=5000)