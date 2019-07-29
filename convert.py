import glob, os


def main():
    os.chdir("data/ulg")
    for file in glob.glob("*.ulg"):
        os.system("ulog2csv -o ../csv/" + file.split(".")[0] + " " + file)
        print(file)


if __name__ == '__main__':
    main()