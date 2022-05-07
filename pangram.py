userI = int(input())
userdata = str(input())
a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
userdata = userdata.lower()
for i in userdata:
    if i in a:
        a.remove(i)
        if len(a) == 0:
            break
if (len(a) == 0):
    print("YES")
else:
    print("NO")
