#!/usr/bin/python3

# import logging
# import numpy as np

import re
import json

from datetime import datetime

import argparse

from sensors_data.sensors import SensorGroup
from sensors_data.templates import SensorTemplate, SensorType, DataType, DataOrder, DataFormat
from sensors_data.converters import ConvertersValue

############################################################
"""
Восходящий канал. Формат данных. Принцип декодирования.

Все данные от датчиков. Значения параметров, и события включаются в восходящую посылку
Максимальный объём данных 51 байт.  Лишние будут отсекаться. Младший байт идет первым.
Первые пять байт передаются всегда. Их порядок не изменен. Остальные, согласно битам регистра статуса данных в этой посылке.

Формат посылки:

Байт #1 и #2 - Статус данных, подключенных к восходящему каналу. Описывает правило декодирования.

 Бит #0 - Включена передача времени - 7 байт в формате 12:59:25 1-02-24#1 Час:мин:сек  день–месяц–год# день недели(1- понедельник)

 Бит #1 - Включена передача температуры датчика DS18B20 в формате int16 с фиксированной точкой 0,1 град С.
 Допустимые значения от -550 до +1250, что равно -55,0 + 125,0 град. Если датчик неисправен, то значение -32767.

 Бит #2 - Включена передача температуры датчика SI7021 (SHT21) в формате int16 с фиксированной точкой 0,1 град С.
 Допустимые значения от -550 до +1250, что равно -55,0 + 125,0 град. Если датчик неисправен, то значение -32767.

 Бит #3 - Включена передача влажности датчика SI7021 (SHT21) в формате int16 с фиксированной точкой 0,1 %.
 Допустимые значения от 0 до 999, что равно 0.0% - 99.9% Если датчик неисправен, то значение -32767.

 Бит #4 - Включена передача температуры датчика AM2302/DHT22 в формате int16 с фиксированной точкой 0,1 град С.
 Допустимые значения от -550 до +1250, что равно -55,0 + 125,0 град. Если датчик неисправен, то значение -32767.

 Бит #5 - Включена передача влажности датчика AM2302/DHT22 в формате int16 с фиксированной точкой 0,1 %.
 Допустимые значения от 0 до 999, что равно 0.0% - 99.9% Если датчик неисправен, то значение -32767.

 Бит #6 - Включена передача температуры датчика PT100 в формате int16 с фиксированной точкой 0,1 град С.
 Допустимые значения от -2500 до +9000, что равно -250,0 + 9000,0 град. Если датчик неисправен, то значение -32767.

 Бит #7 - Включена передача значения канала ADC#1 в формате int16. 0-1023

Байт №2 - старший:
 Бит #8 - Включена передача 3значения канала ADC#2 в формате int16. 0-1023
 Бит #9 - Включена передача значения канала ADC#3 в формате int16. 0-1023
 Бит #10 - Включена передача значения канала ADC#4 в формате int16. 0-1023
 Бит #11 - Включена передача значения канала DIN#1 - DIN#4, Включена передача значения канала датчика протечки и состояния реле - битовый регистр.
 Бит #12 - Включена передача значения канала Счетчика #1 в формате uint32
 Бит #13 - Включена передача значения канала Счетчика #2 в формате uint32
 Бит #14 - Включена передача значения канала Счетчика #3 в формате uint32
 Бит #15 - Включена передача значения канала Счетчика #4 в формате uint32
 
 Примеры данных:
    data_1 = "FECF0B00000C080A01021501E900EF00B101CC00FF0357017F000030"
    data_2 = "000C000000BC002D01"
    data_3 = "C50E0000009CFF9DFFCF02"

"""


def log_reader(file_name=""):
    file_ = 'interface_2020.02.01.txt'

    str_list = list()
    # open(file).read().split('\n')
    # file.read().splitlines()
    try:
        with open(file_name) as file_handler:
            # str_list = file_handler.readlines()
            str_list = file_handler.read().splitlines()

    except IOError:
        print("An IOError has occurred!")

    for str_ in str_list:
        # print(str_)
        data_str = re.search(r'(^dev/\w+/\w+)({.+)$', str_)

        if data_str:
            i = 0
            #print(str_)
            try:
                data_json = data_str.group(2).strip()
                #print(data_json)
                data_dict = json.loads(data_json)
                #print(data_dict['data'])

                #print(data_dict.keys())
                if 'deviceName' in data_dict:
                    print("Device Name: ", data_dict['deviceName'])

                if 'timestamp' in data_dict:
                    print("Date and Time: ", datetime.fromtimestamp(data_dict['timestamp']))

                if 'data' in data_dict:
                    string_reader(string_data=data_dict['data'])
                    print("\n")

            except:
                print("Error read data from log!")


def string_reader(string_data=""):
    if len(string_data) == 0:
        pass
        return

    # data_1 = "FECF0B00000C080A01021501E900EF00B101CC00FF0357017F000030"
    # data_2 = "000C000000BC002D01"
    # data_3 = "C50E0000009CFF9DFFCF02"

    try:
        sensor_group = SensorGroup(data=string_data)
        # print(sensor_group.data)
        # print(sensor_group.status_data)
        # print(sensor_group.status.unsigned_bites)
    except:
        print("Error create SensorGroup() object - perhaps incorrect data")
    else:
        try:
            sensor_group.read()
        except:
            print("Error read SensorGroup() object - perhaps incorrect data")
        else:

            # for k,v in sensor_group.data_dict.items():
            #    pass
            #    print(k, v)

            # print(sensor_group.sensor_template.data.value[0]['size'])
            # print(SensorTemplate.data.value)
            # print(SensorTemplate.head.value)

            for k, v in sensor_group.sensor_dict.items():
                pass
                # print(k, v.info['type'], v.data_human, v.data_int)
                print(k, v.info['type'], v.data_human, v.info['unit'])

            # cv = ConvertValue(data_input="0C080A01021501", data_format=DataFormat.Int8, data_order=DataOrder.Direct, data_type=DataType.DateTime)
            # cv.get()


def main():
    # cfg = CfgYaml(cfg_file="/opt/mtm/etc/mtm.yaml").get_cfg()

    parser = argparse.ArgumentParser(
        prog='Sensors Reader',
        description='Read data from sensors',
        epilog='(c) Robomak'

    )

    parser.add_argument('-s', '--string_data', help='String of data')
    parser.add_argument('-f', '--file_log', help='File.log')
    args = parser.parse_args()

    # if not vars(args):

    if args.string_data is None and args.file_log is None:
        # print(args)
        parser.print_usage()
    else:
        pass
        # print(args)
        if args.string_data:
            # print(args.string_data)
            string_reader(string_data=args.string_data)

        if args.file_log:
            # print(args.file_log)
            log_reader(file_name=args.file_log)

    # log_reader(file_name="sensors.log")


if __name__ == '__main__':
    main()
