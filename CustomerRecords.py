import os
import math
import json
from operator import itemgetter


class CustomerRecords:
    """
    This program reads a customer records file. 
    It returns customers within 100km sorted in ascending order by User_ID.
    To calculate distance the program uses the spherical law of cosines.
    """

    def __init__(self, input_file, accepted_distance, hq_latitude, hq_longitude):

        self.input_file = input_file
        self.accepted_distance = accepted_distance
        self.hq_latitude = hq_latitude
        self.hq_longitude = hq_longitude

    def get_distance(self, lat1, lon1, lat2, lon2):
        """
        Calculate distance between two GPS coordinates.
        Return distance in meters.
        Georgios Migdos's Blog helped me with the calculation:
        https://tinyurl.com/yboof4nz
        """

        delta = lon2 - lon1
        lat1_radians = math.radians(lat1)
        lat2_radians = math.radians(lat2)
        C = math.radians(delta)
        x = math.sin(lat1_radians) * math.sin(lat2_radians) + \
            math.cos(lat1_radians) * math.cos(lat2_radians) * math.cos(C)
        distance = math.acos(x)
        distance = math.degrees(distance)
        distance = distance * 60
        distance = distance * 1852
        distance = round(distance)
        return distance

    def read_file(self):
        """
        Read file in.
        Return records with valid distances.
        """

        data = []
        try:
            with open(self.input_file) as f:
                for line in f:
                    data_line = json.loads(line)
                    distance = self.get_distance(self.hq_latitude, self.hq_longitude, float(
                        data_line['latitude']), float(data_line['longitude']))
                    if distance < self.accepted_distance:
                        data.append(data_line)
        except FileNotFoundError:
            raise FileNotFoundError(self.input_file, "cannot be found")
        return data

    def get_closest_customers(self):
        """
        Sort and output valid distances.
        """

        newlist = sorted(self.read_file(), key=itemgetter('user_id'))
        results = []
        for i in newlist:
            results.append(i['name'])
            print(i['name'])
        return results


if __name__ == "__main__":
    cr = CustomerRecords('gistfile1.txt', 100000, 53.339428, -6.257664)
    cr.get_closest_customers()
