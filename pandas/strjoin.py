# importing pandas module 
import pandas as pd 
	
# reading csv file from url 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 

# dropping null value columns to avoid errors 
data.dropna(inplace = True) 
	
# splitting string and overwriting 
data["Team"]= data["Team"].str.split("t") 

# joining with "_" 
data["Team"]= data["Team"].str.join("_") 

# display 
print(data)
