import glob, os
import csv


def main():
    for root, dirs, files in os.walk("data/csv/", topdown=False):
        real_name = root[9:]
        if (real_name == ""): continue
        last_state = -1
        last_timestamp = 0
        csv_data = []
        top_row = []
        with open("data/csv/" + real_name + "/" + real_name + "_vehicle_local_position_with_state_0.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if (row[0] == 'timestamp'):
                    top_row = row
                    csv_data.append(top_row)
                elif (row[43] == last_state):
                    csv_data.append(row)
                else:
                    if (int(last_state) > -1):
                        if not os.path.exists("output/" + last_state):
                            os.makedirs("output/" + last_state)
                        with open("output/" + last_state + "/" + real_name + "_" + last_timestamp + ".csv", "w", newline="") as f:
                            writer = csv.writer(f) 
                            writer.writerows(csv_data)
                            last_state = row[43]
                            last_timestamp = row[0]
                            csv_data = [top_row]
                    else: 
                        last_state = row[43]
                        last_timestamp = row[0]
                        csv_data = [top_row]
            if (len(csv_data) > 1):
                if not os.path.exists("output/" + last_state):
                    os.makedirs("output/" + last_state)
                with open("output/" + last_state + "/" + real_name + "_" + last_timestamp + ".csv", "w", newline="") as f:
                    writer = csv.writer(f) 
                    writer.writerows(csv_data)
            



if __name__ == '__main__':
    main()