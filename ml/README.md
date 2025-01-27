### Working Environment  
To set up the environment, run:  
```bash
conda env create -f environment.yml
```
> **Note**: The same environment used for data parsing.

### Reproducing Δ-Learning Approach

#### 1. Split the dataset:
Split the dataset into training and testing sets.
Specify the path to the `props.csv` file obtained after parsing.
The training and test subsets will be saved in the specified directory (e.g., the `data` directory).
```
python split.py data/props.csv data
```

#### 2. Train the model:
Train the linear regression-enhanced forest models.
The model instance performs feature scaling, feature selection, and hyperparameter tuning automatically during fitting.
Separate models are trained for each of the 4 targets at the **d4tzvp** level, using **xtb2** or **r2scan** features, and saved in the `models` directory.
```
python train.py data/train_subset.csv
```
> **Note**: Training will use all available cores and may take an extended amount of time.

#### 3. Evaluate the model:
Evaluate the model on the test subset. Metrics (MAE, RMSE, R<sup>2</sup>) are saved in `test_result.csv`.
```
python eval.py data/test_subset.csv
```
