def fix_names(name, position, added_phrase):
    if position == 'prefix' :
        return added_phrase + ' ' + name
    return name + ' ' + added_phrase

print(fix_names("Gerald", "prefix", "Dr."))
print(fix_names("Robert Downey", "suffix", "Jr."))
print(fix_names("Marvel", "prefix", "Captain"))