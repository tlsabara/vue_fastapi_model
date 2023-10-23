import pandas as pd
from sqlalchemy import Column, Integer, String, create_engine
from io import BufferedWriter, StringIO
import os
from dotenv import load_dotenv

load_dotenv()


def collect_view_data(viewname: str, interval: str = '3 months') -> StringIO:
    # siclo_pnm.vw_ap03_nhp
    conn_str = os.environ.get("DB_SICLO")

    engine = create_engine(conn_str)
    sql = f"select * from {viewname} as vw where vw.dat_registro >= CURRENT_DATE - INTERVAL '{interval}'"
    df = pd.read_sql(sql, engine)
    buffer = StringIO()
    df.to_json(buffer, 'records')

    return buffer

