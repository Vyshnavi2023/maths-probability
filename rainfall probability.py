#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd


# In[26]:


df=pd.read_csv("/home/user/Downloads/nuzvid_eluru_rainfall_data_clean.csv")
df


# In[27]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[28]:


# Calculate probability of rainfall today
rainy_years = df[df['Rain_mm'] > 0].shape[0]
total_years = df.shape[0]
probability_rain_today = rainy_years / total_years

print(f"Probability of rainfall today based on past data: {probability_rain_today:.2f}")





# In[29]:


# Pie chart of probability
probability_no_rain = 1 - probability_rain_today

plt.figure(figsize=(6, 6))
plt.pie([probability_rain_today, probability_no_rain],
        labels=['Rain', 'No Rain'],
        autopct='%1.1f%%',
        colors=['green', 'gray'],
        startangle=140)
plt.title('Probability of Rainfall Today')
plt.tight_layout()
plt.show()


# In[30]:


# Calculate average rainfall
average_rainfall = df['Rain_mm'].mean()


# In[31]:


import matplotlib.pyplot as plt

# Line Plot with Average Rainfall Line
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Rain_mm'], marker='o', color='blue', label='Rainfall (mm)')
plt.axhline(average_rainfall, color='red', linestyle='--', label=f'Avg Rainfall = {average_rainfall:.1f} mm')

# Annotate above and below average years
for index, row in df.iterrows():
    if row['Rain_mm'] > average_rainfall:
        plt.text(row['Year'], row['Rain_mm'] + 1, f"{int(row['Rain_mm'])}", ha='center', color='green')
    elif row['Rain_mm'] < average_rainfall:
        plt.text(row['Year'], row['Rain_mm'] + 1, f"{int(row['Rain_mm'])}", ha='center', color='brown')

plt.title('Rainfall Over the Years with Average Line (Line Plot)')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


# In[32]:


# Bar Plot with Average Rainfall Line
plt.figure(figsize=(10, 6))
plt.bar(df['Year'], df['Rain_mm'], color='skyblue')
plt.axhline(average_rainfall, color='red', linestyle='--', label=f'Avg Rainfall = {average_rainfall:.1f} mm')

# Annotate bars
for index, row in df.iterrows():
    plt.text(row['Year'], row['Rain_mm'] + 1, f"{int(row['Rain_mm'])}", ha='center', va='bottom')

plt.title('Rainfall Over the Years with Average Line (Bar Plot)')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[33]:


df=pd.read_csv("/home/user/Downloads/nuzvidu_processed_rainfall (1).csv")
df


# In[34]:


df.shape


# In[35]:


import datetime

today = datetime.date.today()
today_month = today.month
today_day = today.day

today_data = df[(df['month'] == today_month) & (df['day_of_year'] % 365 == today.timetuple().tm_yday)]

rain_probability = today_data['rainfall_occurred'].mean()
print(f"Probability of rainfall on {today.strftime('%B %d')} is: {rain_probability:.2f}")


# In[ ]:





# In[ ]:





# In[13]:


import matplotlib.pyplot as plt

# Group by year and calculate total rainfall
yearly_rainfall = df.groupby('year')['precipitation_mm'].sum()

# Calculate average rainfall
avg_rainfall = yearly_rainfall.mean()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(yearly_rainfall.index, yearly_rainfall.values, marker='o', label='Yearly Rainfall (mm)')
plt.axhline(avg_rainfall, color='red', linestyle='--', label=f'Average Rainfall ({avg_rainfall:.2f} mm)')
plt.title('Total Rainfall by Year')
plt.xlabel('Year')
plt.ylabel('Rainfall (mm)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:





# In[37]:


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Load the dataset
df = pd.read_csv("/home/user/Downloads/nuzvidu_processed_rainfall (1).csv")

# Convert 'date' column to datetime
df['date'] = pd.to_datetime(df['date'])

# Get today's date and the next 7 days
today = datetime.today().date()
next_seven_days = [today + timedelta(days=i) for i in range(7)]

# Extract (month, day) for filtering
next_seven_md = [(d.month, d.day) for d in next_seven_days]

# List to store probabilities
weekly_probabilities = []

# Calculate probability of rainfall for each of the next 7 days
for month, day in next_seven_md:
    day_data = df[(df['month'] == month) & (df['date'].dt.day == day)]
    if not day_data.empty:
        prob = day_data['rainfall_occurred'].mean()
    else:
        prob = None  # No historical data
    weekly_probabilities.append(prob)

# Create DataFrame for plotting
prob_df = pd.DataFrame({
    'Date': [d.strftime('%Y-%m-%d') for d in next_seven_days],
    'Rainfall_Probability': weekly_probabilities
})

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(prob_df['Date'], prob_df['Rainfall_Probability'], marker='o', linestyle='-', color='blue')
plt.title('Rainfall Probability Forecast (Next 7 Days)')
plt.xlabel('Date')
plt.ylabel('Rainfall Probability')
plt.ylim(0, 1)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# | Date       | Rainfall Probability |
# | ---------- | -------------------- |
# | 2025-07-22 | 0.84 (84%)           |
# | 2025-07-23 | 0.88 (88%)           |
# | 2025-07-24 | 0.88 (88%)           |
# | 2025-07-25 | 0.84 (84%)           |
# | 2025-07-26 | 0.92 (92%)           |
# | 2025-07-27 | 0.80 (80%)           |
# | 2025-07-28 | 0.84 (84%)           |
# 

# In[ ]:




