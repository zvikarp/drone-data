import glob, os
import csv


def main():
    for root, dirs, files in os.walk("data/csv/", topdown=False):
        filename = root[9:]
        try:
            check_if_csv_for_state_types(filename)
        except expression as identifier:
            pass


def check_if_csv_for_state_types(filename):
    if (filename == ""): return
    last_state = -1
    last_timestamp = 0
    csv_data = []
    top_row = []
    with open("data/csv/" + filename + "/" + filename + "_vehicle_local_position_with_state_0.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if (row[0] == 'timestamp'):
                top_row = row
                csv_data.append(top_row)
            elif (row[43] == last_state):
                csv_data.append(row)
            else:
                if (int(last_state) > -1):
                    save_csv_file("output/" + last_state, filename + "_" + last_timestamp + ".csv", csv_data)
                last_state = row[43]
                last_timestamp = row[0]
                csv_data = [top_row, row]
        if (len(csv_data) > 1):
            save_csv_file("output/" + last_state, filename + "_" + last_timestamp + ".csv", csv_data)


def assure_loction_folder_exists(location):
    if not os.path.exists(location):
        os.makedirs(location)


def save_csv_file(location, filename, file):
    assure_loction_folder_exists(location)
    with open(location + "/" + filename , "w", newline="") as f:
        writer = csv.writer(f) 
        writer.writerows(file)


if __name__ == '__main__':
    main()