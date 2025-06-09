# BG Tech Jobs Analysis 

This project analyzes trends in the Bulgarian IT job market by scraping the number of job listings on dev.bg and generating visual insights using Python and Jupyter. 

The project expands on a dataset found on [Kaggle](https://www.kaggle.com/code/dimodimchev/deep-dive-into-bulgaria-s-it-job-market-trends/input) for Bulgarian job listings in 2023 

## Project overview

The goal of this project is to: 
-  Scrape IT job listings from a Bulgarian job website 
-  Store data in a CSV file for regulat updates 
-  Analyze job market trends such as: 
    - Most in-demand roles 
    - Popular tech stacks

## Tech stack 
- **Python 3.12**
- **Jupyter Notebook**
- `requests`, `BeautifulSoup` - web scraping
- `pandas` - data wrangling 
- `matplotlib`, `seaborn` - data visualization 
- `GitHub Actions` - automation
- `Git` + GitHub - version control 

## Project structure 
bg-tech-jobs/
├── .github/workflows       # Automation scripts
├── data/                   # Collected job listing CSV files
├── notebooks/              # Jupyter notebooks for analysis
│   └── BG_Tech_Jobs_Analysis.ipynb
├── scraper/                # Web scraping script
│   └── job_scraper.py
├── update_csv_data/                  # Module to update the csv file
│   └── csv_update.py
├── main.py          # Entry point script to run scraper and update the csv
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and folders
└── README.md               # Project documentation

## How to use
1. **Clone the repository**
```bash
   git clone https://github.com/Corentin-dupriez/bg-tech-jobs.git
   cd bg-tech-jobs
```
2. **Install dependencies**
```bash
    pip install -r requirements.txt
```
3. **Run the scraper**
```bash
    python main.py
```
4. **Open the notebook**
```
    jupyter notebook notebooks\BG_Tech_Jobs_Analysis.ipynb
```

## Author 
Corentin Dupriez - [GitHub](https://github.com/Corentin-dupriez)
