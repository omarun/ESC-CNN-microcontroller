
import sys
import pandas
import numpy
import yaml

df = pandas.read_csv('results/results.csv')
print(df)

width_variations = df.nickname.str.startswith('Stride-DS-5x5-')
df = df[width_variations != True]

table = pandas.DataFrame({
    'Model': df.nickname,
    'CPU (%)': (df.utilization * 100).astype(int),
    'Accuracy': (df.test_acc_mean * 100).round(1),
    'FG Accuracy': (df.foreground_test_acc_mean * 100).round(1),
    'BG Accuracy': (df.background_test_acc_mean * 100).round(1),
}, index=df.index)

out = table.to_latex(header=True, index=False)
print(out)

outpath = sys.argv[1] 
with open(outpath, 'w') as f:
    f.write(out)
