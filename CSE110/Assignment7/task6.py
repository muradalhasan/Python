def calc_yead(days):
    year=days//365
    rem_day=days%365
    month=rem_day//30
    day=rem_day%30
    print(f"{year} years, {month} months and {day} days")
calc_yead((int(input())))