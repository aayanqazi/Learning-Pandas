import pandas as pd

cities = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
pd.DataFrame({'City Name': cities, 'Population': population})
print(pd.DataFrame({'City Name': cities, 'Population': population}))