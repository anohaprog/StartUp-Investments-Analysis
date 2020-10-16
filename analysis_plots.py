import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

plt.style.use('ggplot')

data = pd.read_csv("investments_VC.csv", encoding='unicode_escape')

data = data[~data["name"].isna()]
data = data.rename(columns={' market ': 'market', ' funding_total_usd ': 'funding_total_usd'})
data["funding_total_usd"] = data["funding_total_usd"].str.replace(',','')
data['funding_total_usd'] = pd.to_numeric(data['funding_total_usd'], errors='coerce')

print(f"Count rows: {data.shape[0]}")
print(f"Count columns: {data.shape[1]}")

# Status
status_data = data['status'].value_counts()
print(status_data)
plt.title('Startup status')
status_data.plot.pie(startangle=90, autopct='%1.1f%%', explode=(0,0.1,0.1), label='')
plt.show()

# Only startups with operating status
operating = data[data['status'] == 'operating']

# Year
print(operating['founded_year'].value_counts())
plt.title('Startup years')
plt.ylabel('count')
data.groupby('founded_year').size().plot(color='green', linewidth=4.0)
plt.show()


# Country
plt.figure(figsize=(16, 5))
country_data = operating['country_code'].value_counts()[:10]
print(country_data)
sns.barplot(y=country_data.values, x=country_data.index).set(title='Top 10 operating startup countries')
plt.xticks(rotation=45)
plt.show()

# Market
market_data = operating['market'].value_counts()[:20]
print(market_data)
plt.figure(figsize=(10, 5))
stopwords = set(STOPWORDS)
stopwords.update(["NaN", "market", "Length", "object", "Name", "dtype", "int64"])
wordcloud = WordCloud(stopwords=stopwords, max_words=50000,background_color='white').generate(str(market_data))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Finance
plt.figure(figsize=(12, 5))
finance_data = operating.groupby('market')['funding_total_usd'].sum().sort_values(ascending=False)[:10]
sns.barplot(y=finance_data.values, x=finance_data.index)
plt.xticks(rotation=15)
plt.show()
