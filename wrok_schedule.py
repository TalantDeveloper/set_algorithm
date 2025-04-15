# Schedule Library imported
import schedule
import time


# Functions setup
def sudo_placement():
    print("Get ready for Sudo Placement at Medium")


def good_luck():
    print("Good Luck for Test")


def work():
    print("Study and work hard")


def bedtime():
    print("It is bed time go rest")


def medium():
    print("Istuti says Medium")


# Task scheduling
# After every 1mins medium() is called.
schedule.every(1).minutes.do(medium)

# After every hour medium() is called.
schedule.every().hour.do(medium)

# Every day at 12am or 08:45 time bedtime() is called.
schedule.every().day.at("08:45").do(bedtime)

# After every 5 to 45mins in between run work()
schedule.every(5).to(45).minutes.do(work)

# Every monday good_luck() is called
schedule.every().monday.do(good_luck)

# Every tuesday at 18:00 sudo_placement() is called
schedule.every().tuesday.at("18:00").do(sudo_placement)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)
