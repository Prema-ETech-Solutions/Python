
def dateChange(a):
    a = a.split(' ')
    month =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    print(a)
    index = month.index(a[1])
    index = index+1
    return str(a[3]) +"-"+str(index) +"-"+str(a[2])  
