import statistics;
import plotly.express as px;
import pandas as pd;

df = pd.read_csv('data.csv');
overall_data = df['quant_saved'].tolist();

# removing the outliers
Q1 = float(df['quant_saved'].quantile(0.25))
Q3 = float(df['quant_saved'].quantile(0.75));
IQR = float(Q3 - Q1)

lowerMajorityData = Q1 - 1.5 * IQR;
UpperMajorityData = Q3 + 1.5 * IQR;

new_data = [];
for i in overall_data:
    if i < UpperMajorityData:
        new_data.append(i);

new_fig = px.scatter(new_data);
new_fig.show();

print('Mean of new data => ' + str(statistics.mean(new_data)));
print('Median of new data => ' + str(statistics.median(new_data)));
print('Mode of new data => ' + str(statistics.mode(new_data)));


