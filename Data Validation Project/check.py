import pandas as pd
from sqlalchemy import create_engine

# Database credentials and connection
# source
DB_CONNECTION_STRING = "postgresql://postgres:admin@localhost:5432/Project"
engine_s = create_engine(DB_CONNECTION_STRING)

#target
DB_CONNECTION_STRING = "postgresql://postgres:admin@localhost:5432/Project-target"
engine_t = create_engine(DB_CONNECTION_STRING)

def read_source_data(query):
    """Executes a SQL query and returns the result as a Pandas DataFrame."""
    with engine_s.connect() as connection:
        df = pd.read_sql(query, connection)
    return df

def read_target_data(query):
    with engine_t.connect() as connection:
        df = pd.read_sql(query, connection)
    return df

# SQL Queries to fetch data
source_query = "SELECT * FROM employee;"
target_query = "SELECT * FROM employee_t;"

# Read data from database
source_df = read_source_data(source_query)
target_df = read_target_data(target_query)

# Display first few rows
print("Source Table Data:")
print(source_df.head())

print("\nTarget Table Data:")
print(target_df.head())


def count_validation(source_df, target_df):
    """Checks if row counts match between source and target tables."""
    source_count = len(source_df)
    target_count = len(target_df)

    print(f"Source Table Row Count: {source_count}")
    print(f"Target Table Row Count: {target_count}")

    if source_count == target_count:
        print("✅ Count Validation Passed!")
    else:
        print("❌ Count Validation Failed! Row count mismatch.")

    return source_count, target_count


# Run Count Validation
count_validation(source_df, target_df)



def null_validation(df, table_name, key_columns):
    """Checks for NULL values in primary key columns."""
    null_values = df[key_columns].isnull().sum()

    print(f"\nChecking NULL values in {table_name}:")
    print(null_values)

    if null_values.sum() == 0:
        print("✅ Null Validation Passed! No missing values found.")
    else:
        print("❌ Null Validation Failed! Missing values detected.")

# Define Primary Key Columns
primary_key_columns = ['employee_id']  # Modify as per your table schema

# Run Null Validation
null_validation(source_df, "Source Table", primary_key_columns)
null_validation(target_df, "Target Table", primary_key_columns)






def row_comparison(source_df, target_df, key_columns):
    """Finds rows present in source but missing in target, and vice versa."""

    # Convert primary key column(s) to set for quick comparison
    source_keys = set(source_df[key_columns[0]])
    target_keys = set(target_df[key_columns[0]])

    missing_in_target = source_keys - target_keys  # Rows in Source but not in Target
    missing_in_source = target_keys - source_keys  # Rows in Target but not in Source

    # Fetch missing rows
    missing_source_df = source_df[source_df[key_columns[0]].isin(missing_in_target)]
    missing_target_df = target_df[target_df[key_columns[0]].isin(missing_in_source)]

    print(f"\nRows present in Source but missing in Target: {len(missing_source_df)}")
    print(missing_source_df)

    print(f"\nRows present in Target but missing in Source: {len(missing_target_df)}")
    print(missing_target_df)

    return missing_source_df, missing_target_df


# Run Row Comparison
missing_source_df, missing_target_df = row_comparison(source_df, target_df, primary_key_columns)
