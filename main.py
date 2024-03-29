'''
Date Created: 12/21/22
Skills learned: importing pip files, basic python tools, new lines \n and \, classes, functions, lists, dictionary, boolean
Natural Language Processing
First commit file and then push. This will update code to python. From there, you can clone that file to your macbook
Hit update to refresh file on other laptop after you have committed file and pushed it out
some of the responses have been taken from chatGPT

pip install text2emotion==0.0.5
pip install emoji==0.6.0

'''

import text2emotion as te
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

#nltk.download()
import random
import en_core_web_sm
from datetime import datetime
from colorama import init, Fore, Style


class Documentation:

    def __init__(self, notes, answers):
        self.notes = notes
        self.__answers = answers
        # self.journal = journal

    def time(self):
        now = datetime.datetime.now()
        print(now.year, now.month, now.day, now.hour, now.minute)

    def document(self, notes):
        file = open("C:\\Users\\Shado\\Dropbox\\journal23test.txt", 'a')
        file.writelines(notes)
        file.close()

    def read(self):
        with open("C:\\Users\\Shado\\Dropbox\\journal23test.txt", 'r') as file:
            print(file.readline())


def journal(all_emotions_value, Question1):
    today = datetime.now()
    date1 = str(today.month) + "/" + str(today.day) + "/" + str(today.year)
    time1 = str(datetime.today().strftime("%H:%M %p"))

    notes1 = date1 + " " + time1 + " " + str(all_emotions_value) + ", " + str(Question1) + "\n"

    toLog = str(input("\033[1mDo you want to log a journal entry today? \033[0m"))
    toLog = toLog.lower()
    currentDayHolder = Documentation(notes1)
    if toLog.__contains__("yes"):
        note_to_self = input("Write your note: ")
        notes1 += "Note to self: " + note_to_self + "\n" #notes1 += "\033[34mNote to self: \033[0m" + note_to_self + "\n"
        currentDayHolder.document(notes1)
        print("Note has been saved. Have a great day!")
    else:
        print("no problem!")

def name_of_user():
    name1 = input("What is your name? Please enter below: ")
    name1 = str(name1)
    mood_base_tracker(name1)



def mood_base_tracker(name1):
    nlp = en_core_web_sm.load()
    #Question1 = str(input("Hello " + name1 + ". How are you feeling today? Feel free to jot down some notes and observations today: "))
    Question1 = "nothing" # for testing
    answers = Question1
    print("testing pass")

    all_emotions_value = te.get_emotion(Question1)

    happy_value = all_emotions_value.get("Happy")
    angry_value = all_emotions_value.get("Angry")
    surprise_value = all_emotions_value.get("Surprise")
    sad_value = all_emotions_value.get("Sad")
    fear_value = all_emotions_value.get("Fear")

    print(all_emotions_value)
    print(happy_value, angry_value, surprise_value, sad_value, fear_value)

    if happy_value == 1:
        print("great!")
        inspirational_quote()
    elif surprise_value == 1:
        surpriseAnswer = str(input(("interesting. Care to tell me more? ")))
        surpriseAnswer = surpriseAnswer.lower()
        if surpriseAnswer.__contains__("no"):
            inspirational_quote()
        elif surpriseAnswer.__contains__("yes"):
            print(
                "You should really write down your experiences in a journal! Journaling can be a helpful way to process your thoughts and emotions, reflect on your experiences, and track your personal growth")
            inspirational_quote()

    else:
        if angry_value >= 0.75:
            print("Okay, it seems you are kind of angry. Let's see if we can do anything about it.")
            anger(angry_value)
        if sad_value >= 0.75:
            grief = str(input(("Is grief on your mind? ")))
            doc = nlp(grief)
            for i in doc:
                if i.lemma_ == "grief" or i.lemma_ == "grieve" or i.lemma_ == "yes":
                    grief1(sad_value)
                    # print("Found {}".format(i.lemma_))
                else:
                    print('''I see. Nonetheless, I'm sorry to hear that you're feeling sad. It's natural to feel a range of emotions, including sadness, and it's okay to take some time to acknowledge and process these feelings. 
                    If you're struggling with sadness and it's impacting your daily life, it might be helpful to speak with a mental health professional. 
                    They can provide you with support and resources to help you manage your emotions and feel better. 
                    In the meantime, there are also some things you can try to help lift your mood:Engage in activities that you enjoy and that bring you joy, even if it's something small.
                        1. Exercise or spend time outdoors, as this can help improve your mood.
                        2. Connect with others, whether it's through phone or video calls, messaging, or in-person visits (following any necessary COVID-19 precautions).
                        3. Practice self-care, such as getting enough sleep, eating well, and taking breaks when you need them.
                        4. Seek support from friends, family, or a mental health professional if you need additional help managing your emotions.
                        5. Remember, it's okay to feel sad and to take care of yourself when you're feeling down''')

        if fear_value > 0.75:
            anxietyQ = str(input(("Do you think anxiety or a general worry be getting to you? ")))
            anxietyQ = anxietyQ.lower()
            if anxietyQ.__contains__("yes"):
                print("Alright. Let's figure this out!")
                gad7(fear_value)
            else:
                print("Okay, take a few minutes to pause and take a few deep breaths in.")

        elif happy_value == 0 and angry_value == 0 and surprise_value == 0 and sad_value == 0 and fear_value == 0:
            cont_Q = str(input(("Is there anything in particular that you would like to talk about or discuss? I'm here to help with any questions or issues you might have. Should I ask more? ")))
            cont_Q = cont_Q.lower()
            if cont_Q.__contains__('yes'):
                no_emotions_questionnaire(all_emotions_value)
            elif cont_Q.__contains__("no"):
                inspirational_quote()

        elif happy_value == 0 and angry_value != 0 and surprise_value == 0 and sad_value != 0 and fear_value != 0:
            print("hmm, today might not be a great day. Let me ask several more questions!")
            bad_mood(all_emotions_value)
        else:
            print("I didn't quite catch that. Please try again!")

    journal(all_emotions_value, Question1)


def anger(angry_value):
    anger = int(
        input("From 1-10, how angry do you feel right now? (1 - at total peace and calm, 10 - total rage monster): "))
    if anger > 6:
        print('''
        It's completely normal to feel angry sometimes. It's a natural emotion that can be triggered by a variety of situations. 
        It's important to remember that it's okay to feel angry, but it's important to find healthy ways to cope with and express those feelings. 
        It can be helpful to take some time to calm down and think about the situation that is causing you to feel angry. 
        It might also be helpful to talk to someone you trust about how you're feeling, or to find a physical activity that can help you release some of that energy in a positive way

        Given your anger level, perhaps you should take some time off! 
        ''')
    else:
        print(
            '''It seems your anger isn't at an unmanageable level. Please keep watch on your irritation and come back if it gets to unbearable level''')


def grief1(all_emotions_value):
    print('''
    I'm sorry to hear that. Grief is a natural response to loss, and it can be a difficult and painful experience. 
    It's normal to feel a range of emotions when grieving, such as sadness, anger, guilt, and loneliness. 
    It's important to allow yourself to feel these emotions and to take the time you need to heal. 
    It's also important to take care of yourself during this time, both physically and emotionally. 
    This can include getting enough rest, eating well, and finding ways to relax and find comfort. 
    It can also be helpful to reach out to others for support, whether it be through talking with a trusted friend or family member, participating in a support group, or seeking the guidance of a mental health professional. 
    Remember that everyone experiences grief differently, and there is no right or wrong way to grieve. Take things one day at a time and be kind to yourself''')


def gad7(fear_value):
    print('''Over the last two weeks, how often have you been bothered by the following problems? 
    Please put 0 for NOT AT ALL, 1 for SEVERAL DAYS, 2 for MORE THAN HALF THE DAYS, 3 for NEARLY EVERY DAY''')
    question1 = int(input("Feeling nervous, anxious or on edge: "))
    question2 = int(input("Not being able to stop or contorl worrying: "))
    question3 = int(input("Worrying too much about different things: "))
    question4 = int(input("Trouble Relaxing: "))
    question5 = int(input("Being so restless that it is hard to sit still: "))
    question6 = int(input("Becoming easily annoyeed or irritable: "))
    question7 = int(input("Feeling afraid, as if something awful might happen: "))

    # print('''If you checked any problems, how difficult have they made it for you to do your work, take care of things at home, or get along with other people?''')

    sum = question1 + question2 + question3 + question4 + question5 + question6 + question7
    if sum < 5:
        print("minimal anxiety")
    elif sum >= 5 and sum <= 9:
        print("mild anxiety")
    elif sum > 9 and sum <= 14:
        print("moderate anxiety")
    elif sum > 14:
        print("severe anxiety")


def no_emotions_questionnaire(all_emotions_value):
    print('''I'm here to listen and help. It's not uncommon for people to feel numb or as if they have no emotion at times. Can you tell me more about what you're experiencing? 
    When did you start feeling this way? Have there been any recent changes or events in your life that might be contributing to these feelings?
    I recommend journaling to understand more about these feelings''')
    journal(all_emotions_value, answers)

def bad_mood(all_emotions_value):
    print('''I'm sorry to hear that you're feeling in a bad mood. It's okay to have difficult emotions sometimes.
    It may be helpful to take a break, exercise, and take it easy''')


def inspirational_quote():
    askForQuote = str(input("\033[1mDo you want an inspirational quote? \033[0m"))
    askForQuote = askForQuote.lower()
    if askForQuote.__contains__("yes"):
        Dict = {1: 'Trust yourself that you can do it and get it.” ―Baz Luhrmann',
                2: 'If people are doubting how far you can go, go so far that you can’t hear them anymore. —Michele Ruiz',
                3: '“Impossible is just an opinion.” —Paulo Coelho',
                4: 'View life as a story, not as a scoreboard',
                5: 'Writing is Healing',
                6: 'Be kind, for everyone you meet is fighting a great battle',
                7: 'External success will not bring inner peace',
                8: 'One day, in retrospect, the years of struggle will strike you as the most beautiful. - Sigmund Freud',
                9: 'In the end, life is about character - Alvin Cheng',
                10: 'Be confident, not certain - Eleanor Roosevelt',
                11: 'if life were predictable it would cease to be life and be without flavor - Eleanor Roosevelt',
                12: 'I am enough',
                13: 'In the end, life is about character. Bring character to your job and just let all the cards drop in line',
                14: "Believe you can, and you're halfway there - Theodore Roosevelt",
                15: "Existence precedes essence. - Jean-Paul Sartre",
                16: "If nothing we do matters, then all that matters is what we do. - Joss Whedon"
                }
        print(Dict[random.randrange(1, 16, 1)])

    elif askForQuote.__contains__("no") or askForQuote.__contains__("na"):
        # print("Alright. Have a good day!")
        return ()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # name_of_user()
    mood_base_tracker("Alvin")


