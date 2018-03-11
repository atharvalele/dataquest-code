## 1. The Time Module ##

import time
current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime()
current_hour = current_struct_time.tm_hour
print(current_hour)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.utcnow()
current_month = current_datetime.month
current_year = current_datetime.year
print(current_datetime)

## 4. Timedelta ##

import datetime
kirks_birthday = datetime.datetime(year = 2233, month = 3, day = 22)
diff = datetime.timedelta(weeks = 15)
before_kirk = kirks_birthday - diff

## 5. Formatting Dates ##

import datetime
mystery_date_formatted_string = mystery_date.strftime("%I:%M%p on %A %B %d, %Y")

## 6. Parsing Dates ##

import datetime
mystery_date_2 = datetime.datetime.strptime(mystery_date_formatted_string, "%I:%M%p on %A %B %d, %Y")
print(mystery_date_2)

## 8. Reformatting Our Data ##

import datetime

for post in posts:
    post[2] = datetime.datetime.fromtimestamp(float(post[2]))

## 9. Counting Posts from March ##

march_count = 0
for post in posts:
    if post[2].month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##

march_count = 0

def count_posts_in_month(month_to_check):
    count = 0
    for row in posts:
        if row[2].month == month_to_check:
            count += 1
    return count

feb_count = count_posts_in_month(2)
aug_count = count_posts_in_month(8)