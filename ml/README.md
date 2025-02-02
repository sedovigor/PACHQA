### Working Environment
To set up the environment, run:  
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
> **Note**: This is the same environment as for property parsing.

### The Δ-Learning model

#### 1. Split the dataset:
Split the dataset into the training and test sets.
Specify the path to the `props.csv` file obtained after parsing.
The training and test subsets will be saved in the specified directory (e.g., the `data` directory).
```
python split.py ../property_parsing/props.csv ./
```

#### 2. Train the model:
Train the linear regression-enhanced forest models.
The model automatically performs feature scaling, feature selection, and hyperparameter tuning during fitting.
Separate models are trained for each of the 4 targets at the **d4tzvp** level using **xtb2** or **r2scan** features, and saved in the `models` directory.
```
python train.py train_subset.csv
```
> **Note**: Training will use all available cores and may take a significant time.

#### 3. Evaluate the model:
Evaluate the model on the test subset. Metrics (MAE, RMSE, R<sup>2</sup>) are saved in `test_result.csv`.
```
python eval.py test_subset.csv
```
