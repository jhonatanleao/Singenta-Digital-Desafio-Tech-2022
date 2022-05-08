from src.hotel import Hotel
import re

def convert_day(day):
    weekdays = "monday tuesday wednesday thursday friday"
    weekend = "saturday sunday"
    if day in weekdays:
        return 1
    elif day in weekend:
        return 2

def data_transformation(input, listHotel):
    colonSplit = input.split(':')
    listHotel[0] = colonSplit[0]
    regexResult = re.findall(r'\(([^()]*)\)', input)
    for day in regexResult:
        value = convert_day(day)
        if(value == 1):
            listHotel[1] += 1
        else:
            listHotel[2] += 1

def compute(listHotel, hotelPrice, hotels):
    if listHotel[0] in "Regular":
        for i in range(len(hotels)):
            hotelPrice[i] += hotels[i].weekdayRegular * listHotel[1]
            hotelPrice[i] += hotels[i].weekendRegular * listHotel[2]
    elif listHotel[0] in "Rewards":
        for i in range(len(hotels)):
            hotelPrice[i] += hotels[i].weekdayReward * listHotel[1]
            hotelPrice[i] += hotels[i].weekendReward * listHotel[2]       

def get_cheapest_hotel(number):   #DO NOT change the function's name
    lake = Hotel(nome = 'Lakewood', weekdayRegular = 110, weekdayReward = 80, weekendRegular = 90, weekendReward = 80)
    bridge = Hotel(nome = 'Bridgewood', weekdayRegular = 160, weekdayReward = 110, weekendRegular = 60, weekendReward = 50)
    ridge = Hotel(nome = 'Ridgewood', weekdayRegular = 220, weekdayReward = 100, weekendRegular = 150, weekendReward = 40)
    hotels = [lake, bridge, ridge]
    listHotel = ["", 0, 0]
    hotelPrice = [0,0,0]

    data_transformation(number, listHotel)
    compute(listHotel, hotelPrice, hotels)
    cheapestIndex = len(hotelPrice) - hotelPrice[::-1].index(min(hotelPrice)) - 1
    cheapest_hotel = hotels[cheapestIndex].nome
    return cheapest_hotel
