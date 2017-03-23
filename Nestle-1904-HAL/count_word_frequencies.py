import sys

def read_freq_dict(infilename):
    result = {} # Strong's -> frequency

    for line in open(infilename):
        line = line.strip()
        if line == "":
            continue

        strongs = int(line)

        result.setdefault(strongs, 0)
        result[strongs] += 1

    return result

def mycmp(o1, o2):
    if o1[1] < o2[1]:
        return 1
    elif o1[1] > o2[1]:
        return -1
    elif o1[0] < o2[0]:
        return 1
    elif o1[0] > o2[0]:
        return -1
    else:
        return 0

def get_freq_list(freq_dict):
    mylist = [(strongs, freq_dict[strongs]) for strongs in freq_dict]

    mylist.sort(mycmp)

    return mylist

def write_freq_list(freq_list):
    for (strongs, freq) in freq_list:
        sys.stdout.write("%d\t%d\n" % (strongs, freq))
        

def doIt():
    freq_dict = read_freq_dict("nestle1904.strongs.txt")

    freq_list = get_freq_list(freq_dict)

    write_freq_list(freq_list)

if __name__ == '__main__':
    doIt()
