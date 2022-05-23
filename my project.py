#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("chicago,washington,new york city ")
    city=input("please choose a city \n ").lower()
    while city not in CITY_DATA.keys():
          print ("please enter a valid city and try again ")
          city =input("please choose a city \n ").lower()
    
    # get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','all']
    while True:
        print("january,february,march,april,may,june,all")
        month=input("choose a month \n ").lower()
        if month in months:
            break
        else:
            print("please enter a valid month and try again ")
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days=['sunday','monday','tueday','wednesday','thursday','friday','saturday','all']
    while True:
        day=input("choose a day (sunday,monday,tueday,wednesday,thursday,friday,saturday,all) \n ").lower()
        if day in days:
            break
        else:
            print('please enter a valid day and try again ')  
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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['week_day']=df['Start Time'].dt.day_name()
    df['start hour']=df['Start Time'].dt.hour
    if month != 'all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
        
    if day!= 'all':
        df=df[df['week_day'] == day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month=df['month'].mode()[0]
    print("most common month is ",most_month)

    # display the most common day of week
    most_day=df['week_day'].mode()[0]
    print("most common day of week is ",most_day)
    # display the most common start hour
    most_hour=df['start hour'].mode()[0]
    print("most common start hour is ", most_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_station=df['Start Station'].mode()[0]
    print("most commonly used start station is",most_station)
    # display most commonly used end station
    most_end=df['End Station'].mode()[0]
    print("most commonly used end station is",most_end)

    # display most frequent combination of start station and end station trip
    most_common = (df['Start Station'] + " -- " + df['End Station']).mode()[0]

    print("most frequent combination of start station and end station trip is \n",most_common)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel=df['Trip Duration'].sum()
    print("total travel time",total_travel )
    # display mean travel time
    total_travel_mean=df['Trip Duration'].mean()
    print("mean travel time " ,total_travel_mean )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type=df['User Type'].value_counts()
    print("counts of user types\n", user_type )

    # Display counts of gender
    if city =='washington':
        print("this city doesnt have the gender or age data")
    else:
        gender=df['Gender'].value_counts()
        print("counts of gender\n",gender)


    # Display earliest, most recent, and most common year of birth
        earliest_age= df['Birth Year'].min()
        recent_age=df['Birth Year'].max()
        common_age=df['Birth Year'].mode()[0]
        print("earliest, most recent, and most common year of birth \n",
             earliest_age,"---",recent_age,"-----",common_age)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    #ask the user if he would to display 5 rows from the data
    index=0
    print("you can see 5 rows if you want")
    user_choice=input("type YES if you want to see the 5 rows type NO if you dont\n").lower()
    while user_choice not in ['yes','no']:
        print("please enter a valid choice and try again")
        user_choice=input("type YES if you want to see the 5 rows type NO if you dont\n").lower()
        
    while user_choice=='yes':
             
            print(df.iloc[index: index+5])
            index += 5
            next_rows = input("do you want to see the next 5 rows?\n").lower()
            while next_rows not in ['yes','no']:
                print("please enter a valid choice and try again")
                next_rows = input("do you want to see the next 5 rows? \n").lower()
            if next_rows != 'yes':
                break
                    
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




