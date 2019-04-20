from faker import Faker
from haikunator import  Haikunator
import random
import decimal
import csv

class Guitar:
    guitar_comp_list =["Gibson", "Gretsch", "Fender", "G&L", "Ibanez", "Music Man",
                       "Friedman", "First Act", "PRS", "Paul Reed Smith", "Squier",
                       "Epiphone", "ESP", "LTD", "Martin", "Taylor", "Washburn",
                       "Guild", "Scala", "Rickenbacker", "Schecter",
                       "Jackson", "B.C. Rich", "Carvin", "Charvel"]

    def __init__(self, guitar_id):
        faker = Faker()
        haikunator = Haikunator()
        self.guitar_id = guitar_id
        self.manufacturer_name = self.guitar_comp_list[random.randint(0, len(self.guitar_comp_list)-1)]
        self.guitar_name = haikunator.haikunate(token_length=0, delimiter=' ').title()
        self.guitar_model = faker.last_name_female()
        self.serial_number = faker.ean(length=13)


class Story:
    def __init__(self, guitar_id, story_id):
        faker = Faker()
        # i think ext_word_list refers to custom words we can draw upon
        self.story_id = story_id
        self.guitar_id = guitar_id
        self.story_text = faker.paragraph(nb_sentences=50, variable_nb_sentences=True, ext_word_list=None)
        self.where_purchased = faker.city() + ", " + faker.country()
        self.custom_built = random.choice([True, False])


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
        faker = Faker()
        self.guitar_id = guitar_id
        self.guitar_spec_id = str(random.randint(1, 126))
        self.production_year = "19" + str(random.randint(45, 99))
        self.weight = decimal.Decimal(random.randrange(500, 1250))/100
        self.finish = faker.color_name()
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

class Photos:
    def __init__(self, guitar_id):
        faker = Faker()
        self.guitar_id = guitar_id
        self.photo_number = random.randint(1, 126)
        self.photo_path = faker.image_url(width=None, height=None)

class Videos:
    def __init__(self, guitar_id):
        faker = Faker()
        self.guitar_id = guitar_id
        self.video_number = random.randint(1, 126)
        self.video_path = faker.image_url(width=None, height=None)


#begin main section of code
def main():
    hi_range = int(input("Type the number of companies\n"))

    #create distinct guitar number and distinct story number
    guitar_num = list(range(1, hi_range))
    guitar_num = random.sample(guitar_num, k=len(guitar_num))
    story_num = list(range(1, hi_range))
    story_num = random.sample(guitar_num, k=len(story_num))

    #csv file openings
    #guitar

    #appearnaces

    #specs

    #story

    #photos

    #videos


    for x,y  in zip(guitar_num, story_num): #this will function as the guitar id(so it is not completely randomly generated)
        #Guitar
        with open('fake data/guitar.csv', 'a') as csvFile:
            guitar_writer = csv.writer(csvFile)
            guitar = Guitar(x)
            row = [guitar.guitar_id, guitar.manufacturer_name, guitar.guitar_name, guitar.guitar_model, guitar.serial_number]
            guitar_writer.writerow(row)
        csvFile.close()

        #Appearances
        with open('fake data/appearances.csv', 'a') as csvFile:
            appear_writer = csv.writer(csvFile)
            appear = Appearances(x)
            row = [appear.guitar_id, appear.tour_name, appear.album_name]
            appear_writer.writerow(row)
        csvFile.close()

        #Specs
        with open('fake data/specs.csv', 'a') as csvFile:
            specs_writer = csv.writer(csvFile)
            spec = Specs(x)
            row = [spec.guitar_id, spec.guitar_spec_id, spec.production_year, spec.weight, spec.finish, spec.body_wood, spec.neck_wood,
                   spec.fretboard_wood, spec.cap_wood, spec.neck_pickup, spec.middle_pickup, spec.bridge_pickup, spec.repairs]
            specs_writer.writerow(row)
        csvFile.close()

        #Story
        with open('fake data/story.csv', 'a') as csvFile:
            story_writer = csv.writer(csvFile)
            story = Story(x, y)
            row = [story.story_id, story.guitar_id, story.story_text, story.where_purchased, story.custom_built]
            story_writer.writerow(row)
        csvFile.close()

        #Photos
        with open('fake data/photos.csv', 'a') as csvFile:
            photos_writer = csv.writer(csvFile)
            photo = Photos(x)
            row = [photo.guitar_id, photo.photo_number, photo.photo_path]
            photos_writer.writerow(row)
        csvFile.close()


        #video
        with open('fake data/videos.csv', 'a') as csvFile:
            video_writer = csv.writer(csvFile)
            video = Videos(x)
            row = [video.guitar_id, video.video_number, video.video_path]
            video_writer.writerow(row)
        csvFile.close()


if __name__ == '__main__':
    main()