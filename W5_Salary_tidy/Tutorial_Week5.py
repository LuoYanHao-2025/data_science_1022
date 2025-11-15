import pandas as pd
import numpy as np

file_path='wix1007/W5_Salary_tidy/data/salary.csv'
df=pd.read_csv(file_path)
df = df.rename(columns={
    'Unnamed: 0': 'UserID',
    'Timestamp': 'Timestamp',
    'How old are you?': 'Age',
    'What industry do you work in?': 'Industry', 
    'Job title': 'Job title',
    'If your job title needs additional context, please clarify here:': 'Job title context',
    'What is your annual salary? (You\'ll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)': 'Salary',
    'How much additional monetary compensation do you get, if any (for example, bonuses or overtime in an average year)? Please only include monetary compensation here, not the value of benefits.': 'Compensation',
    'Please indicate the currency': 'Currency',
    'If "Other," please indicate the currency here: ': 'Other currency',
    'If your income needs additional context, please provide it here:': 'Salary context',
    'What country do you work in?': 'Country',
    'If you\'re in the U.S., what state do you work in?': 'State',
    'What city do you work in?': 'City',
    'How many years of professional work experience do you have overall?': 'Overall years of exp',
    'How many years of professional work experience do you have in your field?': 'Years of exp in current job',
    'What is your highest level of education completed?': 'Education level',
    'What is your gender?': 'Gender',
    'What is your race? (Choose all that apply.)': 'Race'
})
# Why we do this? Since the original type is int64
df['Salary']=df['Salary'].replace(',', '', regex=True)
df['Salary']=df['Salary'].astype(int)
# df.info()

def missing_value_summary(df):
    '''
    Returns each column's info with the number of missing values

    Parameters:
    df(pd.DataFrame): Input dataframe

    Returns:
    pd.series: Column names with missing value counts
    '''
    missing_counts=df.isna().sum()
    return missing_counts[missing_counts>0]

#Find out columns with missing values
missing_values=missing_value_summary(df)
#print('--Columns and the number of missing values--')
#print(missing_values)

#Drop columns with to many missing values
df=df.drop(missing_values[missing_values>10000].index.tolist(), axis=1)
#df.info()


#Drop rows with NA. And check how many rows are dropped
rows_bef=len(df)
df=df.dropna(thresh=2)
rows_aft=len(df)
print(f"{rows_bef-rows_aft} rows are dropped.")

#Consistency check. Check unique values in each column.
#for col in df.columns:
#    print(f"{col} : {df[col].nunique()}")
#Education level and Gender may need further cleaning.
'''
print('\n--Unique values in Education level--')
print(df['Education level'].unique())
print('\n--Unique values in Gender--')
print(df['Gender'].unique())
Education level looks good. Gender needs cleaning. 
'''

# Clean Gender column
df['Gender']=df['Gender'].replace({
    'Woman': 'Female',
    'Man': 'Male',
    'Non-binary': 'Other',
    'Other or prefer not to answer': 'Other',
    'Prefer not to answer': 'Other'
})

#Impute missing value with mode.
from sklearn.impute import SimpleImputer
numerical_cols=df.select_dtypes(include=[np.number]).columns.tolist()
categorical_cols=df.select_dtypes(include=['object']).columns.tolist()
df[numerical_cols]=SimpleImputer(strategy='mean').fit_transform(df[numerical_cols])
df[categorical_cols]=SimpleImputer(strategy='most_frequent').fit_transform(df[categorical_cols])

'''Check the unique values after cleaning.
print('\n--Unique values in Gender--')
print(df['Gender'].unique())
'''

# Noise removal