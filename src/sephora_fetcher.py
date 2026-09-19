from pathlib import Path

import requests


URL = "https://www.sephora.com/brands-list"

OUTPUT_FILE = (
    Path(__file__).resolve().parent.parent
    / "output"
    / "sephora.html"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def fetch_page():
    """Download the Sephora brands page."""

    response = requests.get(
        URL,
        headers=HEADERS,
        timeout=15
    )

    response.raise_for_status()

    return response.text


def save_page(html):
    """Save page HTML locally for parsing experiments."""

    OUTPUT_FILE.write_text(
        html,
        encoding="utf-8"
    )

    print(f"HTML saved to {OUTPUT_FILE}")


def main():
    try:
        html = fetch_page()
        save_page(html)

    except requests.RequestException as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()