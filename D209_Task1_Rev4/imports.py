# show python environment variables
import sys; import platform
print(sys.executable)
print('python version: {}'.format(platform.python_version()))
import os, sys
from IPython.display import Image

# import and configure pandas
import pandas as pd
pd.set_option('precision',3)
pd.set_option('max_columns',9)
pd.set_option('display.width', None)
print('pandas version: {}'.format(pd.__version__))

# import and configure scientific computing
import numpy as np
import scipy.stats as stats
import scipy
print('numpy version: {}'.format(np.__version__))
print('scipy version: {}'.format(scipy.__version__))

# import and configure sklearn
import sklearn
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import classification_report
from sklearn import metrics, tree
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import KFold, cross_val_score, train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor, _tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.pipeline import FeatureUnion, Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import export_graphviz as dt # decisiontree
from sklearn.base import BaseEstimator, TransformerMixin
print('sklearn version: {}'.format(sklearn.__version__))

# plotDecisionTree from Shmueli (2020) Data Mining for Business Analytics
from dmba import plotDecisionTree, classificationSummary, regressionSummary

# import and configure plotting packages
import graphviz
import matplotlib
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt
import matplotlib.patches as mpatches
plt.rc("font", size=14)

import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
print('matplotlib version: {}'.format(matplotlib.__version__))
print('seaborn version: {}'.format(sns.__version__))
print('graphviz version: {}'.format(graphviz.__version__))

# warnings
import warnings
