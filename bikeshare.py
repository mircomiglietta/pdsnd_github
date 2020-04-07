import time
import pandas as pd
import numpy as np
# definition of .csv file
CITY_DATA = CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday','all' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()
        if city in CITIES:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('what month have you chose?').lower()
        if month in MONTHS:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('insert the day that you chose').lower()
        if day in DAYS:
            break
        
    print('-'*40)
    return city, month, day


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
    df= pd.DataFrame(pd.read_csv(CITY_DATA[city]))
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[ df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('the most common start hour is:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('the most common start hour is:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_startstation = df['Start Station'].mode()[0]
    print('the most commonly used start station is:', popular_startstation)

    # TO DO: display most commonly used end station
    popular_endstation = df['End Station'].mode()[0]
    print('the most commonly used end station is:', popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_duration= df['Trip Duration'].sum()
    print('the total travel time is', total_duration)
    # TO DO: display mean travel time
    mean_duration= df['Trip Duration'].mean()
    print('the mean travel time is', mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_users_type=df['User Type'].value_counts()
    print('the counts of user types is', count_users_type)
    # TO DO: Display counts of gender
    count_gender=df['Gender'].value_counts()
    print('the counts of user types is', count_gender)

    if city != 'washington':
    # TO DO: Display earliest, most recent, and most common year of birth
    # Display earliest
        earliest_birth=df['Birth Year'].min()
        print('the earliest year of birth is', earliest_birth)
    
    # TO DO: Display most recent year of birth
        recent_birth=df['Birth Year'].max()
        print('the most recent year of birth is', recent_birth)
    
    # TO DO: Display most common year of birth
        common_birth=df['Birth Year'].mode()[0]
        print('the most common year of birth is', common_birth)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def table_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating Dataset Stats...\n')
    
    # counts the number of missing values in the entire dataset
    number_of_missing_values = np.count_nonzero(df.isnull())
    print("The number of missing values in the {} dataset : {}".format(city, number_of_missing_values))

    # counts the number of missing values in the User Type column
    number_of_nonzero = np.count_nonzero(df['User Type'].isnull())
    print("The number of missing values in the \'User Type\' column: {}".format(number_of_missing_values))

    
    
def display_data(df):
    """Displays raw bikeshare data."""
    row_length = df.shape[0]

    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):
        
        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        table_stats(df, city)

        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()