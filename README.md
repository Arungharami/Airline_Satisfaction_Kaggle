# Airline Satisfaction — Kaggle S6E10

A reproducible Python starter for [Predicting Airline Satisfaction](https://www.kaggle.com/competitions/playground-series-s6e10), maintained by Arun Gharami.

Predict satisfaction probabilities using a fast SGD logistic baseline and an optional CPU CatBoost challenger. Select the model using a fixed stratified validation split and produce a checked submission CSV.

## Run in Kaggle

1. Join the competition and review its Rules.
2. Create a **Python** notebook. The error `Error in parse(text = input): unexpected symbol ... from pathlib` indicates an R session; switch the notebook language to Python.
3. Import `notebooks/Airline_Satisfaction_Kaggle_Starter.ipynb`.
4. Attach Playground Series S6E10 with Add Input / Add Data.
5. Restart the session and Run All. Inspect the positive-label mapping.
6. Save Version → Save & Run All, then submit that version's `submission.csv`.

Import the notebook file directly. Markdown markers such as `**=**` and HTML entities must not appear in Python code cells.

GitHub commits do not automatically update a Kaggle notebook. Re-import the latest file to sync code; use Kaggle to run the competition session and submit predictions.

## Run locally

Use Python 3.10 or newer.

```bash
git clone https://github.com/Arungharami/Airline_Satisfaction_Kaggle.git
cd Airline_Satisfaction_Kaggle
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run_notebook.py --data-dir /absolute/path/to/competition/files --output-dir outputs
```

On Windows activate the environment using `.venv\Scripts\activate`.
The input directory must contain `train.csv`, `test.csv`, and `sample_submission.csv`, obtained through your authorized Kaggle account.

CatBoost is optional: `python -m pip install catboost`. Without it, the baseline still generates predictions.

## Outputs and checks

- `submission.csv`: IDs follow sample-submission order; probabilities must be finite and between 0 and 1.
- `validation_results.csv`: ROC-AUC, log loss, and measured training time.
- `run_metadata.json`: configuration, label mapping, selected model, and software versions.
- `feature_importance.csv`: produced when CatBoost runs.

Input discovery supports renamed attachments and nested directories. Completely missing numerical predictors are dropped; imputation and encoding are fitted on the fitting split. ID is excluded from predictors.

## Verification and limitations

The fallback path was tested using synthetic mixed, numeric-only, categorical-only, and boolean-label fixtures, plus a missing-input case. These are engineering checks, not competition results. The actual competition data, CatBoost execution, and leaderboard score have not yet been verified.

The stratified split assumes independent rows. Inspect repeated passengers, groups, and time structure before using it for final evaluation. Validation is used for model selection and early stopping; it is not an independent final test.

Do not commit competition CSVs, credentials, model binaries, or generated predictions. Follow the competition Rules for data use and publication.
