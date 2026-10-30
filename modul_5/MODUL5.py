import pandas as pd
sessions = pd.read_csv('Sessions_analytics.csv')
orders = pd.read_csv('Orders_analytics.csv')
items = pd.read_csv('Order_items_analytics.csv')
models = pd.read_csv('Shoe_models_analytics.csv')
sessions['session_start'] = pd.to_datetime(sessions['session_start'])
orders['order_datetime'] = pd.to_datetime(orders['order_datetime'])
print("--- 5.1 ---")
visitors = sessions.groupby('device_type')['user_id'].nunique()
completed = orders[orders['order_status'] == 'completed']
buyers_sessions = completed[['session_id']].merge(
    sessions[['session_id', 'user_id', 'device_type']], on='session_id'
)
buyers = buyers_sessions.groupby('device_type')['user_id'].nunique()
conversion = buyers / visitors
print("Конверсия по устройствам:\n", conversion)
print("Ответ 5.1 (Максимум):", conversion.idxmax())
print("\n--- 5.2 ---")
first_sessions = sessions.groupby('user_id')['session_start'].min().reset_index()
first_sessions.columns = ['user_id', 'first_session']
completed_orders = orders[orders['order_status'] == 'completed']
first_orders = completed_orders.groupby('user_id')['order_datetime'].min().reset_index()
first_orders.columns = ['user_id', 'first_order']
df = first_sessions.merge(first_orders, on='user_id')
df['diff_minutes'] = (df['first_order'] - df['first_session']).dt.total_seconds() / 60
df_filtered = df[df['diff_minutes'] <= 10080]
median_time = df_filtered['diff_minutes'].median()
print(f"Ответ 5.2 (Медианное время в минутах): {median_time}")
print("\n--- 5.3 ---")
idx = sessions.groupby('user_id')['session_start'].idxmin()
first_sessions_ts = sessions.loc[idx].copy()
jan_first = first_sessions_ts[
    (first_sessions_ts['session_start'] >= '2026-01-01') & 
    (first_sessions_ts['session_start'] <= '2026-01-31')
]
feb_sessions = sessions[
    (sessions['session_start'] >= '2026-02-01') & 
    (sessions['session_start'] <= '2026-02-28')
]
feb_users = feb_sessions['user_id'].unique()
jan_first['returned'] = jan_first['user_id'].isin(feb_users)
retention = jan_first.groupby('traffic_source')['returned'].mean()
print("Удержание по каналам:\n", retention)
print("Ответ 5.3 (Максимум):", retention.idxmax())
print("\n--- 5.4 ---")
completed_ids = orders[orders['order_status'] == 'completed']['order_id']
order_totals = items[items['order_id'].isin(completed_ids)].groupby('order_id')['item_total'].sum()
Q1 = order_totals.quantile(0.25)
Q3 = order_totals.quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
filtered = order_totals[(order_totals >= lower) & (order_totals <= upper)]
print(f"Ответ 5.4 (Количество оставшихся заказов): {len(filtered)}")
print("\n--- 5.5 ---")
completed_items = items[items['order_id'].isin(completed_ids)]
r = completed_items['discount_percent'].corr(completed_items['quantity'])
print(f"Ответ 5.5 (Корреляция): {r:.3f}")
print("\n--- 5.6 ---")
data = completed_items.merge(models[['model_id', 'category']], on='model_id')
result = data.groupby('category')['quantity'].sum().sort_values(ascending=False)
print("Продажи по категориям:\n", result)
print("Ответ 5.6 (Максимум):", result.idxmax())