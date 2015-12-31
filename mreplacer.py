inf = open('KLSadd.tex','r').read() # open the file

##outf = open('mReplaced.tex','w')
##outf.write(inf.translate(str.maketrans('mM', 'Mm')))
##outf.close()
# creates file with replaced data

print(inf.translate(str.maketrans('mM', 'Mm')))
# uses str.translate to replace all "m"s with "M"s and all "M"s with "m".
# Note that this method translates both at once, and so is more efficient than str.replace(), where an intermediate would be needed.
