from faker import Faker
from haikunator import  Haikunator
import random


class Specs:
    body_wood_list = ["Maple", "Mahogany", "Basswood", "Alder", "Swamp Ash", "Korina", "Japanese Ash", "Walnut"]
    fretboard_wood_list = ["Rosewood", "Maple", "Ebony"]
    neck_wood_list = ["Wenge", "Maple", "Koa", "Rosewood", "Mahogany"]
    cap_wood_list = ["maple", "walnut"]
    pickup_list = ["Burstbucker", "'57 Classic", "Dirty Fingers", "490R & 490T", "496 & 500T",
               "Fender Vintage", "EMG 85 Active", "DiMarzio DP419 Area 67",  "Lace Sensor Blue-Silver-Red",
               "Fender Vintage Noiseless", "Seymour Duncan Antiquity P-90", "LR Baggs Anthem tru-Mic",
               "Fishman Rare Earth", "EMG-81 Humbucking Active", "Railhammer Hyper Vintage Humbucker",
               "Seymour Duncan SH-13 Dimebucker", "Lollar Imperial Humbucker", "Lollar Precision Bass"]
    def __init__(self):
        self.body_wood = self.body_wood_list[random.randint(0, len(self.body_wood_list)-1)]
        self.fretboard_wood = self.fretboard_wood_list[random.randint(0, len(self.fretboard_wood_list)-1)]
        self.neck_wood = self.neck_wood_list[random.randint(0, len(self.neck_wood_list)-1)]
        self.cap_wood = self.cap_wood_list[random.randint(0, len(self.cap_wood_list)-1)]
        self.pickup = self.pickup_list[random.randint(0, len(self.pickup_list)-1)]



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
    #Testing out Faker
    # fake = Faker()
    # print(fake.last_name())
    # haikunator = Haikunator()
    # print(haikunator.haikunate(token_length=0, delimiter=' '))
    # print(fake.street_name())



    for x in range(100, 200): #this will function as the guitar id(so it is not completely randomly generated)
        #Appearances
        appear = Appearances(x)
        #Specs
        spec = Specs()
        





if __name__ == '__main__':
    main()