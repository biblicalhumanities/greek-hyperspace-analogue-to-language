def read_stopwords(infilename):
    result = set()
    for line in open(infilename):
        line = line.strip()

        if line == "":
            continue
        else:
            result.add(int(line))

    return result
            
