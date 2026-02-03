import pandas as pd
df=pd.read_csv('https://raw.githubusercontent.com/ArchanaInsights/Datasets/main/marketing_campaign.csv')
print(df)
print(df.columns)
print(df.shape)
print(df.head())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df['Campaign_ID'].nunique())
pd.concat([df["Location"],df['Customer_Segment']]).unique()
print(df['Campaign_Type'].value_counts())
print(df['Channel_Used'].value_counts())


##EDA Explorotary data analysis Campaign analysis
##Acqusition cost analysis

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.figure(figsize=(10,5))
sns.scatterplot(x='Acquisition_Cost',y='ROI',data=df)
plt.title('Cost',fontsize='10',color='blue')
plt.show()

##campaign type analysis 
plt.figure(figsize=(10,5))
sns.barplot(x='Channel_Used',y='Conversion_Rate',data=df,hue='Campaign_Type',estimator='mean')
plt.title('channel',fontsize='10',color='blue')
plt.ylim(0,10)
plt.show()

##score Analysis

plt.figure(figsize=(10,5))
sns.boxplot(x='Engagement_Score',y='Campaign_Type',data=df,hue='Campaign_Type')
plt.title('score',fontsize='10',color='blue')
plt.xticks(rotation=45)
plt.show()

##profit analysis
plt.figure(figsize=(10,5))
sns.barplot(x='Company',y='ROI',estimator='mean',data=df,hue='Campaign_Type')
plt.title('profit',fontsize='10',color='blue')
plt.show()

#correlation
correlation=df[['Engagement_Score','Conversion_Rate']].corr()
print(correlation)
sns.heatmap(correlation,annot=True,cmap='coolwarm')

##Customer Segmentation analysis

plt.figure(figsize=(10,5))
plt.title("Target Audience",color='green',fontsize=20)
sns.countplot(x="Target_Audience",data=df,color='blue')
plt.show()

#customer highest conversation rate
plt.figure(figsize=(10,5))
plt.ylim(0,10)
x=sns.barplot(x='Customer_Segment',y='Conversion_Rate',color='blue',data=df,estimator='max',hue='Language')
for container in x.containers:
  x.bar_label(container,fmt='%.2f')
plt.title("Customer highest Segment",color='yellow',fontsize=18)
plt.show()
#Accusition cost by Customer segment
plt.figure(figsize=(12,5))
sns.boxplot(x='Acquisition_Cost',y='Customer_Segment',color='yellow',data=df,hue='Channel_Used')
plt.title('Accusition cost',color='black',fontsize=10)
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,5))
plt.xticks(rotation=45)
x=sns.barplot(x='Conversion_Rate',y='Language',color='blue',data=df,estimator='max',hue='Campaign_Type')
for container in x.containers:
  x.bar_label(container,fmt='%.2f')
plt.title("Customer segment average",color='yellow',fontsize=18)
plt.show()

#Channel Effecticness
plt.figure(figsize=(15,5))
plt.xticks(rotation=45)
plt.title("Customer effect",color='yellow',fontsize=18)
sns.barplot(x='Channel_Used',y='Engagement_Score',data=df,hue='Campaign_Type')
plt.show()

pie=df.groupby('Channel_Used')['ROI'].sum()
plt.title('pie char')
plt.pie(pie,labels=(pie.index),autopct='%1.2f%%',shadow=True)
plt.show()

#Relationships
plt.figure(figsize=(15,5))
plt.title("Relationship",color='yellow',fontsize=18)
sns.scatterplot(x='Clicks',y='Impressions',data=df,hue='Channel_Used')
plt.show()

#kernel density estimation
plt.figure(figsize=(15,5))
plt.title("Duration",color='yellow',fontsize=18)
sns.histplot(x='Duration',data=df,kde=True)
plt.show()

plt.figure(figsize=(15,5))
plt.title("converation size",color='yellow',fontsize=18)
sns.lineplot(x='Date',y='Conversion_Rate',data=df,hue='Company')
plt.show()

plt.figure(figsize=(6,6))
plt.title("enga",color='yellow',fontsize=18)
sns.lineplot(x='Date',y='Engagement_Score',data=df,hue='Date',linestyle='--',marker='.')
plt.show()

#geographic Analysis
plt.figure(figsize=(12,5))
plt.xticks(rotation=45)
x=sns.barplot(x='Location',y='Acquisition_Cost',color='blue',data=df,estimator='max',hue='Location')
for container in x.containers:
  x.bar_label(container,fmt='%.2f')
plt.title("accqusition",color='yellow',fontsize=18)
plt.show()

plt.figure(figsize=(12,5))
plt.xticks(rotation=45)
x=sns.barplot(x='Conversion_Rate',y='Location',color='blue',data=df,hue='Location')
for container in x.containers:
  x.bar_label(container,fmt='%.2f')
plt.title("conversion rate",color='yellow',fontsize=18)
plt.show()

proportion=df.groupby('Location')['ROI'].sum()
plt.figure(figsize=(12,5)) 
plt.title('proportion',color='green')
plt.pie(proportion,labels=proportion.index,autopct='%1.2f%%',shadow=True)
plt.show()
