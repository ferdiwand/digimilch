import time
from datetime import date
from datetime import timedelta
import csv
today = date.today()
print(today)

filePath = r"C:\Users\Lfl-WenzlFer\Desktop\TLG00001.BIN"
ziel = r"C:\Users\Lfl-WenzlFer\Desktop\ferdi.csv"


fieldnames = ['milliseconds']
fieldnames.append('daysDelayed')
fieldnames.append('PositionNorth')
fieldnames.append('PositionEast')
fieldnames.append('PositionStatus')
fieldnames.append('NumberDLV')
fieldnames.append('massPerAreaYield')
fieldnames.append('massPerTimeYield')
fieldnames.append('ActualSpeed')
fieldnames.append('actPctCropDryMatter')
fieldnames.append('cropMoisture')
fieldnames.append('actualProteinContent')
fieldnames.append('milliseconds')
fieldnames.append('daysDelayed')
fieldnames.append('PositionNorth')
fieldnames.append('PositionEast')
fieldnames.append('PositionStatus')
fieldnames.append('NumberDLV')
fieldnames.append('fruchtart')
fieldnames.append('motordrehzahl')
fieldnames.append('ActRohprotein')
fieldnames.append('ActRohfaser')
fieldnames.append('ActRohasche')
fieldnames.append('ActRohfett')
fieldnames.append('ActRohzucker')


with open(filePath, 'rb') as data_file:
    with open(ziel, mode='w', newline='') as employee_file:
        writer = csv.DictWriter(employee_file, fieldnames=fieldnames)
        writer = csv.writer(employee_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(fieldnames)
        file_data = data_file.read()
        print(len(file_data))
        data = file_data[0:97]

        weiter = True
        i = 0
        while weiter:
            i = i + 1
            data = file_data[0:97]
            file_data = file_data[97:]
            if len(data) == 0:
                break
            else:
                print('Länge:', len(data))
                #print('Zeile: ', i)
                milliseconds = int.from_bytes(data[0:4], byteorder='little', signed=False)
                daysDelayed = int.from_bytes(data[4:6], byteorder='little', signed=False)
                PositionNorth = int.from_bytes(data[6:10], byteorder='little', signed=False)
                PositionEast = int.from_bytes(data[10:14], byteorder='little', signed=False)
                PositionStatus = int.from_bytes(data[14:15], byteorder='little', signed=False)
                NumberDLV = int.from_bytes(data[15:16], byteorder='little', signed=False)
                l = [milliseconds]
                l.append(daysDelayed)
                l.append(PositionNorth)
                l.append(PositionEast)
                l.append(PositionStatus)
                l.append(NumberDLV)


                DLV0 = int.from_bytes(data[16:17], byteorder='little', signed=False)
                DLV1 = int.from_bytes(data[21:22], byteorder='little', signed=False)
                DLV2 = int.from_bytes(data[26:27], byteorder='little', signed=False)
                DLV3 = int.from_bytes(data[31:32], byteorder='little', signed=False)
                DLV4 = int.from_bytes(data[36:37], byteorder='little', signed=False)
                DLV5 = int.from_bytes(data[41:42], byteorder='little', signed=False)




                #Standard
                massPerAreaYield = int.from_bytes(data[17:21], byteorder='little', signed=False)     #054
                massPerTimeYield = int.from_bytes(data[22:26], byteorder='little', signed=False)     #057
                ActualSpeed = int.from_bytes(data[27:31], byteorder='little', signed=False)          #18D
                actPctCropDryMatter = int.from_bytes(data[32:36], byteorder='little', signed=False)  #13A
                cropMoisture = int.from_bytes(data[37:41], byteorder='little', signed=False)         #063
                actualProteinContent = int.from_bytes(data[42:46], byteorder='little', signed=False) #196
                l.append(DLV0)
                l.append(massPerAreaYield)
                l.append(DLV1)
                l.append(massPerTimeYield)
                l.append(DLV2)
                l.append(ActualSpeed)
                l.append(DLV3)
                l.append(actPctCropDryMatter)
                l.append(DLV4)
                l.append(cropMoisture)
                l.append(DLV5)
                l.append(actualProteinContent)




                milliseconds = int.from_bytes(data[46:50], byteorder='little', signed=False)
                daysDelayed = int.from_bytes(data[50:52], byteorder='little', signed=False)
                PositionNorth = int.from_bytes(data[52:56], byteorder='little', signed=False)
                PositionEast = int.from_bytes(data[56:60], byteorder='little', signed=False)
                PositionStatus = int.from_bytes(data[60:61], byteorder='little', signed=False)
                NumberDLV = int.from_bytes(data[61:62], byteorder='little', signed=False)
                l.append(milliseconds)
                l.append(daysDelayed)
                l.append(PositionNorth)
                l.append(PositionEast)
                l.append(PositionStatus)
                l.append(NumberDLV)

                #Proprietär
                DLV02 = int.from_bytes(data[62:63], byteorder='little', signed=False)
                DLV12 = int.from_bytes(data[67:68], byteorder='little', signed=False)
                DLV22 = int.from_bytes(data[72:73], byteorder='little', signed=False)
                DLV32 = int.from_bytes(data[77:78], byteorder='little', signed=False)
                DLV42 = int.from_bytes(data[82:83], byteorder='little', signed=False)
                DLV52 = int.from_bytes(data[87:88], byteorder='little', signed=False)
                DLV62 = int.from_bytes(data[92:93], byteorder='little', signed=False)

                fruchtart     = int.from_bytes(data[63:67], byteorder='little', signed=False) #E104
                motordrehzahl = int.from_bytes(data[68:72], byteorder='little', signed=False) #E107
                ActRohprotein = int.from_bytes(data[73:77], byteorder='little', signed=False) #E122
                ActRohfaser   = int.from_bytes(data[78:82], byteorder='little', signed=False) #E123
                ActRohasche   = int.from_bytes(data[83:87], byteorder='little', signed=False) #E125
                ActRohfett    = int.from_bytes(data[88:92], byteorder='little', signed=False) #E126
                ActRohzucker  = int.from_bytes(data[93:97], byteorder='little', signed=False) #E127

                l.append(DLV02)
                l.append(fruchtart)
                l.append(DLV12)
                l.append(motordrehzahl)
                l.append(DLV22)
                l.append(ActRohprotein)
                l.append(DLV32)
                l.append(ActRohfaser)
                l.append(DLV42)
                l.append(ActRohasche)
                l.append(DLV52)
                l.append(ActRohfett)
                l.append(DLV62)
                l.append(ActRohzucker)




                startdatum = date(1980, 1, 1)
                neuesdatum = startdatum + timedelta(days=daysDelayed)
                print(neuesdatum)

                writer.writerow(l)
