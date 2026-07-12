import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv(r'C:\Users\dharm\OneDrive\Desktop\Python Project\Customer Churn.csv')

print(df.head())

print(df.info())

# Replacing blank with zero as Tenure is Zero

df['TotalCharges'] = df['TotalCharges'].replace(' ','0')
df['TotalCharges'] = df['TotalCharges'].astype('float')

print(df.info())

print(df.isnull().sum().sum())

print(df.describe())

print(df.duplicated().sum())

print(df['customerID'].duplicated().sum())

# Converted o and 1 values of Senior Citizen to no and yes for better understanding

def convert (value):
    if value == 1 :
        return 'yes'
    else:
        return 'no'

df['SeniorCitizen'] = df['SeniorCitizen'].apply(convert)

print(df.head(20))


C = sns.countplot(x='Churn',data=df)
C.bar_label(C.containers[0])
plt.title('Count of customer by Churn',fontsize=20)
plt.show()

gb = df.groupby('Churn').agg({'Churn':'count'})
plt.pie(gb['Churn'],labels=gb.index,autopct='%1.2f%%')
plt.title('Percentage of churned Customers',fontsize=20)
plt.show()

# From this we got to know 26.54% of our customers churned out

# Reason Behind it 

C1 = sns.countplot(x = df['gender'],hue='Churn',data=df)
C1.bar_label(C1.containers[0])
plt.title('Churn By Gender',fontsize=20)
plt.show()

# This shows that Gender is not influencing for churn out

#### CHURN BY SENIOR CITIZEN

# Create a cross-tabulation
ct = pd.crosstab(df['SeniorCitizen'], df['Churn'])

# Plot stacked bar
ax = ct.plot(kind='bar', stacked=True, figsize=(6,5), color=['skyblue','salmon'])

# Add percentage labels
for i in range(len(ct)):
    total = ct.iloc[i].sum()
    cumulative = 0

    for j in range(len(ct.columns)):
        value = ct.iloc[i, j]
        percentage = value / total * 100

        ax.text(
            i,
            cumulative + value / 2,
            f'{percentage:.1f}%',
            ha='center',
            va='center',
            fontsize=11,
            color='black'
        )

        cumulative += value

plt.title("Churn by Senior Citizen", fontsize=16)
plt.xlabel("Senior Citizen")
plt.ylabel("Count")
plt.xticks([0,1], ['No', 'Yes'], rotation=0)
plt.legend(title="Churn")
plt.show()


C2 = sns.countplot(x = df['SeniorCitizen'],data=df)
C2.bar_label(C2.containers[0]) 
plt.title('Count of Customer by Age-Group',fontsize=20) 
plt.show()

# This shows that senior citizen are less in no but churn in comparatively higher

sns.histplot(x='tenure',data=df,bins=72,hue='Churn')
plt.show()

# This shows that people using the service for more than 2 months have stayed

C3 = sns.countplot(x = 'Contract',data=df,hue='Churn')
C3.bar_label(C3.containers[0]) 
plt.title('Count of Customer by Contract',fontsize=20) 
plt.show()

# From this we can conclude is the customers having month to month basis contract are churning out 

print(df.columns.values)

cols = ['PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies']

fig, axes = plt.subplots(3, 3, figsize=(15, 12))
axes = axes.flatten()

for i, col in enumerate(cols):
    sns.countplot(data=df, x=col, ax=axes[i], palette='Set2',hue='Churn')

    # Add count labels
    for container in axes[i].containers:
        
        axes[i].bar_label(container,padding=3)
        
        ymax = axes[i].get_ylim()[1]
        axes[i].set_ylim(0, ymax * 1.10)

plt.tight_layout()
plt.show()

#  From this we understand from services provided fibre optic , multiplelines,Tech support
#  are few those parameters leading to churn out

C4 = sns.countplot(x = 'PaymentMethod',data=df,hue='Churn')
C4.bar_label(C4.containers[0]) 
plt.title('Count of Customer churned by Payment Method',fontsize=15) 
plt.show()