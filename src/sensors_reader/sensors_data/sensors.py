
from sensors_data.templates import SensorTemplate, SensorType, DataFormat, DataOrder, DataType
from sensors_data.converters import ConvertersValue


class Sensor:

    def __init__(self,

                 cfg_file="",
                 bit_id=0,
                 bit_value=0,
                 info=dict(),
                 data_input="",
                 ):

        self.cfg_file = cfg_file

        self.bit_id = bit_id
        self.bit_value = bit_value
        self.info = info
        self.data_input = data_input
        self.data_int = 0
        self.data_human = 0

    def read(self):
        pass
        d = ConvertersValue(data_input=self.data_input, data_format=self.info['format'],
                         data_order=self.info['data_order'], data_type=self.info['data_type'])
        d.get()
        if self.info['data_type'] == DataType.DateTime:
            pass
            #"Units destroyed: {players[0]}".format(players=[1, 2, 3])
            #self.data_human = "".join(map(str, d.direct_bytes_int))
            #self.data_human = " ".join(str(d.direct_bytes_int[1]))
            self.data_human = "{dt_str[0]}:{dt_str[1]}:{dt_str[2]} {dt_str[3]}-{dt_str[4]}-{dt_str[5]}#{dt_str[6]}".format(dt_str=d.direct_bytes_int)
            self.data_int = d.int
        if self.info['data_type'] == DataType.Digital:
            #d = SensorInt16(low_byte=self.data_input[0:2], high_byte=self.data_input[2:4])

            #print(d.low_byte, d.high_byte)
            #print(d.data_type)

            #d.get_int()

            self.data_int = d.int
            self.data_human = d.int
            if self.info['div'] > 1:
                self.data_human = d.int/self.info['div']
            if self.info['type'] == SensorType.BitRegister:
                pass
                #self.data_human = " ".join(map(str, d.unsigned_bites))

#data_2 = "FE CF 0B 00 00 0C 08 0A 01 02 15 01 E900EF00B101CC00FF0357017F000030"


class SensorGroup:

    def __init__(self,

                 cfg_file="",
                 data="",
                 sensor_template=SensorTemplate,
                 ):

        self.cfg_file = cfg_file

        self.data = data
        self.sensor_template = sensor_template
        self.data_template = sensor_template.data.value
        self.head_template = sensor_template.head.value
        self.status_template = sensor_template.status.value

        self.status_data = data[self.status_template['start']: self.status_template['start'] + self.status_template['size']]

        #self.status = SensorInt16(low_byte=self.status_data[0:2], high_byte=self.status_data[2:4])
        #self.status.get_int()

        self.status = ConvertersValue(data_input=self.status_data, data_format=DataFormat.Int16, data_order=DataOrder.Reverse, data_type=DataType.Digital)
        self.status.get()

        self.data_dict = dict()
        self.sensor_dict = dict()

    def read(self):
        pass
        # Получаем первое смещение (shift) от начала посылки до первого байта данных, равное размеру заголовка
        shift = self.head_template['size']
        #print("Shift", shift)
        for i in range(0, 16, 1):
            pass
            # Если бит выставлен, то значит данные соответствующего датчика присутствуют в посылке
            if self.status.unsigned_bites[i]:
                pass
                # Забираем байты данных для соответствующего датчика с учетом смещения и размера блока данных
                self.data_dict[i] = self.data[shift: shift + self.data_template[i]['size']]
                # Расчитываем смещение для следующих данных
                shift = shift + self.data_template[i]['size']
                # Формируем элемент словаря из данных датчика
                self.sensor_dict[i] = Sensor(bit_id=i, bit_value=self.status.unsigned_bites[i], info=self.data_template[i], data_input=self.data_dict[i])
                self.sensor_dict[i].read()




