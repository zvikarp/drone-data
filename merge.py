import glob, os
import csv

def main():
    os.chdir("data/csv")
    for root, dirs, files in os.walk(".", topdown=False):
        print(root)
        real_name = root[2:]
        states = []
        with open(real_name + "/" + real_name + "_vehicle_status_0.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                states.append([row[0], row[6]])
        last_timestamp_index = 1
        new_csv = []
        with open(real_name + "/" + real_name + "_vehicle_local_position_0.csv") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if (row[0] == 'timestamp'):
                    row.append('state')
                else:
                    timestamp = row[0]
                    if (timestamp < states[last_timestamp_index][0]):
                        row.append(states[last_timestamp_index][1])
                    elif (len(states)-1 <= last_timestamp_index):
                        row.append(states[last_timestamp_index][1])
                    else:
                        last_timestamp_index = last_timestamp_index + 1
                        row.append(states[last_timestamp_index][1])
                new_csv.append(row)
        with open(real_name + "/" + real_name + "_vehicle_local_position_with_state_0.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(new_csv)
        break

if __name__ == '__main__':
    main()