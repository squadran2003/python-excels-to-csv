import sys
import pandas as pd
import os

print("Please Wait ........")
#get all excel files in a given directory
excel_names = os.listdir(sys.argv[1])
# check if its not a windows machine
if not os.name=='nt':
	excels = [pd.ExcelFile('{}/'.format(sys.argv[1])+'/'+name) for name in excel_names]
else:
	excels = [pd.ExcelFile('{}\\'.format(sys.argv[1])+'\\'+name) for name in excel_names]
frames = [x.parse(x.sheet_names[0],header=None,index_col=None) for x in excels]

combined_files = pd.concat(frames)
combined_files.to_csv(sys.argv[2],header=False, index=False)
print("Complete ......")



