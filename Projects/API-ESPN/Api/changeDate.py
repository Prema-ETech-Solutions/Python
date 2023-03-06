
def dateChange(a):
    a = a.split(' ')
    month =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    index = month.index(a[1])
    index = index+1
    if index <=9:
        index = "0"+str(index)
    if len(a) == 4:
        return str(a[3]) +"-"+str(index) +"-"+str(a[2])
    elif len(a) == 6:
        return str(a[5]) +"-"+str(index) +"-"+str(a[2])
    else:
        return "NA"
