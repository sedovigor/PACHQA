import sys
import numpy as np
import pandas as pd

SEED = 42

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split.py <input_csv_path> <output_dir>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_dir = sys.argv[2]

    # Load data
    df = pd.read_csv(input_path)
    
    # Preprocess data
    df = df.drop(['subset', 'key', 'formula'], axis=1)
    df = df.pivot(index=['id', 'smiles', 'mwt', 'nH', 'nC', 'nCl'],
                  columns='level')
    df.columns = df.columns.map(lambda x: '_'.join(x))
    
    # Select relevant columns
    df = df[
        [col for col in df.columns if 'xtb2' in col] +
        [col for col in df.columns if 'r2scan' in col] +
        [col for col in df.columns if 'd4tzvp' in col]
    ]
    
    # Shuffle and split data
    df = df.sample(frac=1, random_state=SEED)
    idx = round(len(df) * 0.2)
    
    train = df.iloc[:-idx]
    test = df.iloc[-idx:]
    
    # Save train and test subsets
    train.to_csv(f"{output_dir}/train_subset.csv")
    test.to_csv(f"{output_dir}/test_subset.csv")