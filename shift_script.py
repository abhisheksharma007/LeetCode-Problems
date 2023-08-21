from datetime import datetime
import datetime
from os.path import exists


current_day = datetime.datetime.now().day
current_month = datetime.datetime.now().month
current_year = datetime.datetime.now().year
today = datetime.datetime.today().strftime('%d_%m_%y')
start_time = datetime.datetime.now().strftime('%H:%M:%S')
current_time = datetime.datetime.now().strftime("%H:%M:%S")

# print(today)
file = '/var/www/html/shift/shifttime_'+today+'.txt'

if not exists(file):
    content = [ f'Start Time : {start_time}\n' , f'Current Time : {current_time}\n' ,'Completed Hours : 00:00:00\n']
    f = open(file, 'a+')
    f.writelines(content)
    f.close()

f = open(file, 'r')
lines = f.readlines()
start_time = datetime.datetime.strptime(lines[0].rstrip().lstrip('Start Time : '), '%H:%M:%S')
current_time = datetime.datetime.strptime(current_time, '%H:%M:%S')

completed_hours = current_time - start_time

lines[1] = f'Current Time : {current_time.strftime("%H:%M:%S")}\n'
lines[2] = f'Completed Hours : {completed_hours}\n'

a_file = open(file, "w")
a_file.writelines(lines)
a_file.close()
# print(content)