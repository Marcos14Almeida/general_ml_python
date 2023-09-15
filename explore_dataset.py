
# Explore dataset functions

# =============================================================================
# ================================= Libraries =================================
# =============================================================================

# =============================================================================
#                                     Main
# =============================================================================
def explore(df):

    print("Dataframe types:")
    print(df.dtypes)

    for column in df.columns:
        if df[column].dtype != 'int64' or df[column].dtype != 'float64':
            print()
            print("Explore Column: " + column)
            print(df[column].dtype)
            print("Unique Values:")
            print(df[column].value_counts())

    print("Dataframe TOP 10 rows")
    print(df.head(10))

    print("Dataframe Column Names")
    print(df.columns)
