

# creting the  csv fie of question for each survey

import csv
pathCSV = "s.csv"
with open(pathCSV, newline='\n') as f:
    reader = csv.reader(f)
    dataAll = list(reader)[0]
    
l=dataAll[1:]

for i in l:     
    name = i +".csv"
    print(name)
    import pandas as pd
    df = pd.DataFrame(list())
    df.to_csv(name)
