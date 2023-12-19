import pandas as pd
import numpy as np

def format_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path, sep="[,;:]", index_col=False)
    
    # TODO: check the row width
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
