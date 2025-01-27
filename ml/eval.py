import sys
import pickle
import pandas as pd
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2

# Define base feature levels and targets
base_features = ['mwt', 'nH', 'nC', 'nCl']
levels = ['xtb2', 'r2scan']
targets = ['dH_d4tzvp', 'gap_d4tzvp', 'Mu_d4tzvp', 'alpha_d4tzvp']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python eval.py <test_data_path>")
        sys.exit(1)

    # Load test data
    path = sys.argv[1]
    df = pd.read_csv(path)

    results = []

    # Evaluate models
    for level in levels:
        feature_set = base_features + [col for col in df.columns if level in col]
        for target in targets:
            print(f"Testing model for {target} using {level} features...")
            
            # Load the model
            name = f'models/{target}_on_{level}.pickle'
            with open(name, 'rb') as file:
                model = pickle.load(file)
            
            # Make predictions
            y_test = df[target]
            y_pred = model.predict(df[feature_set])
            
            # Calculate metrics
            results.append({
                'feature_set': level,
                'target': target,
                'mae': mae(y_test, y_pred),
                'rmse': mse(y_test, y_pred)**0.5,
                'r2': r2(y_test, y_pred),
            })

    # Save results to CSV
    pd.DataFrame(results).to_csv('test_result.csv', index=False)
