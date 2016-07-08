def dict_compare(d1, d2):
    d1_keys = set(d1.keys())
    d2_keys = set(d2.keys())
    intersect_keys = d1_keys.intersection(d2_keys)
    added = d1_keys - d2_keys
    removed = d2_keys - d1_keys
    modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
    same = set(o for o in intersect_keys if d1[o] == d2[o])
    return added, removed, modified, same

def what_we_care_about(modified, keys_we_care_about):
    keys = keys_we_care_about.split(',')
    return [x for x in keys if x in modified]

x = dict(a=1, b=2, c="John", f="x", y=False, z=True)
y = dict(a=2, b=2, c="Doe", d="y", y=True, z=True)
keys_we_care_about = "a,b,c,z,q"


added, removed, modified, same = dict_compare(x, y)
# print "added:", added
# print "removed:", removed
# print "modified:", modified
# print "same:", same

# only keep the keys_we_care_about
# print
print "before", x
print "after", y
print
print "keys we care about (even ones that don't exist)", keys_we_care_about
print "keys that are different", [x for x in modified]
care = what_we_care_about(modified, keys_we_care_about)
print "keys we care about:", care
print
print "What really matters"
for x in care:
    print x, ": was-", modified[x][0], "now-", modified[x][1]


#HICCUP Isnt a Cool Client Update Program
