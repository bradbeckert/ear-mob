import gsheets
from gsheets import Sheets
import pandas as pd

gsheets.get_credentials()
sheets = Sheets.from_files('~/client_secrets.json', '~/storage.json')
sheets  #doctest: +ELLIPSIS

s = sheets.get('https://docs.google.com/spreadsheets/d/1Ag4RYqsYs3iqWsXqaDiWklDToUIXorakxkP5jb85bEw')
s.find('Album List')
s.sheets[0].to_csv('Ratings.csv', encoding='utf-8', dialect='excel')

df = s.sheets[0].to_frame()
pd.set_option('display.max_columns', 10)
print(df)