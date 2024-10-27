from bs4 import BeautifulSoup
import requests
import csv
import re
import string
from string import punctuation

# Base URL
url = 'https://almeera.online/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

# Find the list of categories
home = soup.find('ul', class_='flyout-menu catalog-categories catalog-categories-tree')
lists = home.find_all('li')

# Open the CSV file in write mode only once
with open('scrap_data.csv', mode='w', newline='', encoding='utf-8') as file:
    # Define the column headers for the CSV
    writer = csv.writer(file)
    writer.writerow(['Page', 'Sub-Category','Photo Link', 'Description', 'Price', 'URL'])  # Write the header
    
    # Loop through the categories
    for items in lists:
        listings = items.a['href']
        urls = url + listings
        print(urls)
        # Loop through the pages (e.g., 1 to 2)
        for i in range(1, 3):  # Adjust the range as needed
            if i == 1:
                new_url = urls
            else:
                new_url = urls + '?pageId=' + str(i)

            # Make a request to each page
            page = requests.get(new_url).text
            soup_page = BeautifulSoup(page, 'html.parser')

            # Find the products grid
            ul = soup_page.find('ul', class_='products-grid grid-list')
            items = soup_page.find_all('li', class_='product-cell box-product')

            # Loop through each product and extract data
            for item in items:
                remove_chars = string.punctuation + string.digits
                # Create a translation table to remove both punctuation and digits
                cleaned_listings = listings.translate(str.maketrans('', '', remove_chars))
                img_link = item.div.div.a['href']  # Extract the photo link
                img_link = url + img_link
                description = item.find('h5', class_='product-name').text.strip()  # Extract the description
                price = item.find('span', class_='price product-price').text.strip()  # Extract the price

                # Print the scraped data (optional)
                print(f'Page {i}')
                print(cleaned_listings)
                print(img_link)
                print(description)
                print(price)
                print(" ")

                # Write the scraped data to the CSV file
                writer.writerow([i,cleaned_listings, img_link, description, price, new_url])

print("Data successfully written to 'scraped_data.csv'")
