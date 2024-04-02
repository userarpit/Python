# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 18:59:54 2023

@author: HP
"""

import seaborn as sns
df = sns.load_dataset('tips')
print(df)
#sns.stripplot(x="day",y="total_bill",data=df)
#sns.stripplot(x='petal_length',y='petal_width',data=df)
sns.swarmplot(x="day",y="total_bill",data=df)