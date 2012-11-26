# attempts to extract abstracts from the .pdfs 
# this is a tricky process and will fail for some papers, in which
# case the script tries to alert the user
# this file is super hacky I'd adwise careful use

# output is a set of files inside abstracts/ folder , one for each paper

import os
from string import punctuation
from operator import itemgetter

# get list of all PDFs supplied by NIPS
relpath = "nips25offline/content/"
allFiles = os.listdir(relpath)
pdfs = [x for x in allFiles if x.endswith(".pdf")]

for i,f in enumerate(pdfs):
	paperid = f[9:-4]
	fullpath = relpath + f

	print "processing %s, %d/%d" % (paperid, i, len(pdfs))

	# create text file from the pdf contet
	cmd = "pdftotext %s %s" % (fullpath, "out.txt")
	#print "EXEC: " + cmd
	os.system(cmd)

	txt = open("out.txt").read()
	L = txt.split("\n")

	# basically, we find the line that says Abstract
	# and then go down until we see an empty line
	# i couldn't find a better way because there is a lot
	# of variation. On NIPS 2012 papers, this fails for 
	# 2 badly formatted papers, in which case the script
	# alerts the user, I had to go in open that file manually
	# and fix the abstract text inside it.
	print "----------"
	i=0
	while (not L[i]=="Abstract") and i<len(L): i+=1
	str = []
	while (not L[i]=="") and i<len(L): 
		i+=1
		str.append(L[i])
	abstract = " ".join(str)
	print abstract
	print len(abstract)
	print "----------"

	f = open("abstracts/a%d.txt" % (int(paperid), ), "w")
	f.write(abstract);
	f.close()

	# suspicious: this abstract is too long. Maybe its right,
	# let the user deicde. If not, user can go in and fix the
	# mistake manually
	if len(abstract) > 2000:
		print txt[:3000]
		print paperid
		a= raw_input()


