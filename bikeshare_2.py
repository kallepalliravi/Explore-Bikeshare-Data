import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

## lists for filter options for get_filters function
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

###################################################################################################
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# get user input for city (chicago, new york city, washington)
    while True:
        try:
            city = cities.index(input("Which City you would like to analyze: chicago, new york city, washington:\n").casefold())
            break
        except ValueError:
            print("\nInvalid input: Please enter correct city name from options available:\n")
    city = cities[city]
# get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = months.index(input("Which Month? january, february, march, april, may, june or all:\n").casefold())
            break
        except ValueError:
            print("\nInvalid input: Please enter correct month from options available:\n")
    month = months[month]
# get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = days.index(input("Which Day? monday, tuesday, Wednesday, thursday, friday,saturday, sunday or all:\n").casefold())
            break
        except ValueError:
            print("\nInvalid input: Please enter correct day from options available:\n")
    day = days[day]

    print('-'*75)
    print('Your city selection was:', city)
    print('Your month selection was:',month)
    print('Your day selection was:',day)



    return city, month, day

###################################################################################################
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
# load data into a data frame
    df= pd.read_csv(CITY_DATA[city])

 # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
         # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
###################################################################################################

def raw_data(df):
    print("Shape of Dataframe for the selections:", df.shape)
    print('-'*75)
    input("Press Enter to continue..............")
    n=0
    while n<=df.shape[0]:
        raw_data = input('\nWould you like to see rows {} to {} of raw data:Enter yes or no.\n'.format(n,n+5))
        if raw_data.lower() == "yes":
            print(df.iloc[n:n+5,])
            n=n+5
        else:
            break
    print('-'*75)
####################################################################################################
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    input("Press Enter to continue..............")
    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    count_common_month = df[df['month']== most_common_month].count()[0]
    print('\nMost Common month:', most_common_month,"...", "count:", count_common_month)

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    count_common_day = df[df['day_of_week'] == most_common_day ].count()[0]
    print('Most Common day:', most_common_day, "..." ,"count:", count_common_day)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    count_common_start_hour = df[df['hour'] == most_common_start_hour].count()[0]
    print('Most Common start hour:', most_common_start_hour, "...", "count:", count_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*75)

###################################################################################################

def station_stats(df):
    """Displays statistics by month day hour."""
    """Displays statistics on the most popular stations and trip."""
    input("Press Enter to continue..............")

    print("\n Calculating count by month, day and hour")
    # display count by month
    month_count = df.groupby(['month'])['month'].count()
    print("\ncount by Month\n", month_count)

    # display count by day
    day_count = df.groupby(['day_of_week'])['day_of_week'].count()
    print("\ncount by Day\n", day_count)

    # display count by hour
    hour_count = df.groupby(['hour'])['hour'].count()
    print("\ncount by hour\n", hour_count)

    print('-'*75)
    input("Press Enter to continue..............")

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    count_common_start_station = df[df['Start Station'] == most_common_start_station].count()[0]
    print('Most Common Start Station:', most_common_start_station, "...", "count:", count_common_start_station )

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    count_common_end_station = df[df['End Station'] == most_common_end_station].count()[0]
    print('Most Common Start Station:', most_common_start_station, "...", "count:", count_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station']+'---->'+df['End Station']
    most_common_trip = df['Trip'].mode()[0]
    count_common_trip = df[df['Trip'] == most_common_trip].count()[0]
    print('Most Common Trip:', most_common_trip, "...", "count:", count_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*75)

###################################################################################################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    input("Press Enter to continue..............")
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*75)
###################################################################################################

def user_stats(df):
    """Displays statistics on bikeshare users."""
    input("Press Enter to continue..............")
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df.groupby(['User Type'])['User Type'].count()
    print('\nCount by:\n', user_counts)
    # Display counts of gender

    if 'Gender' in df.columns:
        gender_counts = df.groupby(['Gender'])['Gender'].count()
        print('\n \nCount by:\n', gender_counts)
    else:
        print("\nUser Gender stats: The gender column doesnt exist in the file selected")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:

        earliest_birth_year = df['Birth Year'].min()
        count_earliest_birth_year = df[df['Birth Year'] == earliest_birth_year].count()[0]
        print('\nEarliest year of Birth:', int(earliest_birth_year), "...", "count:", count_earliest_birth_year)

        recent_birth_year = df['Birth Year'].max()
        count_recent_birth_year = df[df['Birth Year'] == recent_birth_year].count()[0]
        print('Most Recent year of Birth:', int(recent_birth_year), "count:", count_recent_birth_year)

        common_birth_year = df['Birth Year'].mode()[0]
        count_common_birth_year = df[df['Birth Year'] == common_birth_year].count()[0]
        print('Most Common year of Birth:', int(common_birth_year), "...", "count:", count_common_birth_year)

    else:
        print("\nUser Birth Stats: The Birth year column doesnt exist in the file selected")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*75)
###################################################################################################

def main():
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank You...Good Bye")
            break


if __name__ == "__main__":
	main()
