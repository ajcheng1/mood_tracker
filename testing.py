

from datetime import datetime
def datetester(name):

    today = datetime.now()
    date1 = str(today.month) + "/" + str(today.day) + "/" + str(today.year)
    time1 = str(datetime.today().strftime("%H:%M %p"))

    daySinceStart = 0

    modelStartDate = "01/01/2019"
    modelEndDate = "31/12/2019"
    interval = 15
    dateTime = pd.date_range(start=modelStartDate, end=modelEndDate, freq=str(interval) + 'min')

    counter = 0
    for i in dateTime:
        # Do your calculations
        counter+=1  # Counter value incrementing

        if i == i.round(freq='D'):  # Check if its the start of the day
            counter = 0  # Reset the counter
            print("New Date at {}".format(i))

if __name__ == '__testing__':
    # name_of_user()
    datetester("Alvin")
