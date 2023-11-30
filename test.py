import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn import model_selection
from sklearn.feature_selection import SelectFromModel, SelectKBest, chi2, mutual_info_classif
from sklearn.linear_model import LogisticRegression
import warnings
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix, log_loss, accuracy_score, roc_auc_score, precision_score, recall_score, f1_score

warnings.filterwarnings('ignore')
plt.style.use('fivethirtyeight')
pd.set_option('display.max_columns', 26)

data = pd.read_csv('data/ckd_clean.csv')

print(data.info())

# Extracting categorical and numerical columns
cat_cols = [col for col in data.columns if data[col].dtype == 'object']
num_cols = [col for col in data.columns if data[col].dtype != 'object']

data['class'] = data['class'].map({'ckd': 1, 'not ckd': 0})
data['class'] = pd.to_numeric(data['class'], errors='coerce')