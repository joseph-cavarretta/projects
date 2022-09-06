"""
Created on Fri Sept 2 18:02:33 2022
@author: joseph.cavarretta
"""
import pandas as pd


def main():
    df = load_data()


def load_data():
    path = 'data/processed_activities.csv'
    data = pd.read_csv(path)
    return data


class overallReport():
    # this should be the metrics I wnt to see most frequent
    # specific sport reports more granular
    # yearly totals overall
    # yearly totals by sport
    # previous month totals and delta or each metric
    # % by sport
    # summit totals
    pass


class runReport():
    # Run stats by year
    # Run stats by month
    # Run stats by week
    # Other specific metrics
    pass


class strengthReport():
    # strenth totals
    # plyo totals
    # indoor climb and boulder totals
    pass


class climbingReport():
    # grades climbed
    # total pitches
    # total sessions
    # indoor vs outdoor
    pass