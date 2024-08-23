# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 18:40:30 2024

@author: The ACJ
"""

import pandas as pd

# Read the CSV file (assuming the file is named "locations.csv")
df = pd.read_csv("telecom_customer_churn.csv")

# Combine latitude and longitude columns with a comma separating them
df["combined_coordinates"] = df["Latitude"].astype(str) + ", " + df["L   b ongitude"].astype(str)

# Save the updated DataFrame to a new CSV file (assuming the output file name is "combined_locations.csv")
df.to_csv("combined_locations.csv", index=False)

print (df["combined_coordinates"])
print("Combined coordinates saved to combined_locations.csv")
