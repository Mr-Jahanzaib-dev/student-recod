import math
class Driver:
    def __init__(self, driver_id, name, location):
        self.driver = {
            "driver_id": driver_id,
            "name": name,
            "location": location,
            "availability": True,
            "rating": 5.0,
            "rides_completed": 0
        }

class Rider:
    def __init__(self, rider_id, name, location):
        self.rider = {
            "rider_id": rider_id,
            "name": name,
            "location": location
        }

class RideRequest:
    def __init__(self, request_id, rider_id, pickup, drop, status, driver_id, fare):
        self.request = {
            "request_id": request_id,
            "rider_id": rider_id,
            "pickup": pickup,
            "drop": drop,
            "status": status,
            "driver_id": driver_id,
            "fare": fare
        }

class datamanager:
    def check_data(name):
        with open(f"{name}.csv", "r") as file:
            return file.readlines()

    def fetch_driver():
        data = datamanager.check_data("driver")
        record = []
        if data:
            for line in data:
                parts = line.strip().split(",")
                driver_id = parts[0]
                name = parts[1]
                x = int(parts[2])
                y = int(parts[3])
                availability = parts[4] == "True"
                rating = float(parts[5])
                rides_completed = int(parts[6])
                driver = {
                    "driver_id": driver_id,
                    "name": name,
                    "location": (x, y),
                    "availability": availability,
                    "rating": rating,
                    "rides_completed": rides_completed
                }
                record.append(driver)
        return record

    def write_driver(record):
        with open("driver.csv", "w") as file:
            for driver in record:
                x, y = driver['location']
                line = (
                    f"{driver['driver_id']},"
                    f"{driver['name']},"
                    f"{x},{y},"
                    f"{driver['availability']},"
                    f"{driver['rating']},"
                    f"{driver['rides_completed']}\n"
                )
                file.write(line)

    def fetch_rider():
        data = datamanager.check_data("rider")
        record = []
        if data:
            for line in data:
                parts = line.strip().split(",")
                rider_id = parts[0]
                name = parts[1]
                x = int(parts[2])
                y = int(parts[3])
                rider = {
                    "rider_id": rider_id,
                    "name": name,
                    "location": (x, y)
                }
                record.append(rider)
        return record

    def write_rider(record):
        with open("rider.csv", "w") as file:
            for rider in record:
                x, y = rider['location']
                line = f"{rider['rider_id']},{rider['name']},{x},{y}\n"
                file.write(line)

    def fetch_ride_request():
        data = datamanager.check_data("ride_request")
        record = []
        if data:
            for line in data:
                parts = line.strip().split(",")
                request_id = parts[0]
                rider_id = parts[1]
                pickup_x = int(parts[2])
                pickup_y = int(parts[3])
                drop_x = int(parts[4])
                drop_y = int(parts[5])
                status = parts[6]
                driver_id = parts[7]
                fare = float(parts[8])
                req = RideRequest(
                    request_id,
                    rider_id,
                    (pickup_x, pickup_y),
                    (drop_x, drop_y),
                    status,
                    driver_id,
                    fare
                )
                record.append(req.request)
        return record

    def write_ride_request(record):
        with open("ride_request.csv", "w") as file:
            for req in record:
                px, py = req['pickup']
                dx, dy = req['drop']
                line = (
                    f"{req['request_id']},"
                    f"{req['rider_id']},"
                    f"{px},{py},"
                    f"{dx},{dy},"
                    f"{req['status']},"
                    f"{req['driver_id']},"
                    f"{req['fare']}\n"
                )
                file.write(line)


class functionalities:
    def add_driver():
        driver_data = datamanager.fetch_driver()
        while True:
            driver_id = input("\nPlease Enter the Driver ID: ")
            found = False
            for driver in driver_data:
                if driver['driver_id'] == driver_id:
                    found = True
                    break
            if found:
                print("\n\"Please Enter a Unique ID\"\n")
            else:
                if driver_id.upper()[0] == 'D' and driver_id[1:].isdigit():
                    break
                else:
                    print("\n\"Please Enter Driver ID in this Format D1, D2\"\n")
        while True:
            name = input("\nPlease Enter the Driver Name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("\nPlease Enter the Name in Alphabetic form\n")
        while True:
            try:
                x = int(input("\nPlease Enter the x Location: "))
                y = int(input("\nPlease Enter the y Location: "))
                break
            except ValueError:
                print("\n\"Please Enter the Location in Number form\"\n")
        drv = Driver(driver_id, name, (x, y))
        driver_data.append(drv.driver)
        datamanager.write_driver(driver_data)
        print("\n\"Driver Added Successfully\"\n")

        while True:
            nxt = input("\nEnter \"Y\" For Adding More Driver \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.add_driver()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def add_rider():
        rider_data = datamanager.fetch_rider()
        while True:
            rider_id = input("\nPlease Enter the Rider ID: ")
            found = False
            for rider in rider_data:
                if rider['rider_id'] == rider_id:
                    found = True
                    break
            if found:
                print("\n\"Please Enter a Unique ID\"\n")
            else:
                if rider_id.upper()[0] == 'R' and rider_id[1:].isdigit():
                    break
                else:
                    print("\n\"Please Enter Rider ID in this Format R1, R2\"\n")
        while True:
            name = input("\nPlease Enter the Rider Name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("\nPlease Enter the Name in Alphabetic form\n")
        while True:
            try:
                x = int(input("\nPlease Enter the x Location: "))
                y = int(input("\nPlease Enter the y Location: "))
                break
            except ValueError:
                print("\n\"Please Enter the Location in Number form\"\n")
        rdr = Rider(rider_id, name, (x, y))
        rider_data.append(rdr.rider)
        datamanager.write_rider(rider_data)
        print("\n\"Rider Added Successfully\"\n")

        while True:
            nxt = input("\nEnter \"Y\" For Adding More Rider \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.add_rider()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def request_ride():
        rider_data = datamanager.fetch_rider()
        request_data = datamanager.fetch_ride_request()
        while True:
            rider_id = input("\nPlease Enter Your Rider ID: ")
            rider_found = False
            for rider in rider_data:
                if rider['rider_id'].lower() == rider_id.lower():
                    rider_found = True
                    break
            if not rider_found:
                print("\n\"Rider ID Not Found\"\n")
            else:
                break
        while True:
            try:
                px = int(input("\nPlease Enter Pickup x Location: "))
                py = int(input("\nPlease Enter Pickup y Location: "))
                break
            except ValueError:
                print("\n\"Please Enter the Location in Number form\"\n")
        while True:
            try:
                dx = int(input("\nPlease Enter Drop x Location: "))
                dy = int(input("\nPlease Enter Drop y Location: "))
                break
            except ValueError:
                print("\n\"Please Enter the Location in Number form\"\n")
        while True:
            request_id = input("\nPlease Enter the Request ID (e.g. RQ1, RQ2): ")
            found = False
            for req in request_data:
                if req['request_id'].lower() == request_id.lower():
                    found = True
                    break
            if found:
                print("\n\"Please Enter a Unique Request ID\"\n")
            elif request_id.upper()[:2] == 'RQ' and request_id[2:].isdigit():
                break
            else:
                print("\n\"Please Enter Request ID in this Format RQ1, RQ2\"\n")

        fare = functionalities.calculate_fare((px, py), (dx, dy))
        req = RideRequest(request_id, rider_id, (px, py), (dx, dy), "Pending", "", fare)
        request_data.append(req.request)
        datamanager.write_ride_request(request_data)
        print(f"\n\"Ride Request Created Successfully! Estimated Fare: {fare}\"\n")

        while True:
            nxt = input("\nEnter \"Y\" For Adding More Request \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.request_ride()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def find_nearest_driver():
        driver_data = datamanager.fetch_driver()
        while True:
            try:
                px = int(input("\nPlease Enter Pickup x Location: "))
                py = int(input("\nPlease Enter Pickup y Location: "))
                break
            except ValueError:
                print("\n\"Please Enter the Location in Number form\"\n")
        pickup = (px, py)
        nearest = None
        min_dist = float('inf')
        for driver in driver_data:
            if driver['availability']:
                dist = functionalities.calculate_distance(driver['location'], pickup)
                if dist < min_dist:
                    min_dist = dist
                    nearest = driver
        if nearest:
            print(f"\nNearest Available Driver: {nearest['driver_id']} - {nearest['name']}")
            print(f"Distance: {min_dist} units | Rating: {nearest['rating']}\n")
        else:
            print("\n\"No Available Drivers Found\"\n")

        while True:
            nxt = input("\nEnter \"Y\" To Search Again \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.find_nearest_driver()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def match_driver():
        request_data = datamanager.fetch_ride_request()
        driver_data = datamanager.fetch_driver()
        request_id = input("\nPlease Enter the Request ID: ")
        request_found = False
        for req in request_data:
            if req['request_id'].lower() == request_id.lower():
                request_found = True
                if req['status'] != "Pending":
                    print(f"\n\"Request is already in '{req['status']}' state\"\n")
                    break
                nearest = None
                min_dist = float('inf')
                for driver in driver_data:
                    if driver['availability']:
                        dist = functionalities.calculate_distance(driver['location'], req['pickup'])
                        if dist < min_dist:
                            min_dist = dist
                            nearest = driver
                if nearest:
                    req['driver_id'] = nearest['driver_id']
                    req['status'] = "Matched"
                    nearest['availability'] = False
                    print(f"\n\"Driver {nearest['driver_id']} - {nearest['name']} Matched Successfully!\"\n")
                else:
                    print("\n\"No Available Drivers Found\"\n")
                break
        if not request_found:
            print("\n\"Request ID Not Found\"\n")
        datamanager.write_ride_request(request_data)
        datamanager.write_driver(driver_data)

        while True:
            nxt = input("\nEnter \"Y\" For Matching Another \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.match_driver()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def start_ride():
        request_data = datamanager.fetch_ride_request()
        request_id = input("\nPlease Enter the Request ID: ")
        request_found = False
        for req in request_data:
            if req['request_id'].lower() == request_id.lower():
                request_found = True
                if req['status'] != "Matched":
                    print(f"\n\"Cannot Start Ride. Current Status: '{req['status']}'. Must be Matched first.\"\n")
                else:
                    req['status'] = "In Progress"
                    print("\n\"Ride Started Successfully\"\n")
                break
        if not request_found:
            print("\n\"Request ID Not Found\"\n")
        datamanager.write_ride_request(request_data)

        while True:
            nxt = input("\nEnter \"Y\" To Start Another Ride \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.start_ride()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def complete_ride():
        request_data = datamanager.fetch_ride_request()
        driver_data = datamanager.fetch_driver()
        request_id = input("\nPlease Enter the Request ID: ")
        request_found = False
        for req in request_data:
            if req['request_id'].lower() == request_id.lower():
                request_found = True
                if req['status'] != "In Progress":
                    print(f"\n\"Cannot Complete Ride. Current Status: '{req['status']}'. Must be In Progress.\"\n")
                else:
                    req['status'] = "Completed"
                    for driver in driver_data:
                        if driver['driver_id'] == req['driver_id']:
                            driver['availability'] = True
                            driver['rides_completed'] += 1
                            break
                    print(f"\n\"Ride Completed Successfully! Fare: {req['fare']}\"\n")
                break
        if not request_found:
            print("\n\"Request ID Not Found\"\n")
        datamanager.write_ride_request(request_data)
        datamanager.write_driver(driver_data)

        while True:
            nxt = input("\nEnter \"Y\" To Complete Another Ride \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.complete_ride()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def cancel_ride():
        request_data = datamanager.fetch_ride_request()
        driver_data = datamanager.fetch_driver()
        request_id = input("\nPlease Enter the Request ID: ")
        request_found = False
        for req in request_data:
            if req['request_id'].lower() == request_id.lower():
                request_found = True
                if req['status'] in ["Completed", "Cancelled"]:
                    print(f"\n\"Ride is Already '{req['status']}' and Cannot be Cancelled\"\n")
                else:
                    if req['driver_id']:
                        for driver in driver_data:
                            if driver['driver_id'] == req['driver_id']:
                                driver['availability'] = True
                                break
                    req['status'] = "Cancelled"
                    print("\n\"Ride Cancelled Successfully\"\n")
                break
        if not request_found:
            print("\n\"Request ID Not Found\"\n")
        datamanager.write_ride_request(request_data)
        datamanager.write_driver(driver_data)

        while True:
            nxt = input("\nEnter \"Y\" To Cancel Another Ride \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.cancel_ride()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def rate_driver():
        request_data = datamanager.fetch_ride_request()
        driver_data = datamanager.fetch_driver()
        request_id = input("\nPlease Enter the Request ID: ")
        request_found = False
        for req in request_data:
            if req['request_id'].lower() == request_id.lower():
                request_found = True
                if req['status'] != "Completed":
                    print("\n\"You Can Only Rate a Completed Ride\"\n")
                elif not req['driver_id']:
                    print("\n\"No Driver Assigned to This Ride\"\n")
                else:
                    while True:
                        try:
                            rating = float(input("\nPlease Enter Rating (1.0 - 5.0): "))
                            if 1.0 <= rating <= 5.0:
                                break
                            else:
                                print("\nPlease Enter a Rating Between 1.0 and 5.0\n")
                        except ValueError:
                            print("\nPlease Enter the Rating in Numeric Form\n")
                    for driver in driver_data:
                        if driver['driver_id'] == req['driver_id']:
                            total = driver['rating'] * driver['rides_completed']
                            driver['rating'] = round((total + rating) / (driver['rides_completed'] + 1), 2) if driver['rides_completed'] > 0 else rating
                            print(f"\n\"Driver {driver['driver_id']} Rated {rating}. New Average: {driver['rating']}\"\n")
                            break
                break
        if not request_found:
            print("\n\"Request ID Not Found\"\n")
        datamanager.write_driver(driver_data)

        while True:
            nxt = input("\nEnter \"Y\" To Rate Another Driver \"N\" For Main Menu\n  ")
            if nxt.lower() == 'y':
                functionalities.rate_driver()
                break
            elif nxt.lower() == 'n':
                main_menu()
                break
            else:
                print("\nPlease Enter Y or N\n")

    def calculate_distance(loc1, loc2):
        x1, y1 = loc1
        x2, y2 = loc2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return round(distance, 2)

    def calculate_fare(pickup, drop):
        base_fare = 50
        per_unit = 10
        distance = functionalities.calculate_distance(pickup, drop)
        fare = base_fare + round(distance * per_unit, 2)
        return fare


def main_menu():
    while True:
        print("\n========== RIDE SHARING MANAGEMENT SYSTEM ==========")
        print("1.  Add Driver")
        print("2.  Add Rider")
        print("3.  Request Ride")
        print("4.  Find Nearest Driver")
        print("5.  Match Driver")
        print("6.  Start Ride")
        print("7.  Complete Ride")
        print("8.  Cancel Ride")
        print("9.  Rate Driver")
        while True:
            try:
                choice = input("Enter your choice: ")
                break
            except:
                print("\n\"Please Enter Your Choice in Numeric form\"\n")

        if choice == '1':
            functionalities.add_driver()
        elif choice == '2':
            functionalities.add_rider()
        elif choice == '3':
            functionalities.request_ride()
        elif choice == '4':
            functionalities.find_nearest_driver()
        elif choice == '5':
            functionalities.match_driver()
        elif choice == '6':
            functionalities.start_ride()
        elif choice == '7':
            functionalities.complete_ride()
        elif choice == '8':
            functionalities.cancel_ride()
        elif choice == '9':
            functionalities.rate_driver()
        else:
            print("Invalid Choice")

main_menu()