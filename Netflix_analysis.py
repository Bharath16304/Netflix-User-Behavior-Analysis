import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('netflix_data.csv')  # columns: user_id, show_title, genre, watch_hours, rating

# Top Genres
top_genres = df['genre'].value_counts()
top_genres.plot(kind='bar', title='Top Genres Watched')
plt.show()

# Binge Behavior
binge = df.groupby('user_id')['watch_hours'].sum()
binge.hist(bins=20)
plt.title('Total Watch Hours per User')
plt.show()

# Ratings vs Genres
sns.boxplot(x='genre', y='rating', data=df)
plt.title('Ratings by Genre')
plt.xticks(rotation=45)
plt.show()
