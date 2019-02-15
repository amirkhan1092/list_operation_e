a=input('enter the string ')
h=[] #blank list initialize
st='' #blank string
#for loop for char operation
for i in a:
    if i in st:
        h.append(None)  #  avoid repeated char
    else:
        h.append(a.count(i)) #add the frequency number with list
        st +=i

print('List ',h)

