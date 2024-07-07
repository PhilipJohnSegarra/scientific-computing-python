#my version of the code
def add_time_myVersion(start, duration = '0:00', dayOfTheWeek = 'None'):
    days_of_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    days_of_week_lowered = [day.lower() for day in days_of_week]
    day_index = days_of_week_lowered.index(dayOfTheWeek.lower()) if dayOfTheWeek != 'None' else 0
    #get am/pm
    day = start[5::].replace(' ', '').upper()
    time_dict = {
        'starttime': int(start[:4:].split(':')[0]) if day == 'AM' else int(start[:4:].split(':')[0]) + 12,
        'starttime_mins': int(start[:5:].split(':')[1]),
        'duration_hour':int(duration.split(':')[0]),
        'duration_mins': int(duration.split(':')[1])
    }
    
    if time_dict['starttime'] == 12 and day == 'AM':
        time_dict['starttime'] = 0

    numberof_nextdays = 0
    hour_result = (time_dict['starttime'] + time_dict['duration_hour']) if (time_dict['starttime_mins'] + time_dict['duration_mins']) < 60 else ((time_dict['starttime'] + time_dict['duration_hour']) + 1)
    mins_result = (time_dict['starttime_mins'] + time_dict['duration_mins']) if (time_dict['starttime_mins'] + time_dict['duration_mins']) < 60 else (time_dict['starttime_mins'] + time_dict['duration_mins']) - 60
    if hour_result < 24:
        return str('12' if hour_result - 12 == 0 else abs(hour_result - 12)) + ':' + (str("{:02}".format(mins_result)) if mins_result != 0 else '00') + ' ' + ('AM' if (hour_result) < 12 else 'PM') + ((', ' +days_of_week[day_index]) if dayOfTheWeek != 'None' else '')
    elif hour_result >= 24:
        numberof_nextdays = hour_result // 24
        day_index = (day_index + numberof_nextdays) % 7
        time_of_day = abs((hour_result % 24))
        return str('12' if time_of_day == 0 else time_of_day) + ':' + (str("{:02}".format(mins_result)) if mins_result != 0 else '00') + ' ' + ('AM' if time_of_day < 12 else 'PM') + ((', ' + days_of_week[day_index]) if dayOfTheWeek != 'None' and numberof_nextdays >= 1 else '') + ' ' + ('(next day)' if numberof_nextdays == 1 else f'({numberof_nextdays} days later)')


def add_time(start, duration='0:00', dayOfTheWeek='None'):
    # Days of the week lists
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    days_of_week_lowered = [day.lower() for day in days_of_week]
    
    # Find the index of the day of the week
    day_index = days_of_week_lowered.index(dayOfTheWeek.lower()) if dayOfTheWeek != 'None' else 0
    
    # Extract AM/PM from the start time
    day_period = start[-2:].strip().upper()
    
    # Extract hours and minutes from the start time
    start_hour, start_minute = map(int, start[:-2].strip().split(':'))
    
    # Convert the start time to 24-hour format
    if day_period == 'PM' and start_hour != 12:
        start_hour += 12
    elif day_period == 'AM' and start_hour == 12:
        start_hour = 0
    
    # Extract hours and minutes from the duration
    duration_hours, duration_minutes = map(int, duration.split(':'))
    
    # Calculate the total minutes
    total_start_minutes = start_hour * 60 + start_minute
    total_duration_minutes = duration_hours * 60 + duration_minutes
    total_minutes = total_start_minutes + total_duration_minutes
    
    # Calculate the new time
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    
    # Calculate the number of days later
    days_later = (total_minutes // 60) // 24
    
    # Determine AM/PM for the new time
    if new_hour >= 12:
        new_period = 'PM'
        if new_hour > 12:
            new_hour -= 12
    else:
        new_period = 'AM'
        if new_hour == 0:
            new_hour = 12
    
    # Format the new time
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"
    
    # Add the day of the week if provided
    if dayOfTheWeek != 'None':
        new_day_index = (day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"
    
    # Add the number of days later if applicable
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time

if __name__ == '__main__':
    print(add_time('11:59 PM', '24:05'))
    print(add_time_myVersion('11:59 PM', '24:05'))

