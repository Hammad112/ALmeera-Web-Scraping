
# Web Scraper for Almeera Website

This is a Python web scraper that extracts product information from the [Almeera website](https://almeera.online/) and saves it into a CSV file. The script is containerized using Docker, making it easy to set up and run in any environment.

## Features

- Scrapes product categories, sub-categories, product images, descriptions, and prices from the Almeera website.
- Saves the scraped data to a CSV file (`scrap_data.csv`).
- Removes punctuation and numbers from URLs for clean Sub Category.


## Prerequisites

Before running this project, ensure you have the following installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)

## Python Libraries Used

- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML and extracting data.
- `string`: For removing punctuation and numbers.
- `re`: For regular expression operations .

All required libraries are automatically installed inside the Docker container when you build the image.

## Setup and Usage

### 1. Clone the Repository

```bash
git clone https://github.com/iammkullah/scraping_projects_bave_internees.git
cd web-scraper
```

### 2. Docker Setup

Ensure that you have Docker installed on your machine. To build and run the scraper:

#### Build the Docker Image

```bash
docker build -t scraper-app .
```

This command will build a Docker image named `scraper-app` using the instructions in the `Dockerfile`.

#### Run the Docker Container

```bash
docker run -it scraper-app
```

This command will run the container, execute the Python scraper script, and generate a CSV file named `scrap_data.csv` in the `./app` directory of the container.

### 3. Output

The script scrapes product data from the Almeera website and saves the following fields to `scrap_data.csv`:

- **Page**: The page number from which the data was scraped.
- **Sub-Category**: The cleaned sub-category name (punctuation and numbers removed).
- **Image Link**: The link to the product image.
- **Description**: The product description.
- **Price**: The price of the product.
- **URL**: The URL of the scraped page.

### 4. Accessing the CSV File

After the scraper runs, the `scrap_data.csv` file is generated in the current directory. You can extract it from the Docker container to your local machine using the following command:

```bash
docker cp <container_id>:/app/scrap_data.csv .
```

To find the container ID, use:

```bash
docker ps -a
```

### 5. Modifying the Script

If you need to modify the Python script (`main_scrap.py`):

- Edit the `main_scrap.py` file in your local environment.
- Rebuild the Docker image:

  ```bash
  docker build -t scraper-app .
  ```

- Rerun the container.

## Dockerfile Overview

Here’s a quick look at the `Dockerfile` used in this project:

```Dockerfile
# Use Python 3.9-slim as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required Python packages
RUN pip install --no-cache-dir requests beautifulsoup4

# Run the Python script
CMD ["python", "./your_script.py"]
```

## Troubleshooting

- **Error: Docker not found**: Ensure Docker is installed and running on your system.
- **Scraping fails for some URLs**: Check if the website structure has changed or if you're being blocked by the website (rate limiting, IP blocks).
- **CSV not generated**: Ensure that the container has the correct file permissions and paths.

## Contributing

Feel free to submit issues or pull requests if you'd like to improve the scraper or Docker setup.
