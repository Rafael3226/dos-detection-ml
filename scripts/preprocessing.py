import pandas as pd

def main():
    # load the data
    df = pd.read_csv("MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv")
    df.columns = stripAndLowerColumns(df.columns) # strip And Lower Columns name
    df.dropna()  # drop rows with null values
    df.drop_duplicates()  # drop duplicate rows
    # Convert label column to binary values
    df["label"] = df["label"].apply(lambda x: 0 if "BENIGN" in x else 1)
    df = df.rename(columns={'label': 'is attack'})
    # Add new column to the dataframe
    df = addNewColumns(df)
    # remove rows with low correlation
    df = dropLowCorrelations(df,'is attack')
    # Save the preprocessed dataset
    df.to_csv("preprocessed_dataset.csv", index=False)

def stripAndLowerColumns(columns):
    newColumns = columns.str.strip()
    newColumns = columns.str.lower()
    return newColumns

def addNewColumns(df):
    # Create new features that may be useful in detecting attacks
    df["total packet length"] = df["total length of fwd packets"] + \
        df["total length of bwd packets"]
    df["packet length ratio"] = df["total length of fwd packets"] / \
        (df["total length of bwd packets"] + 0.1)
    df["packet rate"] = df["total fwd packets"] + df["total backward packets"]
    df["flow duration (ms)"] = df["flow duration"] / 1000
    return df

def dropLowCorrelations(df, target):
    # Set threshold for correlation with target variable
    corr_threshold = 0.1
    # Compute the correlation matrix between all features and the target variable
    corr_matrix = df.corr()[target].sort_values()
    nan_columns = list(corr_matrix[corr_matrix.abs() == 'nan'].index)
    # Get a list of column names with correlation below a certain threshold (e.g. 0.1)
    low_corr_cols = list(corr_matrix[corr_matrix.abs() < corr_threshold].index) 
    #append nan columns to low_corr_cols
    low_corr_cols.extend(nan_columns)
    # Drop columns with low correlation to target variable
    return df.drop(low_corr_cols, axis=1)

if __name__ == "__main__":
    main()
