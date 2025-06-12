# Python‑Web‑Scraping

Use web scraping to produce a largest U.S. companies by revenue table.   
Scrape the data from Wikipedia with just a few lines of Python.  
Use Beautiful Soup and pandas for an instant DataFrame, (and optional CSV).

***

### Quick start  
Clone this repo:       
```git clone git@github.com:neilburbage/Python-Web-Scraping.git```  
```$ cd Python-Web-Scraping```  
Create a virtual environment:     
```python -m venv venv```  
```# Linux: source venv/bin/activate   # Windows: venv\Scripts\activate```  
Install dependencies:    
```pip install -r requirements.txt```  
Run the scraper:    
```scraper.py```

***

### Example table

| Rank | Name       | Industry | Revenue (USD millions) |
| ---: | ---------- | -------- | ---------------------: |
|    1 | Walmart    | Retail   |                648 124 |
|    2 | Amazon.com | Retail   |                574 785 |
|    3 | ExxonMobil | Energy   |                413 680 |

**Prints the results and saves a CSV (if required)**

***

### Project layout

```
├── scraper.py         # Beautiful Soup → pandas
├── requirements.txt   # bs4, lxml, pandas, requests
├── .gitignore         # venv/, __pycache__/
└── README.md          # you are here
```
***