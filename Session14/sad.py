def sad(pattern, replace, source, dest): 

    f_source = open(source, 'r')
    f_dest = open (dest, 'w')

    for line in f_source:
        new_line = line.replace(pattern, replace)
        f_dest.write(new_line)

    f_source.close()
    f_dest.close()


pattern = 'man'
replace = 'woman'
source = 'output.txt'
dest = 'new_' + source
sad(pattern, replace, source, dest)
