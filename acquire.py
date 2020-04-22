import numpy as np
import pandas as pd

import env


def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(env.user, env.password, env.host, dbname)

def get_telco_data():
    sql_query = """
    SELECT c.*, ct.contract_type, ist.internet_service_type 
    FROM customers c
    JOIN contract_types ct ON ct.contract_type_id = c.contract_type_id
    JOIN internet_service_types ist ON ist.internet_service_type_id = c.internet_service_type_id
    JOIN payment_types pt ON pt.payment_type_id = c.payment_type_id

    """
    return pd.read_sql(sql_query, get_db_url('telco_churn'))