def get_job(soup): 
    
    """returns list of job titles from a soup object"""
    
    jobs = []
    for div in soup.find_all(name='div', attrs={'class':'row'}):
        for a in div.find_all(name='a', attrs={'data-tn-element':'jobTitle'}):
            jobs.append(a['title'])
    return(jobs)

def get_company(soup): 
    
    "returns list of job locations from a soup object"
    
    companies = []
    for div in soup.find_all(name='div', attrs={'class':'row'}):
        company = div.find_all(name='span', attrs={'class':'company'})
        if len(company) > 0:
            for b in company:
                companies.append(b.text.strip())
        else:
            sec_try = div.find_all(name='span', attrs={'class':'result-link-source'})
            for span in sec_try:
                companies.append(span.text.strip())
    return(companies)

def get_date(soup):
    
    """returns list of job dates from a soup object"""
    
    dates = []
    spans = soup.findAll('span', attrs={'class': 'date'})
    for span in spans:
        dates.append(span.text)
    return(dates)

def get_location(soup): 
    
    """returns list of job locations from a soup object"""
    
    locations = []
    spans = soup.findAll('span', attrs={'class': 'location'})
    for span in spans:
        locations.append(span.text)
    return(locations)