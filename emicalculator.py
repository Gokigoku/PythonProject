loneamount=1000000
mounts=36
roipery=9
year=mounts//12
interst=roipery*year
tamount=(loneamount+(loneamount*(interst/100)))/mounts
print(round(tamount))