"""
Se incluyen las funciones necesarias para cargar los datos de la base de datos. 
Se asumen las credenciales de la base de datos y se utiliza sintaxis de MageAI para establecer la conexión.
"""

@data_loader
def load_data():

    schema = "analytics"
    table = "table_name" # Nombre genérico, se debe reemplazar por el nombre real de la tabla a cargar
    table_name = f"{schema}.{table}"
    profile = "default"

    start_position = 0
    chunk_size = 1000
    attempts = 0
    max_tries = 5

    df = pd.DataFrame()

    # Se asume que el archivo de configuración se encuentra configurado
    with Postgres.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
        while attempts < max_tries:
            query = f"SELECT * FROM {table_name} STARTPOS {start_position} MAXRESULTS {chunk_size}"
            try:
                data = loader.load(query)
                if data.empty:
                    break
                df = pd.concat([df, data], ignore_index=True)

                start_position += chunk_size
                attempts = 0
            except Exception as e:
                attempts += 1
                print(f"Error loading data: {e}. Attempt {attempts} of {max_tries}.")
                if attempts >= max_tries:
                    print("Max attempts reached. Stopping data loading.")
                    break

    return df
    
    