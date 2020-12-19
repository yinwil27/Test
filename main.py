import csv
import CSVReader
import HashMap

FirstTime = CSVReader.Ride1[2]
o = min(str(FirstTime))


def dropOff1(packageCount):
    while packageCount > 0:
        print("dropoff")
        print(o)
        as_list = list(FirstTime)
        as_list.pop[o]
        packageCount - 1


print(dropOff1(12))

'''
SecondTime = CSVReader.Ride2
p = min(str(SecondTime))
for p in SecondTime:
    print("Ride2")
    print(p)

ThirdTime = CSVReader.Ride3
q = min(str(ThirdTime))
for q in ThirdTime:
    print("Ride3")
    print(q)

''
h.add("1", "195 W Oakland Ave	Salt Lake City	UT 84115")
h.add('2', '2530 S 500 E	Salt Lake City	UT	84106')
h.add('3', '233 Canyon Rd	Salt Lake City	UT	84103')
h.add('4', '380 W 2880 S	Salt Lake City	UT	84115')
h.add('5', '410 S State St	Salt Lake City	UT	84111')
h.add('6', '3060 Lester St	West Valley City	UT	84119')
h.add('7', '1330 2100 S	Salt Lake City	UT	84106')
h.add('8', '300 State St	Salt Lake City	UT	84103')
h.add('9', '410 S State St Salt Lake City UT 84111')
h.add('10', '600 E 900 South	Salt Lake City	UT	84105')
h.add('11', '2600 Taylorsville Blvd	Salt Lake City	UT	84118')
h.add('12', '3575 W Valley Central Station bus Loop	West Valley City	UT	84119')
h.add('13', '2010 W 500 S	Salt Lake City	UT	84104')
h.add('14', '4300 S 1300 E	Millcreek	UT	84117')
h.add('15', '4580 S 2300 E	Holladay	UT	84117')
h.add('16', '4580 S 2300 E	Holladay	UT	84117')
h.add('17', '3148 S 1100 W	Salt Lake City	UT	84119')
h.add('18', '1488 4800 S	Salt Lake City	UT	84123')
h.add('19', '177 W Price Ave	Salt Lake City	UT	84115')
h.add('20', '3595 Main St	Salt Lake City	UT	84115')
h.add('21', '3595 Main St	Salt Lake City	UT	84115')
h.add('22', '6351 South 900 East	Murray	UT	84121')
h.add('23', '5100 South 2700 West	Salt Lake City	UT	84118')
h.add('24', '5025 State St	Murray	UT	84107')
h.add('25', '5383 South 900 East #104	Salt Lake City	UT	84117')
h.add('26', '5383 South 900 East #104	Salt Lake City	UT	84117')
h.add('27', '1060 Dalton Ave S	Salt Lake City	UT	84104')
h.add('28', '2835 Main St	Salt Lake City	UT	84115')
h.add('29', '1330 2100 S	Salt Lake City	UT	84106')
h.add('30', '300 State St	Salt Lake City	UT	84103')
h.add('31', '3365 S 900 W	Salt Lake City	UT	84119')
h.add('32', '3365 S 900 W	Salt Lake City	UT	84119')
h.add('33', '2530 S 500 E	Salt Lake City	UT	84106')
h.add('34', '4580 S 2300 E	Holladay	UT	84117')
h.add('35', '1060 Dalton Ave S	Salt Lake City	UT	84104')
h.add('36', '2300 Parkway Blvd	West Valley City	UT	84119')
h.add('37', '410 S State St	Salt Lake City	UT	84111')
h.add('38', '410 S State St	Salt Lake City	UT	84111')
h.add('39', '2010 W 500 S	Salt Lake City	UT	84104')
h.add('40', '380 W 2880 S	Salt Lake City	UT	84115')
h.print()

# create an algorithm that checks everything for the shortest distance from current location. recount, go again,
# shortest distance, count, go again Using holistic approach
Ride1 = [h.get('1'), h.get('13'), h.get('14'), h.get('15'), h.get('16'), h.get('17'), h.get('19'), h.get('30'),
         h.get('31'), h.get('34'), h.get('37'), h.get('40')]  # 8 am
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
'''
