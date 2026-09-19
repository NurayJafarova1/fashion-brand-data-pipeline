import string
from pathlib import Path

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://remixshop.com/bg/brands/catalogue"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "output" / "brands.sql"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_brands():
    """Collect brand names from the catalogue pages."""

    brands = []

    for letter in string.ascii_uppercase:
        url = f"{BASE_URL}?letter={letter}&type=ALL"

        print(f"Fetching brands for letter {letter}...")

        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=15
            )

            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Failed to fetch {letter}: {error}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            text = link.get_text(strip=True)

            if text and len(text) > 1:
                brands.append(text)

    return brands


def clean_brands(brands):
    """Remove duplicate brand names and sort the result."""

    return sorted(set(brands), key=str.lower)


def escape_sql(value):
    """Escape apostrophes for SQL INSERT statements."""

    return value.replace("'", "''")


def generate_sql(brands):
    """Generate a SQL INSERT statement."""

    values = [
        f"('{escape_sql(brand)}')"
        for brand in brands
    ]

    return (
        "INSERT INTO brands (name) VALUES\n"
        + ",\n".join(values)
        + ";"
    )


def save_sql(sql):
    """Save generated SQL to the output directory."""

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        sql,
        encoding="utf-8"
    )

    print(f"SQL file created: {OUTPUT_FILE}")


def main():
    brands = fetch_brands()

    clean_data = clean_brands(brands)

    print(f"Total unique brands: {len(clean_data)}")

    sql = generate_sql(clean_data)

    save_sql(sql)


if __name__ == "__main__":
    main()