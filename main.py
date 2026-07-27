from extract import extract_data

def main():
    print("Starting ETL Pipeline...\n")

    df = extract_data()

    print("\nPipeline completed sucessfully")

    print(f"\nRows extracted: {(len(df))}")

    print("\nFirst five records:")
    print(df.head())
if __name__ == "__main__":
    main()