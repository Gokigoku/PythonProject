#Time convertion Problem
def timeConversion(s):
    # Write your code here
    t = s.split(":")
    if t[2][2]=="P":
        sec = t[2].strip("PM")
        m = t[1]
        if t[0]!='12':
            h = str(int(t[0])+12)
        else:
            h = t[0]
        return (h+":"+m+":"+sec)
    elif t[2][2]=="A":
        sec = t[2].strip("AM")
        m = t[1]
        if t[0]=='12':
            h = '00'
        else:
            h = t[0]
        return (h+":"+m+":"+sec)
    else:
        return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
#input formate = hh:mm:ssAM/PM
#example=1:23:44PM output=13:23:44
