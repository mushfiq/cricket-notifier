"""
    this file contains all the utils functions
"""
import argparse

def parse_input():
    """ parse user input and return as args ( truple ) """
    parser = argparse.ArgumentParser(description='Parse user given paramter')
    parser.add_argument('--url', type=str, help='Give your live match url')
    parser.add_argument('--delay', help='Provide how often the score notifier will be displayed')
    args = parser.parse_args()
    return args
