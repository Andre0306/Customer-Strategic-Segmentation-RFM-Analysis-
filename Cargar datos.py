import pandas as pd
from datetime import timedelta

# Cargar datos
df = pd.read_csv('ventas_historicas_rfm.csv')
df['fecha'] = pd.to_datetime(df['fecha'])

# Definir fecha de análisis (hoy)
fecha_analisis = df['fecha'].max() + timedelta(days=1)

# Agrupar por cliente
rfm = df.groupby('id_cliente').agg({
    'fecha': lambda x: (fecha_analisis - x.max()).days,
    'id_transaccion': 'count',
    'monto_venta': 'sum'
}).rename(columns={'fecha': 'Recencia', 'id_transaccion': 'Frecuencia', 'monto_venta': 'Monetario'})

# Crear los puntajes (1 a 5) basándose en las columnas originales
rfm['R_Score'] = pd.qcut(rfm['Recencia'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frecuencia'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetario'], 5, labels=[1, 2, 3, 4, 5])

# Crear puntaje total y segmentos
rfm['RFM_Score'] = rfm['R_Score'].astype(int) + rfm['F_Score'].astype(int) + rfm['M_Score'].astype(int)

def segmentar(df):
    score = df['RFM_Score']
    if score >= 13: return 'Campeones'
    elif score >= 10: return 'Leales'
    elif score >= 7: return 'En Riesgo'
    else: return 'Perdidos'

rfm['Segmento'] = rfm.apply(segmentar, axis=1)
rfm.to_csv('clientes_segmentados_rfm.csv')
print("¡Segmentación completada con éxito!")