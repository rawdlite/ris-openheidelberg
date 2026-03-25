import psycopg2
import pandas as pd

class PostgresDBClient:
    """
    A client for connecting to and querying a PostgreSQL database.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the PostgresDBClient.
        Loads configuration from the Config Class or a config dict.
        
        Args:
            config (Optional[Dict[str, Any]]): Database configuration dictionary.
        """
        self.config = config
        self.conn = None
        self.cursor = None
        
    def connect(self):
        """
        Connect to the database.
        """
        self.conn = psycopg2.connect(**self.config)
        self.cursor = self.conn.cursor()
        
    def disconnect(self):
        """
        Disconnect from the database.
        """
        self.cursor.close()
        self.conn.close()
        
    def execute(self, query: str, params: Optional[Tuple[Any, ...]] = None):
        """
        Execute a query.
        
        Args:
            query (str): SQL query to execute.
            params (Optional[Tuple[Any, ...]]): Parameters for the query.
        """
        self.cursor.execute(query, params)
        self.conn.commit()
        
    def fetchall(self, query: str, params: Optional[Tuple[Any, ...]] = None):
        """
        Fetch all results from a query.
        
        Args:
            query (str): SQL query to execute.
            params (Optional[Tuple[Any, ...]]): Parameters for the query.
            
        Returns:
            List[Tuple[Any, ...]]: List of results.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
        
    def fetchone(self, query: str, params: Optional[Tuple[Any, ...]] = None):
        """
        Fetch one result from a query.
        
        Args:
            query (str): SQL query to execute.
            params (Optional[Tuple[Any, ...]]): Parameters for the query.
            
        Returns:
            Tuple[Any, ...]: Single result.
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
        
    def fetchdf(self, query: str, params: Optional[Tuple[Any, ...]] = None):
        """
        Fetch all results from a query as a pandas DataFrame.
        
        Args:
            query (str): SQL query to execute.
            params (Optional[Tuple[Any, ...]]): Parameters for the query.
            
        Returns:
            pd.DataFrame: DataFrame containing the results.
        """
        self.cursor.execute(query, params)
        return pd.DataFrame(self.cursor.fetchall(), columns=[desc[0] for desc in self.cursor.description])
        
    