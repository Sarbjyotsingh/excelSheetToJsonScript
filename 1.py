import pandas as pd
import numpy as np

df = pd.read_excel("ques.xlsx",encoding='utf8')

temp = open("tempt.json",'w')
temp.write('{ "data": '+df.to_json(orient='records',force_ascii=False)+"}")
temp.close()





