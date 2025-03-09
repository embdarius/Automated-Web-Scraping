def scrape_listings():

    listings_found = []
    import re
    url = ""

    ua = UserAgent()
    headers = {
        "User-Agent": ua.random
    }
    response = requests.get(url, headers=headers)
    print("Response: " + str(response))
    if "<Response [200]>" in str(response):
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        vehicles = soup.find_all('article', class_='list-entry g-row')
        vehicles_promoted = soup.find_all('section', class_='list-entry g-row')
        print(len(vehicles) + len(vehicles_promoted))

        for vehicle in vehicles:
            vehicle_tag = vehicle.find('a', class_='vehicle-data')
            listing_id  = vehicle_tag['data-vehicle-id']
            title = vehicle_tag.find('h3', class_='vehicle-title').text.strip().replace("Nou", "")
            price = vehicle_tag.find('p', class_='seller-currency').text.strip()
            cleaned_price = re.sub(r'\D', '', price)
            mileage_year = vehicle_tag.find('p', class_= 'u-text-bold').text.strip()
            mileage = 'unknown'
            registration = 'unknown'
            if ',' in mileage_year:
                registration, mileage = mileage_year.split(',')
                registration = registration.strip()
                mileage = mileage.strip()
                registration = registration.replace('/', '-').strip()
                mileage = re.sub(r'\D', '', mileage.strip())
    ............................................................
    .............................................................
    .............................................................
return listings_found 

# Function definition for scraping left incomplete on purpose
