# Project 1: Explore Chicago Bikeshare Data

This is an evaluative test for Udacity's Nanadegree: Artificial Intelligence Programming with Python.

## Objective

Bikeshare systems allow that its users renting a bike for a short period of time and a specific price.
People can take a bike in a point A and return it to a point B or just return it to the same point if they just want to take a ride.
The bikes of this system can be used for many users in a day.

Use Python to explore data related to bikeshare system from Chicago and show through descriptive statistics. 

## Explaining the project

Using data from [Motivate](https://www.motivateco.com/), a bikeshare system provider for various United States' cities, you have to discover the use patterns of bikesharing from Chigago.

### Data Set
The provided data refers to the first six months of 2017. The data file `chicago.csv` contains six main columns:

- Start Time, e.g. **2017-01-01 00:07:57**
- End Time, e.g. **2017-01-01 00:20:53**
- Trip Duration (in seconds), e.g. **776**
- Start Station, e.g. **Broadway & Barry Avenue**
- End Station, e.g. **Sedgwick St & do North Ave** 
- User Type, e.g. **Customer** or **Subscriber**
- Gender, e.g. **Female** or **Male**
- Birth Year, e.g. **1996**

### Tasks

- **Task 1**: Show the first 20 samples (lines) from the data set
- **Task 2**: Show the gender of the first 20 samples
- **Task 3**: Create a function that creates a list with the values of a certain column
- **Task 4**: Count how many people for each gender
- **Task 5**: Create a function that counts gender frequency
- **Task 6**: Show the most popular gender
- **Task 7**: Show a chart using the previous data
- **Task 8**: Answer why are there is no gender for all samples
- **Task 9**: Find the minimum, maximum, average and median travel duration.
- **Task 10**: Show all stations from data set 
- **Task 11**: Check out if all functions have docstring
- **Task 12**: Create a function that counts all the column frequency (optional)

## Running on your own

All code was written with **Python 3.7.1**, so, for a correct running, it is recommended to install this one.

1. After Python installed, it is required to install all dependencies from `requirements.pip` file. If you are using **Virtualenv**, you need to activate the environment and install from **requirements.pip** file with the following commands:

```bash
$ source YOUR_ENVIRONMENT_DIRECTORY/bin/activate
$ pip install -r requirements.pip
```

2. Extract the data set from `chicago_bikeshare_data.tar.gz` file.

3. Run the script with:
```bash
$ python chicago_bikeshare_pt.py
```
