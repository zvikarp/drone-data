## Drone Data Parser

### install
- clone the repository.
- run `pip install pyulog`

### run
1. download the data from px4 - run `python download.py`, not that this can take a log time (like a couple of hours) so you might what to stop it in the middle.
2. convert from .ulg to .csv - run `python convert.py`.
3. merge the important data to one csv file - run `python merge.py`.
4. output the data to separate folders by flight state - run `python output.py`.
