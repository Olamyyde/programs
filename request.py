import requests

# r = requests.get("http://www.pythonhow.com")
# print(r.text[:100])


# response = requests.get("http://nairaland.com")
# text = response.text
# count_a = text.count("a")
# print(count_a)



# import webbrowser

# query = input("input your query: ")
# webbrowser.open(f"https://google.com/search?q={query}")


import pandas as pd

# e = pd.read_csv("s.txt")
# data2 = e * 2
# data2.to_csv("s.txt", index=None) 


import matplotlib.pyplot as plt
e = pd.read_csv("s.txt")
e.plot(x='x', y='y', kind='scatter')
plt.show()





