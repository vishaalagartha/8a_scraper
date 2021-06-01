from _8a_scraper.users import get_user_info, get_user_ascents

info = get_user_info('Vishaal Agartha')
print(info)

ascents = get_user_ascents('Vishaal Agartha', 'bouldering')
print(ascents)

from _8a_scraper.ascents import get_ascents

climbers = get_ascents('Midnight Lightning', 'bouldering')
print(climbers)

# This code block shows how to export the data into a csv file
import csv
with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = climbers[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for climber in climbers:
        writer.writerow(climber)

