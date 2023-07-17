#Write apython program to sort the dictionary first by key than by values

d={'beth':37,'zane':32,'john':41,'amy':41,'mike':59,'jane':43}


key=list(d.keys())
key.sort()
As_sort={i:d[i] for i in key}
print(As_sort)

Ds_sort=dict(sorted(d.items(),key=lambda item:item[1]))
print(Ds_sort)

# >>> people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

# >>> # Sort by key
# >>> dict(sorted(people.items()))
# {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}

# >>> # Sort by value
# >>> dict(sorted(people.items(), key=lambda item: item[1]))