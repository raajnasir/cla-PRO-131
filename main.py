import csv


rows = []

with open("total_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]

print(headers)
print(star_data_rows)

headers[0] = "row_num"

temp_stars_data_rows = list(star_data_rows)
for star_data in temp_stars_data_rows:
    star_mass = star_data[3]
    if star_mass.lower() == "unknown":
        star_data_rows.remove(star_data)
        continue
    else:
        star_mass_value = star_mass.split("")[0]
        star_mass_ref = star_mass.split("")[1]
        if star_mass_ref == "Icarus":
            star_mass_value = float(star_mass_value) * 1.989e+30
        star_data[3] = star_mass_value

    star_radius = star_data[4]   
    if star_radius.lower() == "unknown":
        star_data_rows.remove(star_data)
        continue
    else:
        star_radius_value = star_radius.split("")[0]
        star_radius_ref = star_radius.split("")[2]
        if star_radius_ref == "Icarus":
            star_radius_value = float(star_radius_value) * 6.957e+8
        star_data[4] = star_radius_value 

print(len(star_data_rows))



