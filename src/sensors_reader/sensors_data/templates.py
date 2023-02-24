import enum


class SensorType(enum.Enum):
    DateTime = "Date_Time"
    Temperature = "Temperature"
    Humidity = "Humidity"
    BitRegister = "BitRegister"
    Other = "Other"


class SensorModel(enum.Enum):
    DS18B20 = "DS18B20"
    SI7021 = "SI7021 (SHT21)"
    AM2302 = "AM2302/DHT22"
    PT100 = "PT100"
    ADC = "ADC"
    DIN = "DIN"
    Counter = "Counter"
    Other = "Other"


class DataFormat(enum.Enum):
    Int8 = 8
    Int16 = 16
    Int32 = 32


class DataOrder(enum.Enum):
    Direct = 1
    Reverse = 2


class DataType(enum.Enum):
    DateTime = 1
    Digital = 2
    Bit = 3


class SensorTemplate(enum.Enum):
    head = {'start': 0, 'size': 10}
    status = {'start': 2, 'size': 4}
    data = {
            0: {
                'type': SensorType.DateTime,
                'description': "Date Time",
                'size': 14,
                'model': SensorModel.Other,
                'unit': "",
                'min': 0,
                'max': 0,
                'error': 0,
                'div': 1,
                'format': DataFormat.Int8,
                'data_order': DataOrder.Direct,
                'data_type': DataType.DateTime,
            },

            1: {
                'type': SensorType.Temperature,
                'description': "Temperature",
                'size': 4,
                'model': SensorModel.DS18B20,
                'unit': "C",
                'min': -550,
                'max': 1250,
                'error': -32767,
                'div': 10,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            2: {
                'type': SensorType.Temperature,
                'description': "Temperature",
                'size': 4,
                'model': SensorModel.SI7021,
                'unit': "C",
                'min': -550,
                'max': 1250,
                'error': -32767,
                'div': 10,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            3: {
                'type': SensorType.Humidity,
                'description': "Humidity",
                'size': 4,
                'model': SensorModel.SI7021,
                'unit': "%",
                'min': 0,
                'max': 999,
                'error': -32767,
                'div': 10,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            4: {
                'type': SensorType.Temperature,
                'description': "Temperature",
                'size': 4,
                'model': SensorModel.AM2302,
                'unit': "C",
                'min': -550,
                'max': 1250,
                'error': -32767,
                'div': 10,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            5: {
                'type': SensorType.Humidity,
                'description': "Humidity",
                'size': 4,
                'model': SensorModel.AM2302,
                'unit': "%",
                'min': 0,
                'max': 999,
                'error': -32767,
                'div': 10,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            6: {
                'type': SensorType.Temperature,
                'description': "Temperature",
                'size': 4,
                'model': SensorModel.PT100,
                'unit': "C",
                'min': -2500,
                'max': 9000,
                'error': -32767,
                'div': 10,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            7: {
                'type': SensorType.Other,
                'description': "ADC#1",
                'size': 4,
                'model': SensorModel.ADC,
                'unit': "",
                'min': 0,
                'max': 1023,
                'error': -32767,
                'div': 1,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            8: {
                'type': SensorType.Other,
                'description': "ADC#2",
                'size': 4,
                'model': SensorModel.ADC,
                'unit': "",
                'min': 0,
                'max': 1023,
                'error': -32767,
                'div': 1,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            9: {
                'type': SensorType.Other,
                'description': "ADC#3",
                'size': 4,
                'model': SensorModel.ADC,
                'unit': "",
                'min': 0,
                'max': 1023,
                'error': -32767,
                'div': 1,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            10: {
                'type': SensorType.Other,
                'description': "ADC#4",
                'size': 4,
                'model': SensorModel.ADC,
                'unit': "",
                'min': 0,
                'max': 1023,
                'error': -32767,
                'div': 1,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            11: {
                'type': SensorType.BitRegister,
                'description': "BitRegister DIN#1 - DIN#4",
                'size': 4,
                'model': SensorModel.DIN,
                'unit': "",
                'min': 0,
                'max': 0,
                'error': -32767,
                'div': 1,
                'format': DataFormat.Int16,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            12: {
                'type': SensorType.Other,
                'description': "Counter #1",
                'size': 8,
                'model': SensorModel.Counter,
                'unit': "",
                'min': 0,
                'max': 0,
                'error': -1,
                'div': 1,
                'format': DataFormat.Int32,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            13: {
                'type': SensorType.Other,
                'description': "Counter #2",
                'size': 8,
                'model': SensorModel.Counter,
                'unit': "",
                'min': 0,
                'max': 0,
                'error': -1,
                'div': 1,
                'format': DataFormat.Int32,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            14: {
                'type': SensorType.Other,
                'description': "Counter #3",
                'size': 8,
                'model': SensorModel.Counter,
                'unit': "",
                'min': 0,
                'max': 0,
                'error': -1,
                'div': 1,
                'format': DataFormat.Int32,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

            15: {
                'type': SensorType.Other,
                'description': "Counter #4",
                'size': 8,
                'model': SensorModel.Counter,
                'unit': "",
                'min': 0,
                'max': 0,
                'error': -1,
                'div': 1,
                'format': DataFormat.Int32,
                'data_order': DataOrder.Reverse,
                'data_type': DataType.Digital,
            },

        }