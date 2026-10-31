import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Amazon books dataset
df = pd.read_csv("bestsellers.csv")

# Display first 5 records
print("AMAZON BEST SELLING BOOKS")
print(df.head())

# Display dataset information
print("\nTotal Books:", len(df))

print("\nDataset Information:")
print(df.info())

# Calculate average rating
print("\nAverage Rating:")
print(df["User Rating"].mean())

# Calculate average price
print("\nAverage Price:")
print(df["Price"].mean())
# Top 5 Authors
top_authors = df["Author"].value_counts().head(5)

print("\nTop 5 Authors:")
print(top_authors)

# Highest Rated Books
top_rated = df.sort_values(
    by="User Rating",
    ascending=False
)

print("\nTop 5 Highest Rated Books:")
print(top_rated[["Name", "User Rating"]].head(5))

# Most Reviewed Books
top_reviews = df.sort_values(
    by="Reviews",
    ascending=False
)

print("\nTop 5 Most Reviewed Books:")
print(top_reviews[["Name", "Reviews"]].head(5))
# Genre Analysis

genre = df["Genre"].value_counts()

print("\nGenre Distribution:")
print(genre)

# Fiction and Non-Fiction comparison
fiction = len(df[df["Genre"] == "Fiction"])
non_fiction = len(df[df["Genre"] == "Non Fiction"])

print("\nFiction Books:", fiction)
print("Non-Fiction Books:", non_fiction)
# Graph 1: Fiction vs Non-Fiction

import os

os.makedirs("graphs", exist_ok=True)

genre = df["Genre"].value_counts()

plt.figure(figsize=(7, 5))
genre.plot(kind="bar")

plt.title("Fiction vs Non-Fiction Books")
plt.xlabel("Genre")
plt.ylabel("Number of Books")

plt.savefig("graphs/genre.png")
plt.show()
# Graph 2: Top 5 Authors

top_authors = df["Author"].value_counts().head(5)

plt.figure(figsize=(8, 5))

top_authors.plot(kind="bar")

plt.title("Top 5 Best Selling Authors")
plt.xlabel("Author Name")
plt.ylabel("Number of Books")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("graphs/authors.png")
plt.show()
# Graph 3: Book Ratings

ratings = df["User Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

ratings.plot(kind="bar")

plt.title("Amazon Books Rating Analysis")
plt.xlabel("Book Rating")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("graphs/ratings.png")
plt.show()
# Graph 4: Average Book Price

price = df.groupby("Genre")["Price"].mean()

plt.figure(figsize=(8, 5))

price.plot(kind="bar")

plt.title("Average Book Price by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Price")

plt.tight_layout()

plt.savefig("graphs/price.png")
plt.show()
# Graph 5: Books Per Year

yearly_books = df["Year"].value_counts().sort_index()

plt.figure(figsize=(9, 5))

yearly_books.plot(kind="line", marker="o")

plt.title("Best Selling Books Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Books")

plt.grid(True)
plt.tight_layout()

plt.savefig("graphs/year.png")
plt.show()

print("\nPROJECT COMPLETED SUCCESSFULLY!")