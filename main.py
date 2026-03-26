from src.postgresdbclient import PostgresDBClient

def main():
    print("Hello from ris-openheidelberg!")
    client = PostgresDBClient()
    client.connect()
    df = client.fetchdf("SELECT DISTINCT result FROM ris1.agendaitem;")
    print(df)
    client.disconnect() 

if __name__ == "__main__":
    main()
