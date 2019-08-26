import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],
               axis=1)
df.iloc[0, 2] = np.nan

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

dfs = df.style.applymap(color_negative_red)
test_style = dfs.render()
with open('myhtml.html','w') as f:
    f.write(test_style)



