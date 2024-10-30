from bs4 import BeautifulSoup
import pandas as pd
import warnings
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots

url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"

html_data_2 = requests.get(url).text
soup_2 = BeautifulSoup(html_data_2,'html.parser')
gme_revenue = pd.DataFrame(columns=["Date","Revenue"])

for row in soup_2.find("tbody").find_all("tr"):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text

    gme_revenue = pd.concat([gme_revenue,pd.DataFrame({"Data":[date],"Revenue":[revenue]})],ignore_index=True)
    gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(r',|\$',"", regex=True)
    
print(gme_revenue.tail())
