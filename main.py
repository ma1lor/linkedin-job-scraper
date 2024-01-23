from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pickle
from os import path
from bs4 import BeautifulSoup
import lxml
import json
from driver import get_driver
from first_auth import first_auth



vacancies_list = []

def saving_file(html_content, i):


    print('Saving html file...')
    with open(f"templates/page{i + 1}.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    
def opening_file(i):


    print('Opening html file...')
    with open(f"templates/page{i + 1}.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        return soup



def scroll_page(driver):
    print('Scrolling web element...')
    scroll_element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div')
    for i in range(5):
        driver.execute_script("arguments[0].scrollTop += 1000;",scroll_element)
    


def get_number_of_pages(html_content):

    soup = BeautifulSoup(html_content, 'html.parser')

    pages = soup.find_all('li', class_='artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view')

    if pages:
        last_page = pages[-1].text.strip()
        return int(last_page)
    else:
        return int(1)



def entering_site():

    try:
        driver = get_driver()
        driver.maximize_window()
        driver.get('https://www.linkedin.com/home')


        print('Loading cookies...')


        #getting cookies
        for cookie in pickle.load(open("cookies", "rb")):
            driver.add_cookie(cookie)
        

        # reloading page and going to /jobs/
        driver.refresh()
        driver.get('https://www.linkedin.com/jobs/')

        print('Pressing show more.')
        # Wait for the show more button
        print("Before clicking 'Show more'")
        show_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "discovery-templates-vertical-list__footer"))
        )
        print("Clicking 'Show more'")
        show_button.click()
        print("After clicking 'Show more'")




        # Wait for the show more to take effect
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search-results__list-item'))
        )



        # Scroll the page
        scroll_page(driver)

        # Get the HTML content of the page
        html_content = driver.page_source


        for i in range(get_number_of_pages(html_content)):
            if i != 0:
                scroll_page(driver)

            saving_file(html_content, i)
            soup = opening_file(i)



            print('Looking for jobs...')
            job_card_elements = soup.find_all('li', class_='jobs-search-results__list-item')        
            
            for job_card in job_card_elements:
                # Find elements using specific classes
                job_title_elem = job_card.find('a', class_='job-card-list__title')
                company_name_elem = job_card.find('div', class_='artdeco-entity-lockup__subtitle ember-view')
                location_elem = job_card.find('ul', class_='job-card-container__metadata-wrapper')
                link = f"https://www.linkedin.com{job_title_elem.get('href')}"
                

                job_title = job_title_elem.text.strip() if job_title_elem else 'No title'
                company_name = company_name_elem.text.strip() if company_name_elem else 'No company'
                location = location_elem.text.strip() if location_elem else 'No location'
                link = link if link else 'No link'

                # Append to vacancies_list
                vacancies_list.append({
                    'job_title': job_title,
                    'company_name': company_name,
                    'location': location,
                    'link': link
                })

            print("looking for page button")
            page_button = driver.find_elements(By.CLASS_NAME, "artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view")
            if len(page_button) != 0:
                page_button[i].click()

            else:
                print('Only one page.')
                


        # Dump the data to a JSON file
        print('Dumping into data.json...')
        json_file_path = 'data.json'
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(vacancies_list, json_file, ensure_ascii=False, indent=4)
        print('Script has run succesfully!')
        

            

    except Exception as ex:
        print(ex)



    finally:
        driver.close()
        driver.quit()


def main():
    if path.exists('cookies'):
        entering_site()
    else:
        if first_auth() == False:
            print('ERROR \nCheck your logging details.')
        else: entering_site()

        

if __name__ == "__main__":
    main()