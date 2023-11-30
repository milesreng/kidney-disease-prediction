import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn import model_selection
from sklearn.feature_selection import SelectFromModel, SelectKBest, chi2, mutual_info_classif
from sklearn.linear_model import LogisticRegression, LinearRegression
import warnings
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, log_loss, accuracy_score, roc_auc_score, precision_score, recall_score, f1_score
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns', 26)

data = pd.read_csv('data/ckd_clean.csv')

# Extracting categorical and numerical columns
cat_cols = [col for col in data.columns if data[col].dtype == 'object']
num_cols = [col for col in data.columns if data[col].dtype != 'object']

data['class'] = data['class'].map({'ckd': 1, 'notckd': 0})
data['class'] = pd.to_numeric(data['class'], errors='coerce')

# print(data.info())

print(data.isna().sum().sort_values(ascending=False))

lr = LinearRegression()
imp = IterativeImputer(estimator=lr, missing_values=np.nan, max_iter=10,verbose=2, imputation_order='roman',random_state=0)
data[num_cols] = imp.fit_transform(data[num_cols])

# feature and label

X = data.drop(['class'], axis=1)
y = data['class']

def impute_mode(feature):
  mode = X[feature].mode()[0]
  X[feature] = X[feature].fillna(mode)

def random_value_imputation(feature):
  random_sample = X[feature].dropna().sample(X[feature].isna().sum())
  random_sample.index = X[X[feature].isnull()].index
  X.loc[data[feature].isnull(), feature] = random_sample

random_value_imputation('red_blood_cells')
random_value_imputation('pus_cell')

for col in cat_cols[:-1]:
  impute_mode(col)

for col in cat_cols:
    print(f"{col} has {data[col].nunique()} categories\n")

# all variables have 2 categories so we use label encoder

le = LabelEncoder()

for col in cat_cols[:-1]:
   X[col] = le.fit_transform(X[col])

# split train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2, random_state=0)

# normalization
minmax = MinMaxScaler()

X_train[num_cols] = minmax.fit_transform(X_train[num_cols])
X_test[num_cols] = minmax.transform(X_test[num_cols])

# build logistic regression model
