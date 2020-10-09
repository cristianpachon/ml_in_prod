from application import mongo
from datetime import datetime

def manage_db_action(action, table, data):
    table_full_path = eval(f'mongo.db.{table}')
    data_copied = data.copy()

    if action == 'insert':
        if not 'created_at' in data_copied.keys():
            data_copied['created_at'] = datetime.utcnow()
        table_full_path.insert_one(data_copied).inserted_id
