import csv

def load_verses(inputfile='input/verses.csv'):
    '''
    Loads verses from CSV data file
    inputfile: name of csv file
    returns: verses where verses['ggg.vv.l']=token; where ggg=ghazal #; vv=verse number;l=line number
    '''


    verses = {}
    with open(inputfile,'r') as csvfile:
        versereader = csv.reader(csvfile)
        for row in versereader:
            (verse_id, input_string, real_scan) = row # 
            if not 'x' in verse_id: # only muravvaj divan for now
                verses[verse_id] = input_string.strip() 
    return verses

def load_meters(inputfile='input/verses.csv'):
    meters = {}
    with open(inputfile,'r') as csvfile:
        versereader = csv.reader(csvfile)
        for row in versereader:
            (verse_id, input_string, real_scan) = row # 
            if not 'x' in verse_id: # only muravvaj divan for now
                meters[verse_id] = real_scan
    return meters
    
class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)