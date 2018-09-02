def sc(word):
    fh = int(len(word)/2)
    silly = word[:fh]
    case = word[fh:].upper()
    return silly+case

a = sc('treehouse')
print(a)
