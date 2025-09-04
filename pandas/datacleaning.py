import pandas as pd

# User info
users = pd.DataFrame({
    'user_id': [101, 102, 103, 104],
    'name': ['Ali', 'Sara', 'Usman', 'Zara'],
    'country': ['PK', 'PK', 'IN', 'IN']
})

# Transactions
transactions = pd.DataFrame({
    'user_id': [101, 103, 105],
    'txn_id': ['TX1001', 'TX1002', 'TX1003'],
    'amount': [500, 800, 1000]
})

# Login logs (index-based)
logins = pd.DataFrame({
    'login_time': ['2024-01-01', '2024-01-02', '2024-01-03'],
}, index=[101, 102, 106])

users_indexed = users.set_index('user_id')
result=pd.merge(users,transactions,on='user_id',how='inner')
print(result)
result2=pd.merge(transactions,users,on='user_id',how='left')
print(result2)
result1=pd.merge(transactions,users,on='user_id',how='outer')
print(result1)
result3=pd.merge(users_indexed,logins, left_index=True,right_index=True ,how='inner')
print(result3)