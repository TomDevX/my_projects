def day_of_week(date_str):
    # Parse the input date
    day, month, year = map(int, date_str.split('/'))
    
    # Adjust month and year for Zeller's congruence
    if month < 3:
        month += 12
        year -= 1
        
    K = year % 100
    J = year // 100
    
    # Zeller's Congruence formula to calculate day of the week
    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 - 2 * J) % 7
    
    # Mapping Zeller's output to the correct day of the week
    days = ['T7', 'CN', 'T2', 'T3', 'T4', 'T5', 'T6']
    
    return days[h]

# Input date in DD/MM/YYYY format
input_date = input().strip()
# Output the corresponding day of the week
print(day_of_week(input_date))
