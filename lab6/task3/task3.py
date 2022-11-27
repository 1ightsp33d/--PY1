OUTPUT_FILE = "output.csv"


# TODO реализовать функцию to_csv_file
# - ...No one has ever done anything like this. 
# - That's why it's going to work.

headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

# TODO вызвать функцию to_csv_file и записать данные в файл

def to_csv_file(filename, header_list, row_list, delim_list= ",", newline = '\n'):

    header_list = f'{delim_list}'.join(header_list) + newline
    with open(filename, 'w') as file:
        file.write(header_list)
        for l in row_list:
            if l is row_list[-1]:
                l = [x.rstrip() for x in l]
                l = f'{delim_list}'.join(l)
            else:
                l = f'{delim_list}'.join(l) + newline
            file.write(l)
with open(OUTPUT_FILE) as out_f:
    for line in out_f:
        print(line, end="")
