
const char str1[]="ABCDEF1234567"
const char str2[]="269"

len = strcspn(str1,str2)

print("first matching is at %d\n",len+1)
