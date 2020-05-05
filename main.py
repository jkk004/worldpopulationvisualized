import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://gist.githubusercontent.com/johnburnmurdoch/4199dbe55095c3e13de8d5b2e5e5307a/raw/fa018b25c24b7b5f47fd0568937ff6c04e384786/city_populations',
                 usecols=['name', 'group', 'year', 'value'])
print("What year(1500-2020) would you like to see: ")

choice = int(input())
final = (data[data['year'].eq(choice)].sort_values(by='value', ascending=True).head(15))

fig, ax = plt.subplots(figsize=(10,5))
ax.barh(final['name'], final['value'])
ax.set_title("World's Most Populous Cities in " + str(choice))
plt.xlabel("Population in Thousands")
plt.show()
