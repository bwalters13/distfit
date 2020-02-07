import numpy as np
import distfit

def test_distfit():
    data_random = np.random.normal(0, 2, 1000)
    data = [-14,-8,-6,0,1,2,3,4,5,6,7,8,9,10,11,15]
    model = distfit.fit(data_random)
    
    # TEST 1: check output is unchanged
    assert [*model.keys()]==['method', 'model', 'summary', 'histdata', 'size', 'Param']
    # TEST 2: Check model output is unchanged
    assert [*model['model'].keys()]==['distribution', 'params', 'name', 'sse', 'loc', 'scale', 'arg', 'CII_min_alpha', 'CII_max_alpha']

    # TEST 3: Check specific distribution
    model = distfit.fit(data_random, distribution='t', verbose=2)
    assert model['model']['name']=='t'

    # TEST 4: Check specific distribution
    model = distfit.fit(data_random, alpha=0.05, verbose=2)
    assert model['model']['CII_min_alpha'] is not None
    assert model['model']['CII_max_alpha'] is not None
    # model = distfit.fit(data_random, alpha=1)
    # assert np.isinf(model['model']['CII_min_alpha'])
    # assert np.isinf(model['model']['CII_max_alpha'])

    # TEST 5: Bound check
    model = distfit.fit(data_random, alpha=0.05, bound='up', verbose=2)
    assert model['model']['CII_min_alpha'] is None
    assert model['model']['CII_max_alpha'] is not None
    model = distfit.fit(data_random, alpha=0.05, bound='down', verbose=2)
    assert model['model']['CII_min_alpha'] is not None
    assert model['model']['CII_max_alpha'] is None
    model = distfit.fit(data_random, alpha=0.05, bound='both', verbose=2)
    assert model['model']['CII_min_alpha'] is not None
    assert model['model']['CII_max_alpha'] is not None

    # TEST 6: Distribution check
    data_random = np.random.normal(0, 2, 10000)
    model = distfit.fit(data_random, distribution='norm')
    model['model']['loc']
    '%.1f' %model['model']['scale']=='2.0'
    '%.1f' %np.abs(model['model']['loc'])=='0.0'


def test_proba_emperical():
    X = np.random.normal(0, 2, 1000)
    y = [-14,-8,-6,0,1,2,3,4,5,6,7,8,9,10,11,15]

    # TEST 1: Check bounds
    out1 = distfit.proba_emperical(y, X, bound='up')
    assert np.all(np.isin(np.unique(out1['proba'].bound), ['none','up']))
    out2 = distfit.proba_emperical(y, X, bound='down')
    assert np.all(np.isin(np.unique(out2['proba'].bound), ['none','down']))
    out3 = distfit.proba_emperical(y, X, bound='both')
    assert np.all(np.isin(np.unique(out3['proba'].bound), ['none','down','up']))
    
    # TEST 2: Check different sizes array
    X = np.random.normal(0, 2, [10,100])
    out1 = distfit.proba_emperical(y, X, bound='up')
    assert np.all(np.isin(np.unique(out1['proba'].bound), ['none','up']))

def test_proba_parametric():
    data_random = np.random.normal(0, 2, 1000)
    data = [-14,-8,-6,0,1,2,3,4,5,6,7,8,9,10,11,15]
    model = distfit.fit(data_random)

    # TEST 1: Check pre-trained model gives same results
    out1 = distfit.proba_parametric(data, data_random, model=model)
    out2 = distfit.proba_parametric(data, data_random)
    assert np.all(out1['proba']==out2['proba'])

    # TEST 2 Check number of output probabilities
    out = distfit.proba_parametric(data, data_random, model=model)
    assert out['proba'].shape[0]==len(data)
    
    # TEST 3: Check bounds
    out1 = distfit.proba_parametric(data, data_random, bound='up')
    assert np.all(np.isin(np.unique(out1['proba'].bound), ['none','up']))
    out2 = distfit.proba_parametric(data, data_random, bound='down')
    assert np.all(np.isin(np.unique(out2['proba'].bound), ['none','down']))
    out3 = distfit.proba_parametric(data, data_random, bound='both')
    assert np.all(np.isin(np.unique(out3['proba'].bound), ['none','down','up']))
    
    # TEST 4: Check whether alpha responds on results
    out1 = distfit.proba_parametric(data, data_random, alpha=0.05)
    out2 = distfit.proba_parametric(data, data_random, alpha=0.2)
    assert np.all(out2['proba']['Padj']==out1['proba']['Padj'])
    assert np.all(out2['proba']['Padj']==out1['proba']['Padj'])
    assert sum(out1['proba']['bound']=='none')>sum(out2['proba']['bound']=='none')

    # TEST 5: Check different sizes array
    X = np.random.normal(0, 2, [10,100])
    y = [-14,-8,-6,0,1,2,3,4,5,6,7,8,9,10,11,15]
    out1 = distfit.proba_parametric(y, X, bound='up')
    assert np.all(np.isin(np.unique(out1['proba'].bound), ['none','up']))


# def test_plot():
#     data_random = np.random.normal(0, 2, 1000)
#     data = [-14,-8,-6,0,1,2,3,4,5,6,7,8,9,10,11,15]

#     model = distfit.fit(data_random)
#     distfit.plot(model)
#     distfit.plot_summary(model)

#     out = distfit.proba_parametric(data, data_random)
#     distfit.plot(out)

#     out = distfit.proba_parametric(data, data_random, bound='up')
#     distfit.plot(out)

#     out = distfit.proba_parametric(data, data_random, bound='down')
#     distfit.plot(out)

#     out = distfit.proba_parametric(data, data_random, alpha=0.05)
#     distfit.plot(out)

#     out = distfit.proba_parametric(data, data_random, alpha=0.2)
#     distfit.plot(out)


#     out = distfit.proba_emperical(data, data_random)
#     distfit.plot(out)

#     out = distfit.proba_emperical(data, data_random, bound='up')
#     distfit.plot(out)

#     out = distfit.proba_emperical(data, data_random, bound='down')
#     distfit.plot(out)

#     out = distfit.proba_emperical(data, data_random, alpha=0.2)
#     distfit.plot(out)