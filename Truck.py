import CSVReader
import HashMap

''''
loop through RolodexAddressOnly
start from Hub
call getDistance function for each element n RolodexAddressonly
find distance
assign minimum distance  minDistance
find address for minDistance and deliver
repeat this for all addresses 
if address is not in current truck, skip
'''
Truck1 = []
# for Truck1 in CSVReader.RolodexAddressOnly:
print("Package1's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '195 W Oakland Ave')))
print("Package13's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '2010 W 500 S')))
print("Package14's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '4300 S 1300 E')))
print("Package15's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '4580 S 2300 E')))
print("Package16's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '4580 S 2300 E')))
print("Package17's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '3148 S 1100 W')))
print("Package19's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '177 W Price Ave')))
print("Package30's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '300 State St')))
print("Package31's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '3365 S 900 W')))
print("Package34's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '4580 S 2300 E')))
print("Package37's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '410 S State St')))
print("Package40's distance is: " + str(CSVReader.getDistance('4001 South 700 East', '380 W 2880 S')))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '195 W Oakland Ave'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '2010 W 500 S'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '4300 S 1300 E'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '4580 S 2300 E'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '4580 S 2300 E'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '3148 S 1100 W'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '300 State St'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '3365 S 900 W'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '4580 S 2300 E'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '410 S State St'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '380 W 2880 S'))
Truck1.append(CSVReader.getDistance('4001 South 700 East', '177 W Price Ave'))
print(min(Truck1))
minDistance = min(Truck1)

'''print(CSVReader.getDistance(print(getDistance('4001 South 700 East', '1060 Dalton Ave S'))))'''


class Truck:
    def __init__(self):
        self.package_list = []
        self.size = 6
        self.Location = '4001 South 700 East'
        self.LeaveTime = 480
        self.CurrentTime = 480


    def deliveryminutes(mph):
            return CSVReader.getDistance('4001 South 700 East', '1060 Dalton Ave S') / mph

    def currentminutes(mph):
            return (CSVReader.getDistance('4001 South 700 East', '1060 Dalton Ave S') / mph) + Truck.CurrentTime

    # Package ID
    def deliver(self, packageID, h):
        package_list = h.get('5')
        
        ''' Get Address for the package object pacckage_list is the package object
        #find distance from the trucks location to the package's object address 
        #convert that distance to time
        '''
        return print("package :" + CSVReader.PackageID + "was delivered at")


h = HashMap.HashMap()
CSVReader.HashMaker(h)
truckAmazon = Truck()

print(truckAmazon.deliver(5, h))
