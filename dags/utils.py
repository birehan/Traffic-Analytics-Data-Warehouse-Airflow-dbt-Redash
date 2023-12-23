import pandas as pd
import numpy as np

import pandas as pd
import psycopg2
from sqlalchemy import create_engine

def format_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep="[,;:]", index_col=False)
    
    max_columns = 10
    extra_columns = df.shape[1] - max_columns
    
    if extra_columns > 0:
        # Create a list to hold the new rows
        new_rows = []
        
        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            # Extract the first 10 columns
            first_10_columns = row[:max_columns].tolist()
            
            # Create new rows for the remaining columns
            for i in range(0, extra_columns, 6):
                new_row = first_10_columns + row[max_columns + i : max_columns + i + 6].tolist()
                
                # Pad with NaN if the new row is less than 10 columns
                new_row += [np.nan] * (max_columns - len(new_row))
                
                # Append the new row to the list
                new_rows.append(new_row)
        
        # Create a new DataFrame with the modified rows
        new_df = pd.DataFrame(new_rows, columns=df.columns[:max_columns])
        return new_df
    else:
        # If the width is not greater than 10, return the original DataFrame
        return df


def run_sql_query(connection_params: dict, query: str) -> None:
    try:
        connection = psycopg2.connect(**connection_params)

        # Create a cursor
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(query)

        # Commit the transaction
        connection.commit()

        # Log success
        print("Log success")

    except Exception as e:
        print("Log the error: ", e)
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return None





def populate_dataframe_to_database(connection_params: dict, df: pd.DataFrame, table_name:str) -> None:
    try:
        # Extract connection parameters
        db_url = f"postgresql+psycopg2://{connection_params['user']}:{connection_params['password']}@{connection_params['host']}:{connection_params['port']}/{connection_params['database']}"

        # Create database connection
        engine = create_engine(db_url, echo=False)

        # Drop the table and its dependent objects (CASCADE)
        with engine.connect() as connection:
            connection.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")

        # Insert DataFrame into the database
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

        # Log information
        print(f"Inserted {len(df)} rows into the database table {table_name}.")

    except Exception as e:
        # Log the error
        print(f"Error inserting data into the database: {e}")

    finally:
        # Close the connection
        if engine:
            engine.dispose()

    return None
