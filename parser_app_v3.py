import camelot
import cv2

tables = camelot.read_pdf('/Volumes/1TB External/work/ctba/state_pension/il_state_pensions_2021/gars_2021.pdf', pages="34")

tables

tables.export('/Volumes/1TB External/work/ctba/state_pension/il_state_pensions_2021/gars_2021.pdf',pages=34, f='csv', compress=True) # json, excel, html, markdown, sqlite
tables[0]

tables[0].parsing_report
tables[0].to_csv('test.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
tables[0].df # get a pandas DataFrame!