import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = {"january": 1 , "february":2, "march":3, "april":4, "may":5, "June":6, "july":7,
        "august":8, "september":9, "october":10, "november":11, "december":12, "all":13}
days = {"monday": 1 , "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7, "all":8}

print('Hello! Let\'s explore some US bikeshare data!\n')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    
    # A function to check if input data is valid
    def check_data(smaller,larger):
        x = False
        for i in range(len(larger)):
            if smaller == larger[i]:
                x = True
                break
        return x

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to filter data by Chicago, New York, or Washington?\n\n").lower()
    cities = ["chicago","new york","washington"]
    while True:
        if check_data(city,cities) == True:
            print("\nWE will filter data by " + city + " city\n")
            break
        else:
            city = input("Please enter a valid city name (Chicago, New York, or Washington)\n\n").lower()



    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Would you like to filter data by month (all, january, february, ... , december)\n\n").lower()
    months = ["january", "february", "march", "april", "may", "June", "july",
        "august", "september", "october", "november", "december", "all"]

    while True:
        if check_data(month,months) == True:
            print("\nWE will filter data by " + month + "\n\n")
            break
        else:
            month = input("Please enter a valid month name (all, january, february, ... , december)\n\n").lower()
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Would you like to filter data by day (all, monday, tuesday, ... sunday)\n\n").lower()
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]

    while True:
        if check_data(day,days) == True:
            print("\nWE will filter data by " + day + "\n\n")
            break
        else:
            day = input("Please enter a valid day name (all, monday, tuesday, ... sunday)\n\n").lower()
    print('-'*40)
    return city,month,day


    
    
    
    
    
    
    




def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df['Start Time'].dt.weekday_name
    
    if month !="all":
        df = df[df["month"] == months[month]]

    if day != "all":
        df = df[df["day_of_week"] == day.title()]


    return df

   



  




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    monthn = df["month"].mode().loc[0]
    print("The most common month is:" , list(months.items())[monthn][0])

    # TO DO: display the most common day of week
    print("The most common day of week is:" , df["day_of_week"].mode().loc[0])

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("The most common start hour is:" , df["hour"].mode().loc[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
    
    
    




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common used start station is:" , df["Start Station"].mode().loc[0])

    # TO DO: display most commonly used end station
    print("The most common used end station is:" , df["End Station"].mode().loc[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["compined"] = df["Start Station"] + " , " + df["End Station"]
    print("The most common combination of start station & end station is:" , df["compined"].mode().loc[0])
    
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: " + str(sum(df["Trip Duration"])))
    
    # TO DO: display mean travel time
    print("Mean travel time: " + str(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    
    
    
    

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    summition = 0
    df1 = df["User Type"].dropna(axis = 0).to_frame()
    for row in df1.itertuples():
        if row[1] == "Subscriber":
            summition += 1
        
    print("No. Subscribers is: " + str(summition))
    print("No. Customers is: " + str(len(df1) - summition))


        
    # TO DO: Display counts of gender
    if city != "washington" :
        summition = 0
        df2 = df["Gender"].dropna(axis = 0).to_frame()
        for row in df2.itertuples():
            if row[1] == "Male":
                summition += 1
        
        print("No. Males is: " + str(summition))
        print("No. Females is: " + str(len(df2) - summition))
    else:
        print("There is no enough data in Washington city's database to display counts of gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city != "washington" :
        df3 = df["Birth Year"].dropna(axis = 0)
        print("Earliest year of birth is: " + str(int(min(df3))))
        print("Most recent year of birth is: " + str(int(max(df3))))
        print("Most common year of birth is: " + str(int(df3.mode().loc[0])))
    else:
        print("There is no enough data in Washington city's database to display year of birth data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
    
    
    
def display_raw_data(city):
    print("\nRaw data is available to check... \n")
    y = 0
    z = 4
    ans = input("\nDo you want to see 5 rows of the raw data?   (yes,no)\n\n").lower()
    
    while True:
        if ans == "yes":
            df = pd.read_csv(CITY_DATA[city])
            print(df[y:z])
            y+=5
            z+=5
            ans = input("\nDo you want to see 5 rows of the raw data?   (yes,no)\n\n").lower()
        elif ans == "no":
            break
        else:
            ans == input("\n\nPlease enter either yes or no....\n")

        
        
        
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
