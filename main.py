mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

mission_number = 0
successful_missions = 0

for missions in mission_names:
    mission_number += 1

print("The number of missions is: ", mission_number)

for tru in mission_success:
    if tru == True:
        successful_missions += 1

print("The number of successful missions is: ", mission_number)

success_rate = successful_missions /mission_number
success_string = str(success_rate)

print("The rate of mission success is: " + success_string + "%.")

twentieth_century_years = mission_years
twentieth_century_names = mission_names

index = 0

for twentieth_century in mission_years:
    if twentieth_century > 2000:
        del twentieth_century_years[index]
        del twentieth_century_names[index]
    index += 1

relation_list = [(twentieth_century_years[twentieth_century], twentieth_century_names[twentieth_century]) for twentieth_century in range(len(twentieth_century_years))]
print(relation_list)