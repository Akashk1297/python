errorcount = 0
warningcount = 0
criticalcount = 0

file = 'deployment.log'
mydict = {'error': [errorcount, []], 'warning': [warningcount, []], 'critical': [criticalcount, []]}
warningcountlist = []
criticalcountlist = []
errorIpAddress = []

def isIpaddress(var):
    val = var.split('.')
    if len(val) != 4:
        return False
    flag = 0
    for i in val:
        i = int(i)
        if i >= 0 and i <= 255:
            pass
        else:
            flag = 1
    if flag == 0:
        return True


def analyze_logs(file_path):
    global errorcount
    global warningcount
    global criticalcount

    with open(file_path) as f:
        for line in f:
            errorcount = 0
            flag = 0
            wordlist = line.split()

            for word in wordlist:
                print(word)
                if 'ERROR' in word:
                    errorcount += 1
                    flag = 1
                elif 'WARNING' in word:
                    warningcount += 1
                elif 'CRITICAL' in word:
                    criticalcount += 1

                if flag == 1:
                    if isIpaddress(word):
                        errorIpAddress.append(word)

            mydict['error'][0] += errorcount
            mydict['warning'][0] += warningcount
            mydict['critical'][0] += criticalcount
            mydict['error'][1] += errorIpAddress
            mydict['warning'][1] += warningcountlist
            mydict['critical'][1] += criticalcountlist


analyze_logs(file)

print(dict)
