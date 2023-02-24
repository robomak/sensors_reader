from sensors_data.templates import SensorTemplate, SensorType, DataFormat, DataOrder, DataType


class ConvertersValue:
    def __init__(self,
                 data_input="",
                 data_format=DataFormat.Int16,
                 data_order=DataOrder.Reverse,
                 data_type=DataType.Digital,
                 is_unsigned=False,
                 ):

        self.data_input = data_input
        self.data_format = data_format
        self.data_order = data_order
        self.data_type = data_type
        self.is_unsigned = is_unsigned

#        self.bytes_dict = dict()

        self.unsigned_int = 0
        self.unsigned_bites = [0] * 16
        self.reverse_unsigned_bites = [0] * 16

        self.int = 0
        self.int_bites = [0] * 16
        self.reverse_int_bites = [0] * 16
#        self.x = 0

        # Вычисляем количество байт (2 символа) в принятой строке для создания массива из байт
        self.byte_qnt = len(self.data_input) >> 1
        self.direct_bytes = [''] * self.byte_qnt
        self.reverse_bytes = [''] * self.byte_qnt

        self.direct_bytes_int = [0] * self.byte_qnt
        self.reverse_bytes_int = [0] * self.byte_qnt


        self.ini_bytes_array()

        self.reverse_data = ''.join(self.reverse_bytes)

        self.data_hex = self.data_input
        if self.data_order == DataOrder.Reverse:
            self.data_hex = self.reverse_data

    def ini_bytes_array(self):
        pass
        shift = 0
        size = 2
        y = self.byte_qnt - 1
        for i in range(0, self.byte_qnt, 1):
            #print(i)
            self.direct_bytes[i] = self.data_input[shift: shift + size]
            self.reverse_bytes[y] = self.direct_bytes[i]

            self.direct_bytes_int[i] = int(self.direct_bytes[i], base=16)
            self.reverse_bytes_int[y] = self.direct_bytes_int[i]

            shift = shift + size
            y = y - 1
            #print(self.direct_bytes[i])

    def get(self):

        if self.data_type == DataType.DateTime:
            pass
            self.get_int()

        if self.data_type == DataType.Digital:
            if self.data_format == DataFormat.Int16:
                pass
                self.get_int()

            if self.data_format == DataFormat.Int32:
                pass

    def get_str(self):
        pass
        #qnt_bites = 16

    def get_int(self):
        pass
        #qnt_bites = 16
        qnt_bites = self.data_format.value

        self.unsigned_int = int(self.data_hex, base=16)
        self.int = self.unsigned_int

        y = qnt_bites - 1
        for i in range(0, qnt_bites, 1):
            # print(i)
            self.unsigned_bites[i] = (self.unsigned_int >> i) & 0b1
            self.int_bites[i] = self.unsigned_bites[i]
            self.reverse_unsigned_bites[y] = self.unsigned_bites[i]
            self.reverse_int_bites[y] = self.unsigned_bites[i]
            y = y - 1

        if (not self.is_unsigned) and (self.unsigned_bites[15] == 1):
            pass
            # Дополнительный код двоичного числа определяется как величина, полученная вычитанием числа из наибольшей степени двух (из 2N для N-битного второго дополнения).
            # self.int = (0xFFFF - self.unsigned_int) * (-1)

            # Дополнительный код для отрицательного числа можно получить инвертированием его двоичного модуля и прибавлением к инверсии единицы, либо вычитанием числа из нуля.

            x = ~(self.unsigned_int - 1)
            self.int = 0
            for i in range(0, qnt_bites, 1):
                # print(i)
                self.int_bites[i] = (x >> i) & 0b1
                self.int = self.int + self.int_bites[i] * (2 ** i)

            self.int = self.int * (-1)

            y = qnt_bites - 1
            for i in range(0, qnt_bites, 1):
                self.reverse_int_bites[y] = self.int_bites[i]
                y = y - 1

        return self.int


class SensorInt16:
    def __init__(self,

                 low_byte="",
                 high_byte="",
                 is_unsigned=False,
                 ):

        self.bytes_dict = dict()
        self.is_unsigned = is_unsigned
        self.low_byte = low_byte
        self.high_byte = high_byte
        self.two_bytes = self.high_byte + self.low_byte
        self.unsigned_int = 0
        self.unsigned_bites = [0] * 16
        self.reverse_unsigned_bites = [0] * 16

        self.int = 0
        self.int_bites = [0] * 16
        self.x = 0

    def get_int(self):
        pass
        self.unsigned_int = int(self.two_bytes, base=16)
        self.int = self.unsigned_int

        n = 15
        y = 15
        for i in range(0, 16, 1):
            #print(i)
            self.unsigned_bites[i] = (self.unsigned_int >> i) & 0b1
            self.reverse_unsigned_bites[y] = self.unsigned_bites[i]
            y = y - 1

        if (not self.is_unsigned) and (self.unsigned_bites[15] == 1):
            pass
            # Дополнительный код двоичного числа определяется как величина, полученная вычитанием числа из наибольшей степени двух (из 2N для N-битного второго дополнения).
            # self.int = (0xFFFF - self.unsigned_int) * (-1)

            # Дополнительный код для отрицательного числа можно получить инвертированием его двоичного модуля и прибавлением к инверсии единицы, либо вычитанием числа из нуля.

            self.x = ~(self.unsigned_int - 1)
            self.int = 0
            for i in range(0, 16, 1):
                #print(i)
                self.int_bites[i] = (self.x >> i) & 0b1
                self.int = self.int + self.int_bites[i] * (2 ** i)

            self.int = self.int * (-1)

        return self.int

