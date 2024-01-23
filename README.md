# LinkedIn Job Scraper

LinkedIn Job Scraper is a Python script designed to streamline the process of scraping job listings from LinkedIn. The script employs Selenium for web automation and BeautifulSoup for HTML parsing. The workflow involves an initial authentication step where the user logs into their LinkedIn account. The script then gathers cookies for authentication, navigates to the jobs section, and systematically extracts information about available job positions.

---


## Introduction

LinkedIn Job Scraper is designed to simplify the process of gathering job information from LinkedIn. The script automates the initial authentication, leveraging cookies for seamless access to LinkedIn's job listings. Whether you are a job seeker or a data enthusiast, this script can help you collect data on job titles, company names, locations, and links to job listings.

---

## Technologies Used

- **Python**: The primary programming language used for scripting.
- **Selenium**: Web automation for interacting with LinkedIn.
- **BeautifulSoup**: HTML parsing for extracting job details.

---

## Getting Started

### Prerequisites

- Python installed on your machine.


### Installation

1. Clone the repository:


    git clone https://github.com/ma1lor/linkedin-job-scraper.git


2. Navigate to the project directory:

    cd linkedin-job-scraper


3. Install dependencies:


    pip install -r requirements.txt


---

## Usage

1. Run the main script:


    python main.py


2. The script will open a browser window, log in to LinkedIn, gather cookies for authentication, and start scraping job listings. The extracted data will be saved in the `data.json` file.

---

## File Structure

- **main.py**: Main entry point of the application.
- **first_auth.py**: Handles the initial authentication process, gathering cookies for subsequent use.
- **auth.py**: Contains logging details for users and drivers.
- **driver.py**: Module for getting the web driver.


---
