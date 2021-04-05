from get_functions import get_company,get_date, get_job, get_location
from string_functions import indeed_url_builder, clean_jobs_dataframe
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import requests

def scrape_jobs(location,search, debug = False):
    
    '''
    a function that returns a pandas dataframe filled with the jobs from a search
    
    params:
    
    location: where we want the results from
    search: what we are searching (usually job titles)
    
    '''
    
    w = []
    x = []
    y = []
    z = []


    num_of_pages = 1
    for i in range(1,num_of_pages+1): #daily scraper only does the first page

        URL =  indeed_url_builder(search, location, i, 1)
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")

        p1 = get_job(soup)
        p2 = get_company(soup)
        p3 = get_location(soup)
        p4 = get_date(soup)

        w = w + p1    
        x = x + p2
        y = y + p3
        z = z + p4

        sleep(1)

    columns = ['title','company','location','days_ago']
    df = pd.DataFrame(list(zip(w,x,y,z)),columns = columns)
    
    if debug == True:
        
        print(str(len(df)) + ' jobs scraped')
        if len(df) == 0:
            print('either zero jobs were contained in the search or url blocked IP address')
    return df

    
def scrape_many_jobs(cities,searches):
    
    """
    a function that returns a dataframe filled with job entries from multiple cities and searches
    
    parameters:
    
    cities: a list whose entries are the places we want to search
    searches: a list whose entries are the job titles we want to search
    
    """
    df = pd.DataFrame(columns = ['title', 'company','location','date','search'])

    for city in cities:
        for search in searches:
            temp_df = scrape_jobs(city,search)
            temp_df = clean_jobs_dataframe(temp_df,search)
            df = pd.concat([df,temp_df])
        
    print(str(len(df)) + ' seaches returned by searching for ' + str(len(searches)) + ' jobs in ' + str(len(cities)) + ' cities')
    return df