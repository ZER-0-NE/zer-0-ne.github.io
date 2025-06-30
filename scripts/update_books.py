#!/usr/bin/env python

import os
import yaml
from bs4 import BeautifulSoup

# Configuration
INDEX_HTML_PATH = "/Users/abhisheksingh/Desktop/zer-0-ne.github.io/index.html"
BOOKS_NOTES_DIR = "/Users/abhisheksingh/Documents/Second brain/Evernote/Books"
BOOKS_DATA_FILE = "/Users/abhisheksingh/Desktop/zer-0-ne.github.io/_data/books.yml"

def get_book_titles_from_index():
    """Parses index.html to extract book titles."""
    with open(INDEX_HTML_PATH, 'r') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    books_section = soup.find('h2', string="I'm quite fond of reading books which include:")
    if not books_section:
        print("Could not find the books section in index.html")
        return []

    books_list = books_section.find_next('ul').find_all('li')
    titles = [li.text.strip() for li in books_list]
    return titles

def get_book_summary(book_title):
    """Finds the corresponding note file and extracts a summary."""
    # A simple way to match filenames - can be improved
    normalized_title = book_title.lower().replace(' ', '_') + ".txt"
    
    try:
        for filename in os.listdir(BOOKS_NOTES_DIR):
            if filename.lower().startswith(normalized_title[:5]): # Match first 5 chars
                with open(os.path.join(BOOKS_NOTES_DIR, filename), 'r') as f:
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                    return ' '.join(lines[:3]) # Return first 3 non-empty lines
    except FileNotFoundError:
        pass # Directory might not exist

    return "No summary available."

def main():
    """Main function to update the books data file."""
    book_titles = get_book_titles_from_index()
    if not book_titles:
        return

    books_data = []
    for title in book_titles:
        summary = get_book_summary(title)
        books_data.append({'title': title, 'summary': summary})

    with open(BOOKS_DATA_FILE, 'w') as f:
        yaml.dump(books_data, f)

    print(f"Successfully updated {BOOKS_DATA_FILE} with {len(books_data)} books.")

if __name__ == "__main__":
    main()
