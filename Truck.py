class Truck:
    def __init__(self, truckNumber, speed, milesDriven, location, currentTime, timeDeparted, packagesDelivered):
        self.truckNumber = truckNumber
        self.speed = speed
        self.milesDriven = milesDriven
        self.location = location
        self.timeDeparted = timeDeparted
        self.currentTime = timeDeparted
        self.packagesDelivered = packagesDelivered

    def __str__(self):
        return ("Truck Number: {}, Speed: {}, Miles Driven: {}, Current Location: {}, Time Departed: {}, "
                "Current Time: {} Packages "
                "Delivered: {}").format(self.truckNumber,
                                        self.speed, self.milesDriven, self.location, self.timeDeparted,
                                        self.currentTime,
                                        self.packagesDelivered)
