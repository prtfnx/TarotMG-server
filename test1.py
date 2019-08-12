from DeckClass import Deck
from CardShuffle import card_shuffle
from CardClass import Card
from SQLiteClass import SQLite
from ImageProcessing import square_set
from CoreTarot import Tarot
def deck_create_test():
    new_deck = Deck('thoth', 33333)
    new_deck.create()
    second_card = new_deck.card_list[1]
    return new_deck


def shuffle_test():
    list_test = []
    result = []
    for i in range(78):
        list_test.append(Card(str(i),i,i))
    for card in list_test:
        result.append(card.name)
    print(','.join(result))
    result=[]
    card_shuffle(list_test)
    for card in list_test:
        result.append(card.name)
    print(','.join(result))


def get_card_test():
    test_deck = deck_create_test()
    test_deck.shuffle()
    card = test_deck.get_card(4)
    print(card.name)


def sql_test(): 
    deck = deck_create_test()
    sqlite = SQLite()
    sqlite.save_deck(deck)
    new_deck = sqlite.select_deck('thoth',33333)
    new_deck.shuffle()
    sqlite.save_deck(new_deck)
    new_new_deck=sqlite.select_deck('thoth',33333)
    card = new_deck.get_card(4)
    print(card.name)
    print(card.path_to_image)


def image_test():
    test_list=['images/thoth/arcanes/02_Toth_Priestess.jpg',
           'images/thoth/arcanes/03_Toth_Empress.jpg',
           'images/thoth/arcanes/04_Toth_Emperor.jpg',
           'images/thoth/arcanes/05_Toth_Hierophant.jpg']
    list_of_images=[]
    for path in list_of_path:
        list_of_images.append(Image.open(path))
    img = list_of_images[0]  # to take size and mode
    (l, h), img_mode = img.size, img.mode  #  length and height of img  
    print(l,h)
    print((2*l, 2*h))
    image_set = Image.new(img_mode, (2*l, 2*h),)  # create imageset
    # part set in 4 parts
    list_of_boxes=[ (0, 0, l,     h),
                    (l, 0, 2*l,   h),
                    (0, h, l,   2*h),
                    (l, h, 2*l, 2*h)]
    print(list_of_images)
    for image, box in zip(list_of_images, list_of_boxes):
        # paste all images to imageset
        image_set.paste(image, box)
    image_set.save('test.jpg')
    return image_set
def sss(core):
    return core.get_cards([4])

def test_get_cards():
    core = Tarot('232',22222)
    core.create_new_deck('thoth')
    for _ in range(3):
        #card=core.get_cards([4])
        card=sss(core)
        for car in card:
            print(car.name)
        core.put_from_hand_to_deck()
test_get_cards()