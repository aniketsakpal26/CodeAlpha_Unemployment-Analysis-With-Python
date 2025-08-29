import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

unemployment = pd.read_csv("Unemployment_in_India.csv")

print(unemployment.head())
print(unemployment.info())
unemployment.dropna(inplace=True)

unemployment.rename(columns={
    'Region': 'State',
    'Date': 'Date',
    'Estimated Unemployment Rate (%)': 'UnemploymentRate',
    'Estimated Employed': 'Employed',
    'Estimated Labour Participation Rate (%)': 'LabourParticipationRate'
}, inplace=True)

unemployment['Date'] = pd.to_datetime(unemployment['Date'])

state_avg = unemployment.groupby('State')['UnemploymentRate'].mean().sort_values(ascending=False)
plt.figure(figsize=(12,6))
sns.barplot(x=state_avg.values, y=state_avg.index)
plt.title("Average Unemployment Rate by State")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("State")
plt.show()

plt.figure(figsize=(14,6))
sns.lineplot(data=unemployment, x='Date', y='UnemploymentRate', hue='State', legend=False)
plt.title("Unemployment Rate Trends in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

covid_period = unemployment[unemployment['Date'] >= '2020-03-01']
plt.figure(figsize=(12,6))
sns.lineplot(data=covid_period, x='Date', y='UnemploymentRate')
plt.title("Impact of Covid-19 on Unemployment in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()
