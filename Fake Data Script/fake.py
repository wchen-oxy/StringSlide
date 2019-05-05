from faker import Faker
from haikunator import Haikunator
import random
import decimal
import csv


class Guitar:
    fender_guitar_list = ["Stratocaster", "Telecaster", "Jaguar",
                          "Jazzmaster", "Mustsang", "Meteora", "Duo-Sonic"]
    gibson_guitar_list = ["Les Paul Standard", "Les Paul Custom", "Les Paul Jr", "Les Paul Studio",
                          "Les Paul Classic", "Les Paul Jr Double Cut",
                          "Les Paul Standard Double Cut", "ES-355", "ES-355", "ES-330", "Flying V",
                          "Firebird", "ES-175", "Explorer", "SG", "SG Jr"]
    gretsch_guitar_list = ["White Falcon", "G5420T", "G5425", "Chet Atkins", "Reverend Horton Heat",
                           "Irish Falcon", "Black Falcon", "White Penguin", "Black Penguin", "Penguin"]
    gl_guitar_list = ["Fullerton Deluxe ASAT", "Fullerton Deluxe Comanche",
                      "Fullerton Deluxe Doheny", "Fullerton Deluxe Skyhawk", "ASAT Classic Bluesboy",
                      "Tribute ASAT", "Tribute Doheny", "Tribute Comanche", "Tribute Fallout"]
    ibanez_guitar_list = ["JS1CR Joe Satriani", "KIKO200", "GB10 George Benson",
                          "PS10", "PM200", "JEM7V", "JS2480MCR", "PGM333", "AF200"]
    friedman_guitar_list = ["Vintage-T", "Metro-D", "Vintage-S", "Cali"]
    prs_guitar_list = ["Paul's Guitar", "CE 24 Semi-Hollow",
                       "SE Custom 24 Ziricote", "Silver Sky", "SE Standard 24",
                       "SE 245 Standard", "SE Mark Tremonti", "SE Custom 24",
                       "SE Custom 22 Semi-Hollow", "SE 277 Baritone", "SE Custom 22",
                       "SE Carlos Santana", "McCarty 594", "McCarty Singlecut",
                       "Super Eagle II", "Carlos Santana Signature"]
    squier_guitar_list = ["Stratocaster", "Telecaster", "Jaguar",
                          "Jazzmaster", "Mustsang", "Meteora", "Duo-Sonic"]
    epiphone_guitar_list = ["Les Paul Standard", "Les Paul Custom", "Les Paul Jr", "Les Paul Studio",
                            "Les Paul Traditional II", "Les Paul Jr Double Cut",
                            "Les Paul Standard Double Cut", "ES-355", "ES-355", "ES-330", "Flying V",
                            "Firebird", "ES-175", "Explorer", "SG", "SG Jr", "Casino", "Coronet"]
    esp_guitar_list = ["Arrow", "Black Metal", "EC", "EX", "F", "FRX", "H",
                       "H3", "M", "MH", "SN", "TE", "Viper", "Xtone"]
    martin_guitar_list = ["HD-28", "D-41", "GPC-28E", "00-28", "D-35", "D-45",
                          "D-28", "D-18", "CEO-7", "Ed Sheeran Signature", "HD-35", "Style 3 Centennial",
                          "D-28 Authentic 1937", "HD-28V"]
    taylor_guitar_list = ["100 Series", "200 Series", "300 Series",
                          "400 Series", "500 Series", "600 Series",
                          "700 Series", "800 Series"]
    washburn_guitar_list = ["HB15", "HB35", "J3", "J600", "L20", "M10FRQ", "M160"]
    guild_guitar_list = ["Starfire", "D25M", "A-150", "D40", "Doubleneck Custom"]
    scala_guitar_list = ["Underdog", "Junkyard", "Burst", "ES", "T-Style"]
    rickenbacker_guitar_list = ["Model 1993 Plus", "Model 300",
                                "Model 330-12", "Model 340", "Model 360"]
    schecter_guitar_list = ["Solo-II", "E-1 Custom", "Keith Merror KM-7", "C-6 Pro",
                            "C-7 SLS Evil Twin", "V-1", "Synyster Gates Custom"]
    jackson_guitar_list = ["Dinky", "Soloist", "Rhoads", "King V", "Juggernaut", "Kelly"]
    bc_rich_guitar_list = ["Beast", "Bich", "Eagle", "Widow", "Warlock", "Igniter",
                           "Virgin", "Seagull", "Stealth", "Virgo", "Mockingbird", "Wave"]
    carvin_guitar_list = ["A6C", "A6E", "A6H", "A7E", "C7H", "C6H", "CT624X"]
    charvel_guitar_list = ["DK27", "DK24", "SC1", "Guthrie Govan Signature", "DK", "So-Cal Style"]
    guitar_comp_list = ["Gibson", "Gretsch", "Fender", "G&L", "Ibanez",
                        "Friedman", "Paul Reed Smith", "Squier",
                        "Epiphone", "ESP", "Martin", "Taylor", "Washburn",
                        "Guild", "Scala", "Rickenbacker", "Schecter",
                        "Jackson", "B.C. Rich", "Carvin", "Charvel"]

    def __init__(self, guitar_id):
        faker = Faker()
        haikunator = Haikunator()
        self.guitar_id = guitar_id
        self.manufacturer_name = self.guitar_comp_list[random.randint(0, len(self.guitar_comp_list) - 1)]
        self.guitar_name = haikunator.haikunate(token_length=0, delimiter=' ').title()

        if self.manufacturer_name == "Gibson":
            self.guitar_model = self.gibson_guitar_list[random.randint(0, len(self.gibson_guitar_list) - 1)]
        elif self.manufacturer_name == "Gretsch":
            self.guitar_model = self.gretsch_guitar_list[random.randint(0, len(self.gretsch_guitar_list) - 1)]
        elif self.manufacturer_name == "Fender":
            self.guitar_model = self.fender_guitar_list[random.randint(0, len(self.fender_guitar_list) - 1)]
        elif self.manufacturer_name == "G&L":
            self.guitar_model = self.gl_guitar_list[random.randint(0, len(self.gl_guitar_list) - 1)]
        elif self.manufacturer_name == "Ibanez":
            self.guitar_model = self.ibanez_guitar_list[random.randint(0, len(self.ibanez_guitar_list) - 1)]
        elif self.manufacturer_name == "Friedman":
            self.guitar_model = self.friedman_guitar_list[random.randint(0, len(self.friedman_guitar_list) - 1)]
        elif self.manufacturer_name == "Paul Reed Smith":
            self.guitar_model = self.prs_guitar_list[random.randint(0, len(self.prs_guitar_list) - 1)]
        elif self.manufacturer_name == "Squier":
            self.guitar_model = self.squier_guitar_list[random.randint(0, len(self.squier_guitar_list) - 1)]
        elif self.manufacturer_name == "Epiphone":
            self.guitar_model = self.epiphone_guitar_list[random.randint(0, len(self.epiphone_guitar_list) - 1)]
        elif self.manufacturer_name == "ESP":
            self.guitar_model = self.esp_guitar_list[random.randint(0, len(self.esp_guitar_list) - 1)]
        elif self.manufacturer_name == "Taylor":
            self.guitar_model = self.taylor_guitar_list[random.randint(0, len(self.taylor_guitar_list) - 1)]
        elif self.manufacturer_name == "Washburn":
            self.guitar_model = self.washburn_guitar_list[random.randint(0, len(self.washburn_guitar_list) - 1)]
        elif self.manufacturer_name == "Martin":
            self.guitar_model = self.martin_guitar_list[random.randint(0, len(self.martin_guitar_list) - 1)]
        elif self.manufacturer_name == "Rickenbacker":
            self.guitar_model = self.rickenbacker_guitar_list[random.randint(0, len(self.rickenbacker_guitar_list) - 1)]
        elif self.manufacturer_name == "Schecter":
            self.guitar_model = self.schecter_guitar_list[random.randint(0, len(self.schecter_guitar_list) - 1)]
        elif self.manufacturer_name == "Jackson":
            self.guitar_model = self.jackson_guitar_list[random.randint(0, len(self.jackson_guitar_list) - 1)]
        elif self.manufacturer_name == "B.C. Rich":
            self.guitar_model = self.bc_rich_guitar_list[random.randint(0, len(self.bc_rich_guitar_list) - 1)]
        elif self.manufacturer_name == "Carvin":
            self.guitar_model = self.carvin_guitar_list[random.randint(0, len(self.carvin_guitar_list) - 1)]
        elif self.manufacturer_name == "Charvel":
            self.guitar_model = self.charvel_guitar_list[random.randint(0, len(self.charvel_guitar_list) - 1)]
        elif self.manufacturer_name == "Scala":
            self.guitar_model = self.scala_guitar_list[random.randint(0, len(self.scala_guitar_list) - 1)]
        elif self.manufacturer_name == "Guild":
            self.guitar_model = self.guild_guitar_list[random.randint(0, len(self.guild_guitar_list) - 1)]
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
                   "Fender Vintage", "EMG 85 Active", "DiMarzio DP419 Area 67", "Lace Sensor Blue-Silver-Red",
                   "Fender Vintage Noiseless", "Seymour Duncan Antiquity P-90", "LR Baggs Anthem tru-Mic",
                   "Fishman Rare Earth", "EMG-81 Humbucking Active", "Railhammer Hyper Vintage Humbucker",
                   "Seymour Duncan SH-13 Dimebucker", "Lollar Imperial Humbucker", "Lollar Precision Bass"]

    def __init__(self, guitar_id):
        faker = Faker()
        self.guitar_id = guitar_id
        self.guitar_spec_id = str(random.randint(1, 126))
        self.production_year = "19" + str(random.randint(45, 99))
        self.weight = decimal.Decimal(random.randrange(500, 1250)) / 100
        self.finish = faker.color_name()
        self.body_wood = self.body_wood_list[random.randint(0, len(self.body_wood_list) - 1)]
        self.fretboard_wood = self.fretboard_wood_list[random.randint(0, len(self.fretboard_wood_list) - 1)]
        self.neck_wood = self.neck_wood_list[random.randint(0, len(self.neck_wood_list) - 1)]
        self.cap_wood = self.cap_wood_list[random.randint(0, len(self.cap_wood_list) - 1)]
        self.neck_pickup = self.middle_pickup = self.bridge_pickup = \
            self.pickup_list[random.randint(0, len(self.pickup_list) - 1)]
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


# begin main section of code
def main():
    hi_range = int(input("Type the number of companies\n"))

    # create distinct guitar number and distinct story number


    guitar_num = list(range(1, hi_range))
    guitar_num = random.sample(guitar_num, k=len(guitar_num))
    story_num = list(range(1, hi_range))
    story_num = random.sample(guitar_num, k=len(story_num))

    # csv file openings
    # guitar

    # appearnaces

    # specs

    # story

    # photos

    # videos


    for x, y in zip(guitar_num,
                    story_num):  # this will function as the guitar id(so it is not completely randomly generated)
        # Guitar
        with open('fake data/guitar2.csv', 'a') as csvFile:
            guitar_writer = csv.writer(csvFile)
            guitar = Guitar(x)
            row = [guitar.guitar_id, guitar.manufacturer_name, guitar.guitar_name, guitar.guitar_model,
                   guitar.serial_number]
            guitar_writer.writerow(row)
            csvFile.close()

        # Appearances
        with open('fake data/appearances2.csv', 'a') as csvFile:
            appear_writer = csv.writer(csvFile)
            appear = Appearances(x)
            row = [appear.guitar_id, appear.tour_name, appear.album_name]
            appear_writer.writerow(row)
            csvFile.close()

        # Specs
        with open('fake data/specs2.csv', 'a') as csvFile:
            specs_writer = csv.writer(csvFile)
            spec = Specs(x)
            row = [spec.guitar_id, spec.guitar_spec_id, spec.production_year, spec.weight, spec.finish, spec.body_wood,
                   spec.neck_wood,
                   spec.fretboard_wood, spec.cap_wood, spec.neck_pickup, spec.middle_pickup, spec.bridge_pickup,
                   spec.repairs]
            specs_writer.writerow(row)
            csvFile.close()

        # Story
        with open('fake data/story2.csv', 'a') as csvFile:
            story_writer = csv.writer(csvFile)
            story = Story(x, y)
            row = [story.story_id, story.guitar_id, story.story_text, story.where_purchased, story.custom_built]
            story_writer.writerow(row)
            csvFile.close()

        # Photos
        with open('fake data/photos2.csv', 'a') as csvFile:
            photos_writer = csv.writer(csvFile)
            photo = Photos(x)
            row = [photo.guitar_id, photo.photo_number, photo.photo_path]
            photos_writer.writerow(row)
            csvFile.close()

        # video
        with open('fake data/videos2.csv', 'a') as csvFile:
            video_writer = csv.writer(csvFile)
            video = Videos(x)
            row = [video.guitar_id, video.video_number, video.video_path]
            video_writer.writerow(row)
            csvFile.close()

if __name__ == '__main__':
    main()
