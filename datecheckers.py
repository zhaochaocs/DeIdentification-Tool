import re

def isDate(date):
    """Finds dates of the format ##/##/####"""
    pattern = re.compile(r'[^\w]') #find backslash
    pieces = pattern.split(date) #split date string at backslash
    pieces = [int(x) for x in pieces]
    if len(pieces) == 3: #check if this is actually a date
        print "one ran"
        if pieces[0] not in range(1, 13) or pieces[1] not in range(1, 32) or \
           (len(str(pieces[2])) == 3) or \
           (len(str(pieces[2])) == 2 and pieces[2] < 0) or \
           (len(str(pieces[2])) == 4 and pieces[2] not in range(1913,2017)):
            return False
    if len((pieces)) == 2:
        if int(pieces[0]) > 12 or int(pieces[1]) > 2016:
            return False
    try:
        return True
    except len(pieces) != 2 or len(pieces) !=3:
        return False

def main():

    dates = ['2/20/201', '31/23','12/35/2015','6/12/1353']
    for date in dates:
        print "date is %s it is" % date, isDate(date)
        
if __name__ =='__main__':
    main()
