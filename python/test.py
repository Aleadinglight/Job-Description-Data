from getPageElement import getContent
import pandas as pd
import xlsxwriter
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("link", help="Input the result link of the job search.")
args = parser.parse_args()

print(args.link)