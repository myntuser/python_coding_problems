# imports
import datetime
from datetime import timedelta

# try for specific import
try:
    import ConfigParser
except:
    print "No such libraries in the lib"
    exit(1)

#  start of the main script

if __name__ == "__main__":
    # number of records to be written
    config = ConfigParser.RawConfigParser()
    try:
        config.read('input.cfg')
        rec = config.get('CSV', 'rec_count')
    except:
        print "The configuration is not defined properly"
        exit(1)

    rec = int(rec)
    # initial values of a, b
    a = 1.0; b = 2.0
    ini_ord = 65
    # start time
    st_time = datetime.datetime.now()

    # open file for writing
    writer = open('output.csv', 'w')

    # write header
    writer.write("Row1, Row2, Row3, Row4, Row5\n")

    for i in range(1, rec + 1):
        # increment time by 5 minutes
        end_time = st_time + timedelta(minutes=5)
        st_fmt = st_time.strftime("%Y%m%d000000+%H%M")
        end_fmt = end_time.strftime("%Y%m%d000000+%H%M")

        # format the string to be written
        print_str = chr(ini_ord) + ", " + str(a) + ", " + str(b) + ", " + st_fmt + ", " + end_fmt + "\n"
        writer.write(print_str)
        st_time = end_time

        # increment a, b
        a += 0.1; b += 0.1

        # check for the ordinal values in the range 65--90
        if ini_ord >= 90:
            ini_ord = 65
        else:
            ini_ord += 1

    # close writer
    writer.close()
