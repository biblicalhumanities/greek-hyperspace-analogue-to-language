import sys
import re
import os

start_section_re = re.compile(r'^(\d+)\s+=\s+\[\s*$')
middle_re = re.compile(r'^\s+(\d+)\s+:\s+([\d\.]+)\s+(\d+)\s*$')
end_section_re = re.compile(r'^\]\s+(\d+)\s*$')

from util import *

def read_HAL(infilename, stopwords_set):
    result = {} # int-strongs -> [(int-strongs, float-score, int-frequency),...]
    for line in open(infilename):
        if line.strip() == "":
            continue
        
        mo_middle = middle_re.match(line)
        if mo_middle != None:
            related_strongs = int(mo_middle.group(1))
            if related_strongs not in stopwords_set:
                score = float(mo_middle.group(2))
                frequency = int(mo_middle.group(3))
                result[cur_strongs].append((related_strongs, score, frequency))
        else:
            mo_start = start_section_re.match(line)
            if mo_start != None:
                cur_strongs = int(mo_start.group(1))
                if cur_strongs in result:
                    raise Exception("Error: cur_strongs = %d already in result." % cur_strongs)
                result[cur_strongs] = []
            else:
                mo_end = end_section_re.match(line)
                if mo_end != None:
                    cur_strongs = None
                else:
                    pass

    return result

def write_HAL(result, outfilename):
    fout = open(outfilename, "wb")
    for strongs in sorted(result):
        count = 0
        for (related_strongs, score, frequency) in result[strongs]:
            count += 1
            if count > 15:
                break
            fout.write(u"%d\t%d\t%d\n" % (strongs, related_strongs, frequency))
    fout.close()

def doIt(stopwords_infilename, infilename, outfilename):
    stopwords_set = read_stopwords(stopwords_infilename)
    result = read_HAL(infilename, stopwords_set)

    write_HAL(result, outfilename)
    sys.stderr.write("... Done! Now look in:\n\t%s\n" % outfilename)

if __name__ == '__main__':
    stopwords_infilename = sys.argv[1]
    infilename = sys.argv[2]
    outfilename = sys.argv[3]
    doIt(stopwords_infilename, infilename, outfilename)
        
