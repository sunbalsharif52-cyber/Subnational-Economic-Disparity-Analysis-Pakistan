import numpy as np
import pandas as pd

# Set random seed for statistical consistency
np.random.seed(101)

# Real-world district distribution approximation for Pakistan
provinces = {
    "Punjab": 42,
    "Sindh": 30,
    "KPK": 36,
    "Balochistan": 36,
    "Gilgit-Baltistan": 10,
}

district_names = []
province_labels = []

for prov, count in provinces.items():
    for i in range(1, count + 1):
        district_names.append(f"{prov}_District_{i}")
        province_labels.append(prov)

total_districts = len(district_names)  # 154 Districts

# Simulating structural multi-variable socioeconomic data
# Based on national economic ranges
education_index = np.round(np.random.uniform(0.35, 0.85, total_districts), 2)
healthcare_index = np.round(
    education_index * 0.85 + np.random.uniform(0.1, 0.25, total_districts), 2
)
population_millions = np.round(
    np.random.exponential(scale=1.5, size=total_districts) + 0.3, 2
)

# Generating Income Index using human capital theory (with variance)
income_index_gdp = np.round(
    0.4 * education_index
    + 0.35 * healthcare_index
    + 0.05 * np.log(population_millions)
    + np.random.normal(0, 0.05, total_districts),
    2,
)

# Creating Dataframe
dataset_dict = {
    "District_ID": range(1, total_districts + 1),
    "Province": province_labels,
    "District_Name": district_names,
    "Population_Millions": population_millions,
    "Education_Index": education_index,
    "Healthcare_Index": healthcare_index,
    "Income_Index_GDP": income_index_gdp,
}

df_pro = pd.DataFrame(dataset_dict)

# Exporting to Excel
file_name = "Pakistan_SubNational_Economic_Data.xlsx"
df_pro.to_excel(file_name, index=False)

print(
    f"Success! Generated a professional-grade dataset with {total_districts} rows."
)
print(f"Saved file as: {file_name}")