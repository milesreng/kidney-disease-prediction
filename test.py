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

data = pd.read_csv('data/chronic_kidney_disease.csv')
data.drop('id', axis = 1, inplace = True)
data.columns = ['age',
                'blood_pressure',
                'specific_gravity',
                'albumin',
                'sugar',
                'red_blood_cells',
                'pus_cell',
                'pus_cell_clumps',
                'bacteria',
                'blood_glucose_random',
                'blood_urea',
                'serum_creatinine',
                'sodium',
                'potassium',
                'haemoglobin',
                'packed_cell_volume',
                'white_blood_cell_count',
                'red_blood_cell_count',
                'hypertension',
                'diabetes_mellitus',
                'coronary_artery_disease',
                'appetite',
                'peda_edema',
                'anemia',
                'class']

data['age'] = pd.to_numeric(data['age'], errors='coerce')
data['blood_pressure'] = pd.to_numeric(data['blood_pressure'], errors='coerce')
data['specific_gravity'] = pd.to_numeric(data['specific_gravity'], errors='coerce')
data['albumin'] = pd.to_numeric(data['albumin'], errors='coerce')
data['sugar'] = pd.to_numeric(data['sugar'], errors='coerce')
data['blood_glucose_random'] = pd.to_numeric(data['blood_glucose_random'], errors='coerce')
data['blood_urea'] = pd.to_numeric(data['blood_urea'], errors='coerce')
data['serum_creatinine'] = pd.to_numeric(data['serum_creatinine'], errors='coerce')
data['sodium'] = pd.to_numeric(data['sodium'], errors='coerce')
data['potassium'] = pd.to_numeric(data['potassium'], errors='coerce')
data['haemoglobin'] = pd.to_numeric(data['haemoglobin'], errors='coerce')
data['packed_cell_volume'] = pd.to_numeric(data['packed_cell_volume'], errors='coerce')
data['white_blood_cell_count'] = pd.to_numeric(data['white_blood_cell_count'], errors='coerce')
data['red_blood_cell_count'] = pd.to_numeric(data['red_blood_cell_count'], errors='coerce')

print(data.info())