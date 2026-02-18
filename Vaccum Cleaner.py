rooms = {'A':'Dirty','B':'Dirty'}
pos='A'

while 'Dirty' in rooms.values():
    if rooms[pos]=='Dirty':
        print("Cleaning",pos)
        rooms[pos]='Clean'
    pos = 'B' if pos=='A' else 'A'

print("All Clean")
