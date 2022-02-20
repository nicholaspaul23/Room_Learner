import csv

filename = "room_data.csv"

def write_room_data(row):
    with open(filename, 'a') as roomDataFile:
        csvwriter = csv.writer(roomDataFile)
        csvwriter.writerows(row)