import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = "http://quotes.toscrape.com"

def scrape_quotes():
    quotes_data = []
    url = BASE_URL
    while url:
        print(f"Scraping: {url}")
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        quotes = soup.select(".quote")
        for quote in quotes:
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.select(".tags .tag")]
            quotes_data.append({"text": text, "author": author, "tags": tags})

        next_btn = soup.select_one(".pager .next a")
        url = BASE_URL + next_btn['href'] if next_btn else None

    return quotes_data

def save_to_csv(data, filename="quotes.csv"):
    df = pd.DataFrame(data)
    df['tags'] = df['tags'].apply(lambda tags: ", ".join(tags))
    df.to_csv(filename, index=False)
    print(f"Saved data to {filename}")

def analyze_data(filename="quotes.csv"):
    df = pd.read_csv(filename)

    # Count quotes per author
    author_counts = df['author'].value_counts()
    print("Quotes per author:\n", author_counts)

    # Plot top 10 authors by number of quotes
    author_counts.head(10).plot(kind='bar', title="Top 10 Authors by Number of Quotes")
    plt.xlabel("Author")
    plt.ylabel("Number of Quotes")
    plt.tight_layout()
    plt.savefig("top_authors.png")
    print("Saved author analysis plot as top_authors.png")

    # Analyze tags frequency
    tags_series = df['tags'].str.split(", ").explode()
    tags_counts = tags_series.value_counts()
    print("\nTop Tags:\n", tags_counts.head(10))

    # Plot top 10 tags
    tags_counts.head(10).plot(kind='bar', title="Top 10 Tags")
    plt.xlabel("Tag")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig("top_tags.png")
    print("Saved tags analysis plot as top_tags.png")

def main():
    data = scrape_quotes()
    save_to_csv(data)
    analyze_data()

if __name__ == "__main__":
    main()
