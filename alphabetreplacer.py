from string import ascii_lowercase, ascii_uppercase # get the lowercase + uppercase alphabets
inf = open('KLSadd.tex','r').read() # open the file

##outf = open('alphabetReplaced.tex','w')
##outf.write(inf.translate(str.maketrans(ascii_lowercase+ascii_uppercase, ascii_uppercase+ascii_lowercase)))
##outf.close()
# creates file with replaced data

print(inf.translate(str.maketrans(ascii_lowercase+ascii_uppercase, ascii_uppercase+ascii_lowercase)))
# translates abcdefg...ABCDEFG... -> ABCDEFG...abcdefg...
