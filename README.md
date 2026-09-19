# Fashion Brand Data Pipeline

A Python-based data collection pipeline for extracting fashion and beauty brand information from public catalogue pages, cleaning the collected data, and exporting it into SQL-ready format.

The project was originally developed to help populate the brand catalogue for a second-hand marketplace application.

## Features

- Automated A-Z catalogue crawling
- HTTP data collection using Requests
- HTML parsing with BeautifulSoup
- Duplicate brand removal
- Alphabetical data sorting
- SQL-safe string escaping
- Automatic SQL INSERT generation
- HTTP error handling
- Structured output generation

## Technologies

- Python
- Requests
- BeautifulSoup
- SQL

## Project Structure

```text
fashion-brand-data-pipeline/
│
├── src/
│   ├── remix_scraper.py
│   └── sephora_fetcher.py
│
├── output/
│   └── brands.sql
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/fashion-brand-data-pipeline.git
```

Navigate to the project directory:

```bash
cd fashion-brand-data-pipeline
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the fashion brand scraper:

```bash
python src/remix_scraper.py
```

The scraper visits catalogue pages from A to Z, collects brand names, removes duplicates, and generates an SQL file.

The generated file is saved to:

```text
output/brands.sql
```

## Example SQL Output

```sql
INSERT INTO brands (name) VALUES
('Adidas'),
('Armani'),
('Balenciaga'),
('Burberry');
```

## Current Result

The pipeline currently generates more than 3,000 unique brand records from the catalogue source.

## Use Cases

The generated dataset can be used in:

- Second-hand marketplaces
- Fashion applications
- E-commerce platforms
- Product catalogue databases
- Backend database seeding

## Project Background

This project was created while working on a second-hand marketplace platform and was used to automate the creation of a large fashion brand catalogue instead of manually entering thousands of brand names.

## Disclaimer

This project is intended for educational and development purposes. Website terms of service and robots.txt policies should be reviewed before running automated data collection against third-party websites.

## License

MIT License