import numpy as np
from scipy.stats import binom, poisson
import matplotlib.pyplot as plt

import distfit
# print(distfit.__version__)
# print(dir(distfit))

from distfit import distfit
X = np.random.normal(163, 10, 1000)
dfit = distfit()
dfit.fit_transform(X, n_boots=0)
dfit.plot_summary()


# %%

from distfit import distfit
X = np.random.normal(6, 1, 500)
dfit = distfit()
dfit.fit_transform(X)

X2 = np.random.normal(6, 0.9, 500)
X2 = np.hstack([[7]*50, X2])
dfit2 = distfit()
dfit2.fit_transform(X2)

fig, ax = plt.subplots(1,2, figsize=(25,10))
dfit.plot(title='without swear words', ax=ax[0])
dfit2.plot(title='with swear words', ax=ax[1])

import scipy.stats as st
st.kstest(X, X2)

# %% lineplot
from distfit import distfit
X = np.random.normal(163, 10, 1000)
dfit = distfit(multtest='test')
dfit.fit_transform(X, n_boots=10)
dfit.plot_summary()
dfit.plot_summary(ylim=[0, 0.0002])

dfit.lineplot(X)

y = [135, 145, 150, 160, 180, 185, 200]
results = dfit.predict(y, multtest='holm')
dfit.lineplot(X)

# %% Import example

from distfit import distfit
dfit = distfit()
df = dfit.import_example(data='gas_spot_price')
dfit.lineplot(df, xlabel='Years', ylabel='Natural gas spot price', grid=True)
plt.show()



# %% CDF plot
from distfit import distfit

# Random Exponential data
# X = np.random.exponential(0.5, 10000)
# X = np.random.uniform(0, 1000, 10000)
X = np.random.normal(163, 10, 10000)
# Initialize with bootstrapping
dfit = distfit(n_boots=10)
# Fit
results = dfit.fit_transform(X)
# Results
dfit.summary[['name', 'score', 'bootstrap_score', 'bootstrap_pass']]
# Plot
dfit.plot_summary()


out = dfit.bootstrap(X, n_boots=10, n_top=None)
dfit.plot_summary()

fig, ax = dfit.plot(chart='PDF', n_top=5, cmap='Set2');
dfit.plot(chart='CDF', n_top=10, cmap='Set2', ax=ax);
dfit.plot_cdf()


# %%
from distfit import distfit
# Set parameters for the test-case
n = 8
p = 0.5
# Generate 10000 samples of the distribution of (n, p)
X = binom(n, p).rvs(10000)

# Initialize distfit for discrete distribution for which the binomial distribution is used. 
dfit = distfit(method='discrete')
# Run distfit to and determine whether we can find the parameters from the data.
results = dfit.fit_transform(X)
# Get the model and best fitted parameters.

y = [0, 1, 10, 11, 12]

results = dfit.predict(y)
dfit.plot(chart='PDF')
dfit.plot(chart='PDF', pdf_properties=None)
dfit.plot(chart='CDF', n_top=5)
dfit.plot(chart='CDF', pdf_properties=None, n_top=2)
dfit.plot_cdf()

# %% QQ plot
from distfit import distfit
dfit = distfit(verbose=20)

# Random Exponential data
# X = np.random.exponential(0.5, 10000)
# X = np.random.uniform(0, 1000, 10000)
X = np.random.normal(0, 1, 10000)
dfit = distfit(distr='popular')
# Fit
dfit.fit_transform(X)
# QQplot
dfit.qqplot(X)
dfit.qqplot(X, n_top=11, cmap='Set1')

dfit.plot(chart='PDF')
dfit.plot(chart='PDF', pdf_properties=None)
dfit.plot(chart='PDF', pdf_properties=None, n_top=10)
dfit.plot(chart='CDF', n_top=10)
dfit.plot(chart='CDF', pdf_properties=None, n_top=10)


# fig, ax = dfit.plot(chart='CDF', n_top=10);
# dfit.plot(chart='PDF', n_top=10, fig=fig, ax=ax);
# dfit.qqplot(X, n_top=10, fig=fig, ax=ax);

# %% CDF plot
from distfit import distfit
dfit = distfit(verbose=20)

# Random Exponential data
X = np.random.exponential(0.5, 10000)
# X = np.random.uniform(0, 1000, 10000)
# X = np.random.normal(0, 1, 1000)
dfit = distfit(distr='popular')
# Fit and plot
dfit.fit_transform(X)
# dfit.plot_cdf(n_top=10);
fig, ax = dfit.plot(chart='PDF', n_top=5, cmap='Set2');
dfit.plot(chart='CDF', n_top=10, cmap='Set2', ax=ax);
# dfit.plot_cdf()
dfit.plot_summary(n_top=10);

import scipy.stats as stats
import pylab 
# Calculate quantiles for a probability plot, and optionally show the plot.
# Generates a probability plot of sample data against the quantiles of a specified theoretical distribution.
# probplot optionally calculates a best-fit line for the data and plots the results using Matplotlib or a given plot function.
fig, ax = plt.subplots(figsize=(15,10))
out = stats.probplot(X, dist=dfit.model['name'], sparams=dfit.model['params'], plot=ax)
ax.grid(True)
    

# %%
from distfit import distfit
# Set parameters for the test-case
n = 8
p = 0.5
# Generate 10000 samples of the distribution of (n, p)
X = binom(n, p).rvs(10000)

# Initialize distfit for discrete distribution for which the binomial distribution is used. 
dfit = distfit(method='discrete')
# Run distfit to and determine whether we can find the parameters from the data.
results = dfit.fit_transform(X)
# Get the model and best fitted parameters.

y = [0, 1, 10, 11, 12]

results = dfit.predict(y)
dfit.plot(fontsize=14)

# %%
from distfit import distfit
dfit = distfit()
d = dfit.get_distributions('popular')

X = np.random.normal(0, 1, 1000)
bins, density = dfit.density(X)
plt.figure(); plt.plot(bins, density)

# %% Figure 1

# Load library
from distfit import distfit

# Random Exponential data
X = np.random.poisson(10, 10000)
X = np.random.uniform(0, 1000, 10000)
# initialize with uniform distribution
dfit = distfit(distr='uniform')
# Fit and plot
results = dfit.fit_transform(X, verbose='warning')
dfit.plot(grid=False, cii_properties=None);

# Random exponential data
X = np.random.exponential(0.5, 10000)
# initialize with exponential distribution
dfit = distfit(distr='expon')
# Fit and plot
results = dfit.fit_transform(X, verbose='debug')
dfit.plot(grid=False, cii_properties=None, verbose=10);

# Random normal distribution
X = np.random.normal(0, 2, 10000)
dfit = distfit(distr='norm')
# Fit and plot
results = dfit.fit_transform(X)
dfit.plot(figsize=(15, 12), grid=False)

# Random bimodal distribution
X1 = list(np.random.normal(10, 3, 10000))
X2 = list(np.random.normal(0, 2, 2000))
X = np.array(X1+X2)
dfit = distfit()
# Fit and plot
results = dfit.fit_transform(X)
dfit.plot(figsize=(15, 12), grid=False, cii_properties=None, pdf_properties=None)

# %% Figure 2
# Random normal distribution
X = np.random.normal(2, 4, 10000)
y = [-8, -2, 1, 3, 5, 15]
dfit = distfit(distr='norm')
# dfit = distfit(method='quantile')
# Fit and plot
dfit.fit_transform(X);
dfit.model

dfit.predict(y);
dfit.plot(figsize=(15, 12), grid=True);
dfit.plot_summary()

# Create random normal data with mean=2 and std=4
X = np.random.normal(2, 4, 10000)
# Load library
from distfit import distfit
# Initialize using the quantile or percentile approach.
model = distfit(method='quantile') # percentile
# Fit model on input data X and detect the best theoretical distribution.
model.fit_transform(X);
# Make prediction for new data points.
y = [-8, -2, 1, 3, 5, 15]
model.predict(y)
# Plot the results
model.plot()


# Random discrete data
X = binom(8, 0.5).rvs(1000)
dfit = distfit(method='discrete', f=1.5, weighted=True, stats='wasserstein')
dfit = distfit(method='discrete')
# Fit and plot
model = dfit.fit_transform(X, verbose=3)
dfit.plot(figsize=(15, 12), grid=True)

# %% Quantile approach
from distfit import distfit
import numpy as np

X1 = list(np.random.normal(10, 3, 10000))
X2 = list(np.random.normal(0, 2, 2000))
X = np.array(X1+X2)
y = [3,4,5,6,10,11,12,18,20]

# Initialize
# dfit = distfit(method='percentile', alpha=0.05, todf=False)
# dfit = distfit(method='quantile', alpha=0.05, todf=False)
dfit = distfit(method='parametric', alpha=0.05, todf=False)
dfit.fit_transform(X);
dfit.plot(figsize=(15, 12), cii_properties=None, pdf_properties=None, grid=False)

# Make prediction
dfit.predict(y);
dfit.plot();
dfit.plot_summary();


# %% Multiple distributions as input
from distfit import distfit
X = np.random.normal(0, 2, 10000)
y = [-8, -6, 0, 1, 2, 3, 4, 5, 6]
dfit = distfit(stats='RSS', distr=['norm','expon'])
results = dfit.fit_transform(X)
dfit.plot(cii_properties={'size': 50})

results = dfit.predict(y, alpha=0.01)
dfit.plot(cii_properties={'size': 20, 'marker': 'x', 'linewidth':2})

print(dfit.model)


from distfit import distfit
X = binom(8, 0.5).rvs(1000)
dfit = distfit(method='discrete', f=1.5, weighted=True, stats='wasserstein')
model = dfit.fit_transform(X, verbose=3)
dfit.plot(figsize=(15, 12), grid=True)


from distfit import distfit
X = np.random.uniform(0, 1000, 10000)
dfit = distfit(bound=None, distr='uniform')
results = dfit.fit_transform(X)
dfit.plot(figsize=(15, 12), grid=False)

from distfit import distfit
X = np.random.exponential(0.5, 10000)
dfit = distfit(bound=None, distr='expon')
results = dfit.fit_transform(X)
dfit.plot(figsize=(15, 12), grid=False)
# dfit.plot_summary()

from distfit import distfit
X = np.random.normal(0, 2, 10000)
dfit = distfit(bound=None, distr='norm')
results = dfit.fit_transform(X)
dfit.plot(figsize=(15, 12), grid=False)

dfit.plot(bar_properties={'color': 'r', 'label': None}, pdf_properties={'color': 'k'}, emp_properties={'color': 'k', 'linewidth': 3})
dfit.plot(bar_properties=None, pdf_properties=None)
dfit.plot(bar_properties={}, pdf_properties=None, emp_properties={})
dfit.plot(bar_properties={}, pdf_properties={}, emp_properties=None)


# %% K distributions as input
import scipy.stats as st
from distfit import distfit
X = np.random.normal(0, 2, 1000)
dfit = distfit(stats='ks', distr=['k','t','expon', 'gamma', 'lognorm'], bins=50)
results = dfit.fit_transform(X, verbose=0)

dfit.plot()
dfit.plot_summary(fontsize=10)

# %% Multiple distributions as input
import scipy.stats as st
from distfit import distfit
X = np.random.normal(0, 2, 1000)
y = [-8, -6, 0, 1, 2, 3, 4, 5, 6]
dfit = distfit(stats='ks', distr=['expon', 't', 'gamma', 'lognorm'])
# dfit = distfit(stats='ks', distr=['lognorm'])
results = dfit.fit_transform(X)

# dfit.plot()
# dfit.plot_summary()

# results = dfit.predict(y, alpha=0.01)

print(dfit.model)
# dist_t = st.t(dfit.model['arg'], loc=dfit.model['loc'], scale=dfit.model['scale'])
# dist_t = st.t(dfit.model['params'])

# dfit.predict(y)['P']
# dist_t.cdf(y)
# dfit.model['model'].cdf(y)

# fit dist to data
params = st.t.fit(X)
# Separate parts of parameters
arg = params[:-2]
loc = params[-2]
scale = params[-1]

params==dfit.model['params']

# Calculate fitted PDF and error with fit in distribution
# pdf = st.t.pdf(X, loc=loc, scale=scale, *arg)

# %% Multiple distributions as input
from distfit import distfit
import scipy.stats as st
import pandas as pd

ranking = []
b_pareto = [0.75, 1, 2, 3, 4, 5]
size = [100, 1000, 10000]
bins = [50, 100, 200]
stats = ['RSS', 'wasserstein']

for stat in stats:
    for bs in bins:
        for b in b_pareto:
            for s in size:
                X = st.pareto.rvs(b, size=s)
                dfit = distfit(todf=True, stats=stat, bins=bs)
                dfit.fit_transform(X)
                r = np.where(dfit.summary['name']=='pareto')[0][0]
                ranking.append([r, b, s, bs, stat])

df = pd.DataFrame(ranking, columns=['rank','b','sample size', 'bins', 'stats'])

np.sum(df['rank']==0) / df.shape[0]
np.sum(df['rank']<=1) / df.shape[0]
np.sum(df['rank']<=2) / df.shape[0]
np.sum(df['rank']<=3) / df.shape[0]

# Other distr. have better scores under these conditions
df.loc[df['rank']>=3, :]

dfit.plot_summary()
# results['model']

# %% Multiple distributions as input
from distfit import distfit
X = np.random.normal(0, 2, 10000)
y = [-8, -6, 0, 1, 2, 3, 4, 5, 6]
dfit = distfit(stats='RSS', distr=['norm','expon'])
results = dfit.fit_transform(X)
dfit.plot()

results = dfit.predict(y, alpha=0.01)
dfit.plot()

print(dfit.model)

# %% Discrete example
from distfit import distfit
from scipy.stats import binom
# Generate random numbers
X = binom(8, 0.5).rvs(1000)

dfit = distfit(method='discrete', f=1.5, weighted=True, stats='wasserstein')
model = dfit.fit_transform(X, verbose=3)
dfit.plot()

# Make prediction
results = dfit.predict([0, 1, 3, 4, 10, 11, 12])
dfit.plot()

# Generate samples
Xgen = dfit.generate(n=1000)
dfit.fit_transform(Xgen)
results = dfit.predict([0, 1, 10, 11, 12])
dfit.plot()

# %%
from distfit import distfit
X = np.random.normal(0, 2, 10000)
y = [-8, -6, 0, 1, 2, 3, 4, 5, 6]
dfit = distfit(stats='RSS', distr='full')
# dfit = distfit(stats='wasserstein')
# dfit = distfit(stats='energy')
# dfit = distfit(stats='ks')

# Fit
dfit.fit_transform(X)
dfit.predict(y)

dfit.plot_summary()
dfit.plot()

# Generate samples
Xgen = dfit.generate(n=10000)
dfit.fit_transform(Xgen)

# Plot
dfit.plot_summary()
dfit.plot()

# %%
from distfit import distfit
X = np.random.normal(0, 2, 5000)
y = [-8,-6,0,1,2,3,4,5,6]
dfit = distfit(distr='loggamma')
dfit.fit_transform(X)
dfit.plot()

# %%
from distfit import distfit
X = np.random.normal(0, 2, 5000)
y = [-8,-6,0,1,2,3,4,5,6]

dfit = distfit(distr='popular', todf=False)
model = dfit.fit_transform(X)
dfit.plot()

dfit = distfit(distr='popular', todf=True)
dfit.fit_transform(X)
dfit.plot()

# Make prediction
results = dfit.predict(y)

# plot
dfit.plot()
dfit.plot_summary()

# Save
dfit.save(filepath='c:\\temp\\model.pkl', overwrite=True)
# Load
dfit.load(filepath='c:\\temp\\model.pkl')

# Store entire object


# %%
X = np.random.normal(0, 2, 100)
model = distfit(smooth=10)
model.fit_transform(X)
model.plot()

# %%
# Create random data with varying number of samples

#%%
# Initialize model
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
samples = np.arange(250, 20000, 250)
smooth_window=[None,2,4,6,8,10]
plt.figure(figsize=(15,10))

for smooth in tqdm(smooth_window):
    dfit = distfit(distr='norm', smooth=smooth)
    # Estimate paramters for the number of samples
    out = []
    for s in samples:
        X = np.random.normal(0, 2, s)
        dfit.fit_transform(X, verbose=0)
        # out.append([dfit.model['RSS'], dfit.model['name'], np.where(dfit.summary['name']=='norm')[0][0], s])
        out.append([dfit.model['scale'], dfit.model['name'], s])

    df=pd.DataFrame(out, columns=['mu','name','samples'])
    ax=df['mu'].plot(grid=True, label='smooth: '+str(smooth) + ' - ' + str(df['mu'].mean()))

ax.set_xlabel('Nr.Samples')
ax.set_ylabel('mu')
ax.set_xticks(np.arange(0,len(samples)))
ax.set_xticklabels(samples.astype(str), rotation = 90)
# ax.set_ylim([0, 0.02])
# ax.set_ylim([1.9, 2.1])
ax.legend()

# ax=df['std'].plot(grid=True)
# ax.set_xlabel('Nr.Samples')
# ax.set_ylabel('std')
# ax.set_xticks(np.arange(0,len(samples)))
# ax.set_xticklabels(samples.astype(str))

#%%
# Initialize model
import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
samples = np.arange(250, 20000, 250)
smooth_window=[None, 2,4,6,8,10]
plt.figure(figsize=(15,10))

for smooth in tqdm(smooth_window):
    dfit = distfit(distr='uniform', smooth=smooth)
    # dfit = distfit(smooth=smooth)
    # Estimate paramters for the number of samples
    out = []
    for s in samples:
        X = np.random.randint(0, 100, s)
        dfit.fit_transform(X, verbose=0)
        # out.append([dfit.model['RSS'], dfit.model['name'], np.where(dfit.summary['name']=='uniform')[0][0], s])
        out.append([dfit.model['RSS'], dfit.model['name'], s])

    df = pd.DataFrame(out, columns=['RSS','name','samples'])
    ax=df['RSS'].plot(grid=True, label='smooth: '+str(smooth) + ' - RSS: ' + str(df['RSS'].mean()))

ax.set_xlabel('Nr.Samples')
ax.set_ylabel('RSS')
ax.set_xticks(np.arange(0,len(samples)))
ax.set_xticklabels(samples.astype(str), rotation = 90)
ax.set_ylim([0, 0.0005])
ax.legend()


# %% Fit and transform
X = np.random.beta(5, 8, [100,100])
y = [-1,-0.8,-0.6,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.5]

dfit = distfit(stats='wasserstein')
dfit.fit()
dfit.transform(X)
dfit.plot()
dfit.predict(y)
dfit.plot()

dfit.plot_summary()

# %%  for Fit and transform in one go
X = np.random.beta(5, 8, [100,100])
y = [-1,-0.8,-0.6,0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.5]

model = distfit()
model.fit_transform(X)
model.plot()
model.predict(y)
model.plot()

model.plot_summary()

# %% Show some results
print(model.results['y_proba'])
print(model.results['y_pred'])
# print(model.results['df'])
print(model.summary)


# %%
X = np.random.normal(0, 2, 1000)
y = [-8,-6,0,1,2,3,4,5,6]

model = distfit()
model.fit_transform(X)
model.plot()

# Make prediction
model.predict(y)
model.plot()

# %%
X = np.random.normal(5, 8, [100,100])
y = [-35, -10, 0, 10, 15, 35]

model = distfit()
model.fit_transform(X)
model.predict(y)
model.plot()
model.results['y_proba']
model.results['y_pred']

model = distfit(todf=True)
model.fit_transform(X)
model.predict(y)
model.plot()

model.results['y_proba']
model.results['y_pred']
model.results['df'] # Only availble when using todf=True

# %%
X = np.random.beta(5, 8, 1000)

model = distfit()
model.fit_transform(X)
model.plot()

# %% Find distribution parameters
X = np.random.normal(0, 2, 5000)
model = distfit()
model.fit_transform(X)
model.plot()

X = np.random.normal(10, 1, 5000)
model = distfit()
model.fit_transform(X)
model.plot()

X = np.random.normal(10, 5, 5000)
model = distfit()
model.fit_transform(X)
model.plot()

# %%
X = np.random.normal(0, 2, 1000)
y = [-8,-6,0,1,2,3,4,5,6]

model = distfit(todf=True)
model.fit_transform(X)
model.predict(y)
model.plot()

model.results['y_proba']
model.results['y_pred']
model.results['df']


model = distfit(bound='up', todf=True)
model.fit_transform(X)
model.predict(y)
model.plot()
model.results['df']

model = distfit(bound='down', todf=True)
model.fit_transform(X)
model.predict(y)
model.plot()
model.results['df']

# %% Find best fit distribution
X = np.random.normal(0, 2, 1000)
y = [-8,-6,0,1,2,3,4,5,6]

model = distfit()
model.fit_transform(X)
model.plot()

model = distfit(distr='popular')
model.fit_transform(X)
model.plot()

model = distfit(distr='full')
model.fit_transform(X)
model.plot()


# %% Quantile approach
from distfit import distfit
import numpy as np

X = np.random.normal(10, 3, 10000)
y = [3,4,5,6,10,11,12,18,20]

# Initialize
# dfit = distfit(method='percentile', alpha=0.05, todf=False)
dfit = distfit(method='quantile', alpha=0.05, todf=False)
# dfit = distfit(method='parametric', alpha=0.05, todf=False)
dfit.fit_transform(X)
dfit.plot()

# Make prediction
dfit.predict(y)
dfit.plot()
dfit.plot_summary()

# from tabulate import tabulate
# print(tabulate(dfit.results['df'], tablefmt="grid", headers="keys"))

# %%
