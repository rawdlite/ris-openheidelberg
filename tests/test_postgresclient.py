from src.postgresdbclient import PostgresDBClient

def test_postgresclient_init():
    client = PostgresDBClient()
    assert client.config is not None
    

def test_postgresclient_connect():
    client = PostgresDBClient()
    client.connect()
    assert client.conn is not None
    client.disconnect()
    
    
def test_postgresclient_fetchdf():
    client = PostgresDBClient()
    client.connect()
    df = client.fetchdf("SELECT DISTINCT result FROM ris1.agendaitem;")
    assert df is not None
    assert len(df) > 0
    client.disconnect()