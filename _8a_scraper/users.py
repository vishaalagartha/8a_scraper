import json, requests
from slugify import slugify
from bs4 import BeautifulSoup

try:
    from utils import login
except:
    from _8a_scraper.utils import login

def get_user_info(user):
    user = slugify(user)
    base_url = 'https://www.8a.nu/user/{}'
    user_url = base_url.format(user)
    r = requests.get(user_url)
    user_info = {'location': None, 'age': None, 'website': None,
                    'sponsors': None, 'started_climbing': None,
                    'occupation': None, 'other_interests': None,
                    'best_climbing_area': None, 'known_areas': None}

    if r.status_code==200:
        soup = BeautifulSoup(r.content, 'html.parser')
        top_div = soup.find('div', {'class': 'c-header-info'})
        sub_titles = top_div.find_all('p', {'class': 'sub-title'})
        for sub_title in sub_titles:
            if 'years old' in sub_title.text:
                age = int(sub_title.text.strip().replace('years old', ''))
                user_info['age'] = age
            else:
                user_info['location'] = sub_title.text.strip().replace(u'\xa0','')
        bottom_div = soup.find('div', {'class': 'user-info-body'})
        
        website_div = bottom_div.find('i', {'class': 'vl-website'})
        if website_div and len(website_div.text)>0:
            user_info['website'] = website_div.text.strip()
            
        for sponsor_div in bottom_div.find_all('div', {'class': 'sponsor-item'}):
            if not user_info['sponsors']:
                user_info['sponsors'] = []
            user_info['sponsors'].append(sponsor_div.text.strip())
        
        right_info = bottom_div.find_all('div', {'class': 'user-info-cell__right'})
        
        for i, div in enumerate(right_info):
            cell = div.find_all('div', {'class': 'cell'})[1]
            if i==0:
                user_info['started_climbing'] = cell.text.strip()
            elif i==1:
                user_info['occupation'] = cell.text.strip()
            elif i==2:
                user_info['other_interests'] = cell.text.strip()
            elif i==3:
                user_info['best_climbing_area'] = cell.text.strip()
            elif i==4:
                user_info['known_areas'] = cell.text.strip()
        
    return user_info


def get_recommended_ascents(user):
    user = slugify(user)
    driver = login()
    base_url = 'https://www.8a.nu/api/users/{}/recommended?pageSize=15&pageIndex={}'
    page_index = 0
    recommendations = []
    while True:
        url = base_url.format(user, page_index)
        driver.get(url)
        pre = driver.find_element_by_tag_name('pre').text
        data = json.loads(pre)
        if len(recommendations)<data['totalItems']:
            recommendations+=data['ascents']
            page_index+=1
        else:
            break
    driver.quit()
    return recommendations

def get_user_ascents(user, category):
    user = slugify(user)
    driver = login()
    base_url = 'https://www.8a.nu/api/users/{}/ascents?category={}&pageIndex={}&pageSize=50&sortfield=grade_desc&timeFilter=0&gradeFilter=0&typeFilter=&isAscented=true'
    ascents = []
    page_index = 0
    while True:
        url = base_url.format(user, category, page_index)
        driver.get(url)
        pre = driver.find_element_by_tag_name('pre').text
        data = json.loads(pre)
        if len(data['ascents'])==0:
            break
        else:
            ascents+=data['ascents']
            page_index+=1
    driver.quit()
    return ascents  
