import os
import pandas as pd

def dateiType(fileName):
    fileType = ' '.join(fileName.split('_')[1:-2])
    return(fileType)

def spaltenNamen(fileName):
    df = pd.read_csv(fileName)
    colCount = df.count()
    out = colCount.to_dict()
    return(out)

root = '/media/sf_Haddie/Documents/20160316.LearnPython/USB/Learn-Python/gmw/'
list = []
files = os.listdir(root)
textFiles = [f for f in files if f.endswith('.txt')]
for f in textFiles:
    out1 = dateiType(f)
    out2 = spaltenNamen(os.path.join(root, f))
    list.append([f, out1, out2])


finalDF = pd.DataFrame(list, columns=['file','type','info'])


finalDF.to_csv(os.path.join(root, '20160415_Aufgabe2.csv'))


