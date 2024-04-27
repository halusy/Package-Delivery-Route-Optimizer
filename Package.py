import datetime


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, notes, packageStatus, timeDeparted,
                 timeDelivered, truckLoaded):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.packageStatus = packageStatus  # at the hub, in transit, delivered
        self.timeDeparted = None  # from the hub
        self.timeDelivered = None  # function of when the truck reaches the package destination
        self.truckLoaded = None  # will update with the truck the package is loaded on

    def __str__(self):
        return (
            "ID: {}, Truck Loaded: {}, Address: {}, {}, {} {}, Delivery Deadline: {}, Package Weight: {}, "
            "Special Notes: {},"
            "Package Status: {}, Time Departed: {}, Time Delivered: {}.").format(self.id, self.truckLoaded,
                                                                                 self.address,
                                                                                 self.city, self.state,
                                                                                 self.zip, self.deadline,
                                                                                 self.weight, self.notes,
                                                                                 self.packageStatus,
                                                                                 self.timeDeparted,
                                                                                 self.timeDelivered)

    def statusHelper(self, statusTime):
        if self.timeDelivered < statusTime:
            self.packageStatus = "Delivered"
        elif self.timeDeparted < statusTime:
            self.packageStatus = "In Transit"
        elif self.timeDeparted > statusTime:
            self.packageStatus = "At the Hub"
        if self.id == '9':
            if statusTime > datetime.timedelta(hours=10, minutes=20):
                self.address = "410 S State St"
                self.zip = "84103"
