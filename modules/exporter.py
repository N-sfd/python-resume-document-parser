def export_csv(df, path="data/reviews.csv"):
    df.to_csv(path, index=False)