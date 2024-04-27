# Student: Nicholas Ryan
# Student ID: 009984406
# Project: DSA2 WGUPS Part 2
# Date: Dec 5th 2023

import csv
import datetime
from HashTable import HashTable
from Package import Package
from Truck import Truck

# load csv files

with open("CSV/DistanceFile.csv") as distFile:
    DistanceList = list(csv.reader(distFile))

with open("CSV/AddressFile.csv") as addFile:
    AddressList = list(csv.reader(addFile))

# init hash table for packages
packageHashTable = HashTable()


# this method helps me retain the fact that time is merely a mechanism of distance traveled within this project
# it takes the distance traveled of any given truck, and returns timedelta
def milesToTime(milesTraveled):
    timeInSeconds = milesTraveled * 200  # at 18mph, each mile take 3min 20sec which = 200sec
    formattedTime = datetime.timedelta(seconds=timeInSeconds)
    return formattedTime


# this method takes the package info from the CSV file and creates new package objects for each package,
# and adds the package objects to the previously created (and empty) hash table
def loadPackageFile(file):
    with open(file) as packageFile:
        packageData = csv.reader(packageFile)
        next(packageData)
        for packageList in packageData:
            packageID = packageList[0]
            packageAddress = packageList[1]
            packageCity = packageList[2]
            packageState = packageList[3]
            packageZip = packageList[4]
            packageDeadline = packageList[5]
            packageWeight = packageList[6]
            packageNotes = packageList[7]
            packageStatus = 'At Hub'  # init
            packageTimeDeparted = None  # init
            packageTimeDelivered = None  # init
            packageTruckLoaded = None   # init

            newPackage = Package(packageID, packageAddress, packageCity, packageState, packageZip, packageDeadline,
                                 packageWeight, packageNotes, packageStatus, packageTimeDeparted, packageTimeDelivered,
                                 packageTruckLoaded)

            packageHashTable.add(packageID, newPackage)


# calling the loadPackageFile method, passing in the Package CSV file

loadPackageFile('CSV/PackageFile.csv')

# created 3 truck objects with the current location (the hub), the speed of the truck, the time of departure from the
# hub, and the packages loaded.

truck1 = Truck(1, 18, 0.0, "4001 South 700 East", 0, datetime.timedelta(hours=8),
               ['1', '13', '14', '15', '16', '19', '20', '27', '29', '30', '31', '34', '37', '40'])
truck2 = Truck(2, 18, 0.0, "4001 South 700 East", 0, datetime.timedelta(hours=10, minutes=30),
               ['2', '3', '4', '5', '9', '18', '26', '28', '32', '35', '36', '38'])
truck3 = Truck(3, 18, 0.0, "4001 South 700 East", 0, datetime.timedelta(hours=9, minutes=5),
               ['6', '7', '8', '10', '11', '12', '17', '21', '22', '23', '24', '25', '33', '39'])


# this method takes an address string and returns the location of the address via an integer corresponding with the
# address table

def addressHelper(address):
    for table in AddressList:
        if address in table[2]:
            return int(table[0])


# this method takes two integers which represent addresses (which will always be returned by the addressHelper) and
# returns the distance between the two addresses utilizing pythons built in List traversal functionality

def distanceHelper(address1, address2):
    distance = DistanceList[address1][address2]
    if distance == '':
        distance = DistanceList[address2][address1]
    return float(distance)


# this is the main program method. it will be called passing in a truck object.
def deliveryAlgorithm(truck):
    toBeDelivered = []
    for packageID in truck.packagesDelivered:
        package = packageHashTable.get(packageID)
        toBeDelivered.append(package)
    truck.packagesDelivered.clear()
    truck.currentTime = truck.timeDeparted
    # nearest neighbor algorithm implementation
    while len(toBeDelivered) > 0:
        nextAddress = 10000
        nextPackage = None
        for package in toBeDelivered:
            if distanceHelper(addressHelper(truck.location), addressHelper(package.address)) <= nextAddress:
                nextPackage = package
                nextAddress = distanceHelper(addressHelper(truck.location), addressHelper(package.address))
        toBeDelivered.remove(nextPackage)
        truck.packagesDelivered.append(nextPackage.id)
        truck.milesDriven += nextAddress
        truck.currentTime += milesToTime(nextAddress)
        nextPackage.timeDelivered = truck.currentTime
        nextPackage.timeDeparted = truck.timeDeparted
        nextPackage.truckLoaded = truck.truckNumber
        truck.location = nextPackage.address


deliveryAlgorithm(truck1)
deliveryAlgorithm(truck2)
# ensures truck3 uses the driver who returns first between truck1 and truck2
truck3.timeDeparted = min(truck1.currentTime, truck2.currentTime)
deliveryAlgorithm(truck3)


class Main:
    print("Welcome to the WGUPS Delivery Program \nTotal Miles Traveled: {}".format(
        truck1.milesDriven + truck2.milesDriven + truck3.milesDriven))
    text = input("Press Enter to Continue:")
    try:
        time_input = input("Enter a time to check the status of the packages (HH:MM:SS): ")
        (hours, minutes, seconds) = time_input.split(":")
        statusTime = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
        allorindividual = input(
            "To see the status of a particular package, please enter the package ID (00). To see the ""status of all "
            "packages, enter 'all': ")

        if allorindividual == 'all':
            for packageID in range(1, 41):
                package = packageHashTable.get(str(packageID))
                package.statusHelper(statusTime)
                print(str(package))
        elif int(allorindividual) >= 0 or int(allorindividual) <= 40:
            package = packageHashTable.get(allorindividual)
            package.statusHelper(statusTime)
            print(str(package))
        else:
            print("Error. Incorrect input. Please Try Again")

    except ValueError:
        print("Invalid Time. Try Again")
