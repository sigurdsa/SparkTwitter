__author__ = 'SigurdLap'
from collections import defaultdict


def flatten(x):
    result = []
    for el in x:
        # if isinstance(el, (list, tuple)):
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result


myFile = open('naiveBayesTest.txt', 'a')

file2list = []
with open('countryCodes.txt', 'r') as file2:  # make list

    for line in file2:
        line = line.replace('\"', '')
        file2list.append(line.splitlines())

file2list = flatten(file2list)

options = {"Pacific/Midway": '1', "Midway Island": '1', "American Samoa": '2',
           'Pacific/Pago_Pago': '3', "Hawaii": '3', "Alaska": '4',
           "Pacific Time (US & Canada)": '5', "Tijuana": '6',
           "Mountain Time (US & Canada)": '7', "Arizona": '8', "Chihuahua": '9',
           "Mazatlan": '10', "Central Time (US & Canada)": '11',
           "Saskatchewan": '12', "Guadalajara": '13', "Mexico City": '14',
           "Monterrey": '15', "Central America": '16',
           "Eastern Time (US & Canada)": '17', "Indiana (East)": '18',
           "Bogota": '19', "Lima": '20', "Quito": '21',
           "Atlantic Time (Canada)": '22', "Caracas": '23', "La Paz": '24',
           "Santiago": '25', "Newfoundland": '26', "Brasilia": '26',
           "Buenos Aires": '27', "Montevideo": '28', "Georgetown": '29',
           "Greenland": '30', "Mid-Atlantic": '31', "Azores": '32',
           "Cape Verde Is.": '33', "Dublin": '33', "Edinburgh": '34',
           "Lisbon": '35', "London": '36', "Casablanca": '37', "Monrovia": '38',
           "UTC": '39', "Belgrade": '40', "Bratislava": '41', "Budapest": '42',
           "Ljubljana": '43', "Prague": '44', "Sarajevo": '45', "Skopje": '47',
           "Warsaw": '48', "Zagreb": '49', "Brussels": '50', "Copenhagen": '51',
           "Madrid": '52', "Paris": '53', "Amsterdam": '54', "Berlin": '55',
           "Bern": '56', "Rome": '57', "Stockholm": '58', "Vienna": '59',
           "West Central Africa": '60', "Bucharest": '61', "Cairo": '62',
           "Helsinki": '63', "Europe/Helsinki": '63', "Kyiv": '64', "Riga": '65', "Sofia": '66',
           "Tallinn": '67', "Vilnius": '68', "Athens": '69', "Istanbul": '70',
           "Minsk": '71', "Jerusalem": '72', "Harare": '73', "Pretoria": '74',
           "Kaliningrad": '75', "Moscow": '76', "Kiev": '76', "St. Petersburg": '77',
           "Volgograd": '78', "Samara": '79', "Kuwait": '80', "Riyadh": '81', "Asia/Riyadh": '81',
           "Nairobi": '82', "Baghdad": '83', "Tehran": '84', "Abu Dhabi": '85',
           "Muscat": '86', "Baku": '87', "Tbilisi": '88', "Yerevan": '89',
           "Kabul": '90', "Ekaterinburg": '91', "Islamabad": '92',
           "Karachi": '93', 'Asia/Karachi': '93', "Tashkent": '94', "Chennai": '95', "Kolkata": '96',
           "Mumbai": '97', "New Delhi": '98', "Kathmandu": '99', "Asia/Kathmandu": '99',
           "Astana": '100', "Dhaka": '101', "Sri Jayawardenepura": '102', "Almaty": '103',
           "Novosibirsk": '104', "Rangoon": '105', "Bangkok": '106', "Hanoi": '107',
           "Jakarta": '108', "Krasnoyarsk": '109', "Beijing": '110',
           "Chongqing": '111', "Hong Kong": '112', "Urumqi": '113',
           "Kuala Lumpur": '114', "Asia/Kuala_Lumpur": '114', "Singapore": '115', "Taipei": '116',
           "Perth": '117', "Irkutsk": '118', "Ulaanbaatar": '119', "Ulaan Bataar": '119',
           "Seoul": '120',"Osaka": '121', "Sapporo": '122', "Tokyo": '123', "Yakutsk": '124',
           "Darwin": '125', "Adelaide": '126', "Canberra": '127',
           "Melbourne": '128', "Sydney": '129', "Brisbane": '130', "Hobart": '131',
           "Vladivostok": '132', "Guam": '133', "Port Moresby": '134',
           "Magadan": '135', "Srednekolymsk": '136', "Solomon Is.": '137',
           "New Caledonia": '138', "Fiji": '139', "Kamchatka": '140',
           "Marshall Is.": '141', "Auckland": '142', "Wellington": '143',
           "Nuku'alofa": '144', "Tokelau Is.": '145', "Chatham Is.": '146',
           "Samoa": '147', "Asia/Calcutta": '148', "Asia/Kolkata": '148',
           "International Date Line West": '149', "GMT+8": '150', "Asia/Dubai": '151',
           "Asia/Colombo": '152', "null": '500', "null,": '500'}

with open('exampleFilter3.txt', 'r') as file1:
    for line in file1:
        line = line.replace('\"', '')
        list_of_list = line.split(', ')
        for i, item in enumerate(file2list):
            if item in line:
                myFile.write(str(i))
                myFile.write(',')
                break

        if 'en' in list_of_list[4]:
            myFile.write('1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'ru' in list_of_list[4]:
            myFile.write('0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'uk' in list_of_list[4]:
            myFile.write('0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'th' in list_of_list[4]:
            myFile.write('0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'ar' in list_of_list[4]:
            myFile.write('0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'tr' in list_of_list[4]:
            myFile.write('0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'ja' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'es' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'id' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'msa' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'hi' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'zh-cn' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'fr' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'fa' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'pt' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'de' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0')
        elif 'ko' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0')
        elif 'zh-CN' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        elif 'zh-tw' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0')
        elif 'it' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0')
        elif 'ms' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0')
        elif 'mr' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0')
        elif 'vi' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0')
        elif 'da' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0')
        elif 'no' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0')
        elif 'nl' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0')
        elif 'pl' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0')
        elif 'fil' in list_of_list[4]:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1')
        else:
            myFile.write('0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')
        #myFile.write(' ')
        #myFile.write(options[list_of_list[5]])
        myFile.write('\n')
