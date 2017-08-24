import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from gurobipy import *
from pandas_datareader.data import DataReader
from datetime import datetime

stocks = ['ISP', 'CSV', 'RGC', 'WMS', 'GYB', 'KCC', 'BPL', 'WTW', 'GS', 'SPR']
ls_key = 'Adj Close'
start = datetime(2014,1,1)
end = datetime(2016,12,23)
# fetch daily adjusted close and drop na, WMS go public on 2014-07-25
price = DataReader(stocks, 'yahoo', start, end)[ls_key].dropna()[stocks]
# Calculate log return
rtn = np.log(price) - np.log(price.shift(1))
meanDailyReturns = rtn.mean()
covMatrix = rtn.cov()

# Calculate performance
def performance(weights, meanReturns, covMatrix):
    portReturn = np.sum(meanReturns*weights)
    portStdDev = np.sqrt(np.dot(weights.T, np.dot(covMatrix, weights)))
    return portReturn * 252, portStdDev * np.sqrt(252), portReturn/portStdDev * np.sqrt(252)
# Visualize Efficient Frontier
numPortfolios = 10000
results=np.zeros((3,numPortfolios))
for i in xrange(numPortfolios):
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)
    results[0,i], results[1,i], results[2,i] = performance(weights, meanDailyReturns, covMatrix)
plt.scatter(results[1,], results[0,], c=results[2,])
plt.title('Portfolio Simulation for Efficient Frontier');plt.xlabel('Expected Volatility');plt.ylabel('Expected Return');
cl = plt.colorbar();cl.set_label('Sharpe Ratio');plt.show();

# Optimize Sharpe Ratio
def sharpe_optimize(mu, Q):
    N = len(mu)
    model = Model()
    # Add variables to model
    y = []
    for j in xrange(N):
        y.append(model.addVar(vtype=GRB.CONTINUOUS))
        model.update()
    # Constraints
    expr = LinExpr()
    for i in xrange(N):
        expr += mu[i] * y[i]
    model.addConstr(expr, '==', 1)
    # Use full covariance matrix
    obj = QuadExpr()
    for i in xrange(N):
        for j in xrange(N):
            if Q[i][j] != 0:
                obj += Q[i][j] * y[i] * y[j]
    model.setObjective(obj, GRB.MINIMIZE)
    model.update()
    # Solve
    model.optimize()
    if model.status == GRB.Status.OPTIMAL:  # optimization status code
        result = model.getVars()
        yOpt = np.zeros(N)
        for i in xrange(N):
            yOpt[i] = result[i].x
        return yOpt / sum(yOpt)  # normalize to get weights
    else:
        return 'Not lucky this time'
amount = sharpe_optimize(meanDailyReturns, covMatrix.values.tolist())*10**6
y_pos = np.arange(len(stocks))
plt.barh(y_pos, amount, align='center', alpha=0.5)
plt.yticks(y_pos, stocks)
plt.xlabel('Investment Amount')
plt.title('Mean-Variance Portfolio Optimization')
plt.show()

compare = []
index = []
for i in xrange(1,len(rtn)-504,22):
    temp = rtn[i:(i+504)]
    index.append(rtn.index[i+504])
    compare.append(list(sharpe_optimize(temp.mean(), temp.cov().values.tolist())*10**6))
compare = pd.DataFrame(compare,columns=stocks,index=index)
compare.plot(colormap="jet")
