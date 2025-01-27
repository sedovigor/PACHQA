import os
import sys
import pickle
import pandas as pd
from tuned_linear_forest import TunedLinearForest

# Constants
SEED = 0
FOLDS = 5

# Define base feature levels and targets
levels = ['xtb2', 'r2scan']
base_features = ['mwt', 'nH', 'nC', 'nCl']
targets = ['dH_d4tzvp', 'gap_d4tzvp', 'Mu_d4tzvp', 'alpha_d4tzvp']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python train.py <data_path>")
        sys.exit(1)

    path = sys.argv[1]
    df = pd.read_csv(path)

    os.makedirs('models', exist_ok=True)
    
    for level in levels:
        feature_set = base_features + [col for col in df.columns if level in col]
        for target in targets:
            print(f"Training model for {target} using {level} features...")
            
            model = TunedLinearForest(cv=FOLDS, random_state=SEED)
            model.fit(df[feature_set], df[target])
            
            with open(f"models/{target}_on_{level}.pickle", 'wb') as file:
                pickle.dump(model, file)