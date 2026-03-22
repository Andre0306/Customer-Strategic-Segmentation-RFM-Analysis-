import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración inicial
np.random.seed(42)
n_rows = 20000

# Generar IDs de clientes (500 clientes distintos)
customer_ids = [f"CUST-{i:03d}" for i in range(1, 501)]

# Crear el dataset de transacciones
data = {
    'id_transaccion': range(1, n_rows + 1),
    'id_cliente': np.random.choice(customer_ids, n_rows),
    'fecha': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 420)) for _ in range(n_rows)],
    'monto_venta': np.random.uniform(10.0, 500.0, n_rows).round(2),
    'categoria': np.random.choice(['Electrónica', 'Hogar', 'Moda', 'Alimentos'], n_rows)
}

df = pd.DataFrame(data)

# Guardar el CSV para Power BI
df.to_csv('ventas_historicas_rfm.csv', index=False)
print("¡Archivo 'ventas_historicas_rfm.csv' creado con éxito!")