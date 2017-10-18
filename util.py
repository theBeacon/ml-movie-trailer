import unicodecsv;

def read_csv(file):
    """ loads the csv as list of dictionary from the specfied file """
    with open(file, "rb") as f:
        return list(unicodecsv.DictReader(f))