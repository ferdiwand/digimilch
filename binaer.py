import binascii
import codecs


filePath = r"C:\Users\Lfl-WenzlFer\Desktop\TLG00001.BIN"

with open(filePath, 'rb') as data_file:
    data = data_file.read()
    print(data.decode('unicode-escape').encode('latin2').decode('utf-8'))


#f = codecs.open(filePath, encoding='utf-8')
#for line in f:
#    print(line)

#Str.decode(encoding='UTF-8',errors='strict')

#file = open(filePath, "rb")
#with file:
#       byte = file.read(1)
#       hexadecimal = binascii.hexlify(byte)
#       decimal = int(hexadecimal, 16)
#       binary = bin(decimal)[2:].zfill(8)
#       print("hex: %s, decimal: %s, binary: %s" % (hexadecimal, decimal, binary))
#        print("sdf")
#       print(byte)



