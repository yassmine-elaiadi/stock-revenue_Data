
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)

url =" https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text

soup = BeautifulSoup(html_data,'html.parser')
tesla_revenue = pd.DataFrame(columns=["Date","Revenue"])
for row in soup.find("tbody").find_all('tr'):   #locate the table 
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text 
    
    tesla_revenue = pd.concat([tesla_revenue,pd.DataFrame({"Date" : [date],"Revenue":[revenue]})],ignore_index=True)
    tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(r',|\$',"", regex=True)
    tesla_revenue.dropna(inplace=True)

    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
print(tesla_revenue.tail())