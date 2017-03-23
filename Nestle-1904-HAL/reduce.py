import sys
import os

import util

def read_and_reduce_infile(infilename, stopwords_set):
    result = []
    for line in open(infilename, "rb"):
        uline = line.strip()

        if uline != u"":
            strongs = int(uline)
            if strongs in stopwords_set:
                continue
            else:
                result.append(strongs)

    return result
    

def write_outfile(outfilename, result):
    fout = open(outfilename, "wb")

    for strongs in result:
        fout.write("%d\n" % strongs)

    fout.close()

def doIt(stopwords_infilename, infilename, outfilename):
    sys.stderr.write("Now reading and reducing %s\n" % infilename)
    stopwords_set = util.read_stopwords(stopwords_infilename)
    result = read_and_reduce_infile(infilename, stopwords_set)
    write_outfile(outfilename, result)
    sys.stderr.write("... Done! Now look in:\n\t%s\n" % outfilename)


if __name__ == '__main__':
    stopwords_infilename = sys.argv[1]
    infilename = sys.argv[2]
    outfilename = sys.argv[3]
    
    doIt(stopwords_infilename, infilename, outfilename)
