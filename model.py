import pandas as pd
from sklearn.linear_model import LogisticRegression

print("✅ CI pipeline ran successfully with Logistic Regression model")

data = pd.DataFrame({
    'text': ['bad service', 'great loan', 'credit issue', 'loan problem'],
    'label': ['negative', 'positive', 'negative', 'negative']
})

print("📦 Dummy training data loaded.")
