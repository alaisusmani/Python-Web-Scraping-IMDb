# IMDb Anime Scraper

A Python automation tool that scrapes real-time data from IMDb to identify the top trending anime series and movies. This project demonstrates web scraping techniques, HTML parsing, and data extraction using the `BeautifulSoup` library.

## 🚀 Features
* **Real-Time Data:** Fetches the latest top 10 trending anime directly from IMDb.
* **Anti-Blocking:** Uses custom User-Agent headers to mimic a real browser and bypass basic scraping protections.
* **Error Handling:** Robust error management for network issues or missing data fields (e.g., missing ratings).
* **Data Parsing:** extracts specific data points (Title, Rating) from complex HTML structures.

## 🛠️ Technologies Used
* **Python 3.13**
* **BeautifulSoup4** (HTML Parsing)
* **Urllib3** (HTTP Requests)
* **Lxml** (Parser Engine)

## 📦 How to Run

1.  **Clone the repository**
    ```bash
    git clone https://github.com/alaisusmani/Python-Web-Scraping-IMDb.git
    ```

2.  **Install Dependencies**
    ```bash
    pip install urllib3 beautifulsoup4 lxml
    ```

3.  **Run the Script**
    ```bash
    python topanime.py
    ```

## ⚠️ Disclaimer
This tool is for educational purposes only. Please respect IMDb's `robots.txt` policy and do not overburden their servers with excessive requests.
