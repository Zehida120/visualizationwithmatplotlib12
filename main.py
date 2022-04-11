# Data visualization with matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# Scatter plot using axes method
pd_file=pd.read_csv('abs.csv')
pd_file.index=pd_file['country']
pd_file['year']=pd.to_datetime(pd_file['year'], infer_datetime_format=True)
plt.style.use('ggplot')
fig, ax=plt.subplots()
ax.scatter(pd_file.index, pd_file['living space'], color='black')
ax.set_xticklabels(pd_file['medals'], rotation=90, color='black')
ax.tick_params('x', color='black')
ax.set_yticklabels(pd_file['living space'], color='black')
ax.tick_params('y', color='black')
fig.savefig('scatter.png')
# Bar plot using axes method
fig, ax=plt.subplots()
ax.bar(pd_file.index, pd_file['zip'], color='black')
ax.set_xticklabels(pd_file.index, rotation=90)
plt.show()
# subplots using axes method
fig, ax=plt.subplots(2, 1)
ax[0].plot(pd_file.index, pd_file['living space'], color='black', linestyle='--', marker='o')
ax[0].set_xticklabels(pd_file.index, rotation=90)
ax[1].plot(pd_file.index, pd_file['zip'], color='black', linestyle='--', marker='o')
ax[1].set_xticklabels(pd_file.index, rotation=90)
fig.savefig('twinx.png')
# plot using twin axes
fig, ax=plt.subplots()
ax.plot(pd_file.index, pd_file['beds'], color='black', linestyle='--')
ax.set_xticklabels(pd_file.index, rotation=90)
ax2=ax.twinx()
ax2.plot(pd_file.index, pd_file['baths'], color='black', linestyle='--')
plt.show()
# boxplot using axes method
fig, ax=plt.subplots()
ax.boxplot([pd_file['living space'], pd_file['zip']])
ax.set_xlabel(['living space', 'zip'])
fig.savefig('box.png')
# Error bar using axes method
fig, ax=plt.subplots()
ax.errorbar(pd_file.index, pd_file['beds'], yerr=pd_file['zip'])
ax.set_xticklabels(pd_file.index, rotation=90)
fig.savefig('errorbar.png')
fig, ax=plt.subplots()
ax.bar(pd_file['medals'], pd_file['beds'], yerr=pd_file['baths'])
fig.savefig('bar.png')
# Histogram using axes method
fig, ax=plt.subplots()
ax.hist(pd_file['zip'], histtype='step', label='ZIP')
ax.set_xlabel('zip')
ax.set_ylabel('number of observations')
ax.legend()
fig.savefig('hist.png')

