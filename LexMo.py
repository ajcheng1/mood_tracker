# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
Skills learned: importing pip files, basic python tools, new lines \n


'''
import text2emotion as te
import nltk
nltk.download('punkt')
from LeXmo import LeXmo


def name_of_user():
    name1 = input("What is your name? Please enter below: ")
    name1 = str(name1)
    mood_base_tracker(name1)

def mood_base_tracker(name1):
    Question1 = str(input("Hello " + name1 + ". How are you feeling today? "))
    emotion = LeXmo.LeXmo(Question1)
    print (emotion)
    #Question1 = "okay" # for testing

    all_emotions_value = te.get_emotion(Question1)
    print(all_emotions_value)

    happy_value = all_emotions_value.get("Happy")
    angry_value = all_emotions_value.get("Angry")
    surprise_value = all_emotions_value.get("Surprise")
    sad_value = all_emotions_value.get("Sad")
    fear_value = all_emotions_value.get("Fear")

    print(happy_value, angry_value, surprise_value, sad_value, fear_value)

    if happy_value == 1:
        print("great!")
    if angry_value > 0.3:
        print("Okay, it seems you are kind of angry. Let's see if we can do anything about it.")
        anger = int(input("From 1-10, how angry do you feel right now? (1 - at total peace and calm, 10 - total rage monster"))
        #if anger =
    elif happy_value == 0 and angry_value == 0 and surprise_value == 0 and sad_value == 0 and fear_value == 0:
        cont_Q = str(input(("Just a regular old day for you, I'm assuming. Should I ask more? ")))
        cont_Q = cont_Q.lower()
        if cont_Q.__contains__('yes'):
            no_emotions_questionnaire(all_emotions_value)
        elif cont_Q.__contains__("no"):
            print("Sounds Good. I hope you have a great day!")
            return()
    if happy_value == 0 and angry_value != 0 and surprise_value == 0 and sad_value != 0 and fear_value !=0:
        print("hmm, today might not be a great day. Let me ask several more questions!")
        bad_mood(all_emotions_value)
    else:
        print("I didn't quite catch that. Please try again!")
def no_emotions_questionnaire(all_emotions_value):
    print("TO BE CONTINUED")


def bad_mood(all_emotions_value):
    print("")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #name_of_user()
    mood_base_tracker("Alvin")

