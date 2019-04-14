from faker import Faker
from haikunator import  Haikunator
import random
import decimal

class Guitar:
    def __init__(self, guitar_id, manufacturer_name):
        faker = Faker()
        haikunator = Haikunator()
        self.guitar_id = guitar_id
        self.manufacturer_name = manufacturer_name
        self.guitar_name = haikunator.haikunate(token_length=0, delimiter=' ').title()
        self.guitar_model = 


class Story:
    def __init__(self, guitar_id, story_id):
        faker = Faker()
        # i think ext_word_list refers to custom words we can draw upon
        self.story_id = story_id
        self.guitar_id = guitar_id
        self.story = faker.paragraph(nb_sentences=50, variable_nb_sentences=True, ext_word_list=None)
        self.where_purchased = faker.city() + ", " + faker.country()


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
    def __init__(self, guitar_id):
        self.guitar_id = guitar_id
        self.production_year = "19" + random.randint(45, 99)
        self.weight = decimal.Decimal(random.randrange(500, 125))/100
        self.body_wood = self.body_wood_list[random.randint(0, len(self.body_wood_list)-1)]
        self.fretboard_wood = self.fretboard_wood_list[random.randint(0, len(self.fretboard_wood_list)-1)]
        self.neck_wood = self.neck_wood_list[random.randint(0, len(self.neck_wood_list)-1)]
        self.cap_wood = self.cap_wood_list[random.randint(0, len(self.cap_wood_list)-1)]
        self.neck_pickup = self.middle_pickup = self.bridge_pickup = \
            self.pickup_list[random.randint(0, len(self.pickup_list)-1)]
        self.repairs = random.choice([True, False])




class Appearances:
    # tour_name = ""
    # album_name = ""
    def __init__(self, guitar_id):
        haikunator = Haikunator()
        fake = Faker()
        self.guitar_id = guitar_id
        self.tour_name = fake.state() + " " + fake.street_name()
        self.album_name = haikunator.haikunate(token_length=0, delimiter=' ').title()



#begin main section of code
def main():

    #create distinct guitar number and distinct story number
    guitar_num = list(range(1, 4))
    guitar_num = random.sample(guitar_num, k=len(guitar_num))
    story_num = list(range(1, 4))
    story_num = random.sample(guitar_num, k=len(story_num))

    #create list of companies
    guitar_companies = []
    fake = Faker()
    for x in range(0, 50):
        guitar_companies.append(fake.company())

    for x,y  in guitar_num, story_num: #this will function as the guitar id(so it is not completely randomly generated)
        #

        #Appearances
        appear = Appearances(x)
        #Specs
        spec = Specs()
        #Story
        story = Story(x, y)










if __name__ == '__main__':
    main()