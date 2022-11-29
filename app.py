from shiny import App, render, ui
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns
from pathlib import Path 

data = pd.read_csv(Path(__file__).parent / "ds_salaries.csv")



#Mean of 'salary_in_usd' based on 'company_size'
salary_mean = data.groupby("company_size")["salary_in_usd"].mean() 
#print(salary_mean)

counts = data["experience_level"].value_counts().sort_index() 
#print(counts)

#Setting up 1x2 grid for plots
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

#Themes
sns.set_palette("spring")
sns.set_style("whitegrid")

#First plot
sns.barplot(ax=axes[0], x = salary_mean.index, y = salary_mean) 
axes[0].set(xlabel='', ylabel='Average Salary in USD', title="Company Size & Salary")
axes[0].set_xticklabels(["Large Company", "Medium Company", "Small Company"], rotation=0)

#Second plot (using Pandas dataframe)
df = (data
        .groupby("company_size")["experience_level"]
        .value_counts(normalize=True)
        .mul(100)
        .round(2)
        .unstack())

df.plot.bar(stacked = True,
            ax = axes[1],
            width = 0.3,
            edgecolor = "black")

# Adding bar labels
for c in axes[1].containers:
    labels = [str(round(v.get_height(), 2)) + "%" if v.get_height() > 0 else '' for v in c]
    axes[1].bar_label(c,
                    label_type='center',
                    labels = labels,
                    size = 8)

axes[1].set(xlabel='',ylabel='Work Experience %', title="Company Size & Work Experience")
axes[1].set_xticklabels(["Large Company", "Medium Company", "Small Company"], rotation=0)

axes[1].legend(["Entry", "Executive", "Mid", "Senior"], title="Work Experience")
axes[1].legend_.set_bbox_to_anchor([1,1])
#plt.show()

        
