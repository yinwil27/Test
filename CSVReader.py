import csv

import HashMap

GPSMatrix = []
# Read in csv file that is the mapping of distances between locations
with open('DistanceNumbers.csv') as csvfile:
    readCSV2 = csv.reader(csvfile, delimiter=',')
    readCSV2 = list(readCSV2)
    for row in readCSV2:
        GPS = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
               row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
               row[23], row[24], row[25], row[26]]
        GPSMatrix.append(row)
print("GPS Numbers")
print(GPSMatrix)
'''    for row in readCSV:
        print("row")
        print(row)
        print(row[0])
        print(row[0], row[1],row[2])

        package = [row[1],row[2],row[3],row[4],row[5],row[6], row[7] ,row[8]]
        h.add(row[0], package)
        #PackageID.append(PackageID)
        #Address.append(Address)'''
# Read in csv file that is the names of all possible delivery locations
Rolodex = []
RolodexAddressOnly = []
with open('DistanceApart.csv') as csv_name_file:
    readCSV3 = csv.reader(csv_name_file, delimiter=',')
    readCSV3 = list(readCSV3)
    for row in readCSV3:
        Book = [row[0], row[1], row[2]]

        Rolodex.append(row)
        RolodexAddressOnly.append(row[2])
print("GPS NAMES")
print(Rolodex)
print(RolodexAddressOnly)

PackageID = []
Address = []
h = HashMap.HashMap()
with open('WGUPS Package File.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        (' print("row")\n'
         '        print(row)\n'
         '        print(row[0])\n'
         '        print(row[0], row[1],row[2])\n')
        package = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]]
        h.add(row[0], package)
        PackageID.append(row[0])
        Address.append(package)

    print(PackageID)
    print(Address)
# Holistic Approach to loading packages onto truck
# create an algorithm that checks everything for the shortest distance from current location. recount, go again,
# shortest distance, count, go again Using holistic approach
Ride1 = [(h.get('1'), Rolodex[5][1], GPSMatrix[5][0]), (h.get('13'), Rolodex[6][1], GPSMatrix[6][0]),
         (h.get('14'), Rolodex[20][1], GPSMatrix[20][0]),
         (h.get('15'), Rolodex[21][1], GPSMatrix[21][0]), (h.get('16'), Rolodex[21][1], GPSMatrix[21][0]),
         (h.get('17'), Rolodex[14][1], GPSMatrix[14][0]), (h.get('19'), Rolodex[4][1], GPSMatrix[4][0]),
         (h.get('30'), Rolodex[12][1], GPSMatrix[12][0]), (h.get('31'), Rolodex[15][1], GPSMatrix[15][0]),
         (h.get('34'), Rolodex[21][1], GPSMatrix[21][0]), (h.get('37'), Rolodex[19][1], GPSMatrix[19][0]),
         (h.get('40'), Rolodex[18][1], GPSMatrix[18][0])]  # 8 am

Ride2 = [h.get('3'), h.get('6'), h.get('18'), h.get('25'), h.get('36'), h.get('38'), h.get('32'), h.get('33'),
         h.get('35'), h.get('39')]  # 9:06 am
Ride3 = [h.get('2'), h.get('4'), h.get('5'), h.get('7'), h.get('8'), h.get('9'), h.get('10'), h.get('11'),
         h.get('21'), h.get('22'), h.get('23'), h.get('24'), h.get('26'), h.get('27'), h.get('28')]  # 1021am

print("Truck1")
print(Ride1)

print("Truck2")
print(Ride2)

print("Truck1, 2nd Ride")
print(Ride3)

# Print GPS Matrix
for row in GPSMatrix:
    print(row)
for i in range(27):
    for j in range(27):
        print(GPSMatrix[i][j])


# '4001 South 700 East', '1060 Dalton Ave S',
def getDistance(fromAddress, toAddress):
    return GPSMatrix[RolodexAddressOnly.index(toAddress)][RolodexAddressOnly.index(fromAddress)]


print("Get Distance Results")
print(getDistance('4001 South 700 East', '1060 Dalton Ave S'))
