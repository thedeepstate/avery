import json
import csv
import requests

def main():
    data = json.load(open("locations.json"))

    with open("locations.csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID','LATITUDE','LONGITUDE','URL','CITY','COUNTRY','LOCATION','TITLE','SUBTITLE'])
        for location in data:
            print('Processing %s' % location['id'])
            info_url = 'https://www.atlasobscura.com/places/%s.json?place_only=1' % location['id']
            r = requests.get(info_url)
            try:
                location_info = r.json()
                csvwriter.writerow([
                    location['id'],
                    location['lat'],
                    location['lng'],
                    location_info['url'],
                    location_info['city'],
                    location_info['country'],
                    location_info['location'],
                    location_info['title'],
                    location_info['subtitle']
                ])
            except Exception as e:
                print("Ummm... something went wrong with id: %s" % location['id'], e)

if __name__ == '__main__':
    main()
