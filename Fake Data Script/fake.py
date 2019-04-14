from faker import Faker
from haikunator import  Haikunator
import random

fake = Faker()
print(fake.last_name())
haikunator = Haikunator()
print(haikunator.haikunate(token_length=0, delimiter=' '))
print(fake.street_name())


class Specs:
    body_wood = ["Maple", "Mahogany", "Basswood", "Alder", "Swamp Ash", "Korina", "Japanese Ash", "Walnut"]
    fretboard_wood = ["Rosewood", "Maple", "Ebony"]
    neck_wood = ["Wenge", "Maple", "Koa", "Rosewood", "Mahogany"]
    cap_wood = ["maple", "walnut"]
    pickups = ["Burstbucker", "'57 Classic", "Dirty Fingers", "490R & 490T", "496 & 500T",
               "Fender Vintage", "EMG 85 Active", "DiMarzio DP419 Area 67",  "Lace Sensor Blue-Silver-Red",
               "Fender Vintage Noiseless", "Seymour Duncan Antiquity P-90", "LR Baggs Anthem tru-Mic",
               "Fishman Rare Earth", "EMG-81 Humbucking Active", "Railhammer Hyper Vintage Humbucker",
               "Seymour Duncan SH-13 Dimebucker", "Lollar Imperial Humbucker", "Lollar Precision Bass"]
    # def __init__(self):



class Appearances:
    # tour_name = ""
    # album_name = ""
    def __init__(self, guitar_id):
        fake = Faker()
        self.guitar_id = guitar_id
        self.tour_name = fake.state() + " " + fake.street_name()
        self.album_name = haikunator.haikunate(token_length=0, delimiter=' ').title()



#begin main section of code
def main():
    a = Appearances(1)

    for x in range(100, 200): #this will function as the guitar id
        random.randint(1, 100)


if __name__ == '__main__':
    main()