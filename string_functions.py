from datetime import timedelta, datetime

def indeed_url_builder(what,where,date_posted, page):
    
    """
    a function that returns the URL of the page that needs to be scraped
    
    Params:
    
    what: the search (usually a job title)
    where: the job location
    date_posted: 1, 3, 7 , or 14 days
    page: the page of the search are we looking at (starts at 1) 
    
    Note: if given a page greater than the last page of the search, it will return the url of the last page of the search
    
    """
    
    base = 'http://www.indeed.com'
    q = what.replace(" ","+")
    l = where.replace(" ", "+")
    l = l.replace(",","%2C")
    start = (page - 1) * 10

    url = base + '/jobs?q='+ q + '&l=' + l + '&fromage=' + str(date_posted) + '&start=' + str(start)
    return url

def days_ago_to_date(days_ago):
    
    '''
    returns the actual date of an indeed date
    indeed dates are referenced relative to the current date
    This function finds the date relative to the reference date
    Example: '7 days ago' --> the actual date 7 days from the search
    
    '''
    
    today = datetime.now()
    n_days_ago = today - timedelta(days = days_ago)
    new_date = str(n_days_ago.month) + '/' +  str(n_days_ago.day) + '/' + str(n_days_ago.year)
    return new_date

def string_to_int(string):
    
    ''' returns the integer in a string. If there is no integer, it returns 0
        note: if string is '30+ days ago', function returns 30
    '''
    
    num = ''.join(filter(str.isdigit,string))
    if len(num) == 0:
        return 0
    else:
        return int(num)

def clean_jobs_dataframe(df,search):
    
    '''
    a function to help clean the jobs dataframe
    - correctly changes the relative date to the real date
    - deletes the old dates column
    - adds a columns filled with the job title that was searched
    '''
    
    dates = []
    for i in df['days_ago'].to_list():
        dates.append(days_ago_to_date(string_to_int(i)))

    df['date'] = dates
    del df['days_ago']
    
    df['search'] = search   
    return df