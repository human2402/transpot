day, month, year = 29, 2, 2023

feb_l = 28
if year % 4 == 0:
    feb_l = 29
mounts_lenght = {
    1: 31,
    2: feb_l,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

result = "date is incorrect"
if (month < 13):
    if(day <= mounts_lenght[month]):
        result ="date is correct"

print (result)
