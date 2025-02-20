import random
import json
import boto3

class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate
    
    def __str__(self):
        return self.license_plate

class ParkingLot:
    def __init__(self, square_footage, spot_size):
        self.spot_size = spot_size
        self.spots = [[] for _ in range(square_footage // spot_size)]
    
    def park(self, car, spot):
        if self.spots[spot]:
            return f"Car with license plate {car} could not be parked in spot {spot}. Spot is occupied."
        else:
            self.spots[spot] = car
            return f"Car with license plate {car} parked successfully in spot {spot}."
    
    def map_to_json(self):
        mapping = {i: str(car) if car else None for i, car in enumerate(self.spots)}
        return json.dumps(mapping, indent=4)

def main():
    parking_lot_size = 2000  # parking lot size
    spot_size = 96  # each parking spot size in parkin lot
    max_cars_count = 22
    occupied_spots = 0
    
    parking_lot = ParkingLot(parking_lot_size, spot_size)
    
    cars = [Car(str(random.randint(1000000, 9999999))) for _ in range(max_cars_count)]
    
    for car in cars:
        
        # exit in case of maximum occupancy
        if occupied_spots == (parking_lot_size // spot_size):
            break
        
        while True:
            spot = random.randint(0, len(parking_lot.spots) - 1)
            result = parking_lot.park(car, spot)
            print(result)
            if "successfully" in result:
                occupied_spots += 1
                break
    
    # Optional: Save parking lot mapping to JSON and upload to S3 bucket
    mapping_json = parking_lot.map_to_json()
    
    with open('parking_mapping.json', 'w') as json_file:
        json_file.write(mapping_json)
    
    # Upload mapping file to S3 code
    # s3 = boto3.client('s3', aws_access_key_id='ACCESS_KEY',
    #                   aws_secret_access_key='SECRET_KEY',
    #                   region_name='REGION')
    # bucket_name = 'bucket_name'
    # s3.upload_file('parking_mapping.json', bucket_name, 'parking_mapping.json')
    # print("Mapping JSON file uploaded to S3 bucket.")
    
if __name__ == "__main__":
    main()