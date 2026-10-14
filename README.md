# Python Web Scraping

Use web scraping to produce a largest U.S. companies by revenue table.   
Scrape the data from Wikipedia with just a few lines of Python.  
Use Beautiful Soup and pandas for an instant DataFrame, (and optional CSV).

---

### Quick start  
**Clone this repo:**       
```git clone git@github.com:neilburbage/Python-Web-Scraping```  
**Make sure you've added your SSH key first:**     
```https://docs.github.com/en/authentication/connecting-to-github-with-ssh```  
```cd Python-Web-Scraping```  
**Create a virtual environment:**     
```python -m venv .venv```  
```# Linux / macOS: source .venv/bin/activate```     
```# Windows (PowerShell): .venv\Scripts\activate```  
```# Windows (cmd): .venv\Scripts\activate.bat```  
**Install dependencies:**    
```pip install -r requirements.txt```  
**Run the scraper:**    
```python scraper.py```

---

### Example table

<small>

| Rank | Name               | Industry                   | Revenue (USD millions) |
| ---- | ------------------ | -------------------------- | ---------------------- |
| 1    | Walmart            | Retail                     | 680 985                |
| 2    | Amazon             | Retail and cloud computing | 637 959                |
| 3    | UnitedHealth Group | Healthcare                 | 400 278                |

*Sample scraped 14 October 2026; figures follow Wikipedia's current list.*

</small>

---

### Project layout

```
├── scraper.py            # Beautiful Soup → pandas
├── us_top_companies.csv  # sample output
├── requirements.txt      # bs4, lxml, pandas, requests
├── .gitignore            # venv/, __pycache__/
└── README.md             # you are here
```
---