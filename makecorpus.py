# prints all papers into file one per line with words separated by space, to be used with LDA

import os
from string import punctuation
from operator import itemgetter
import re

# load in stopwords (i.e. boring words, these we will ignore)
stopwords = open("stopwords.txt", "r").read().split()
stopwords = [x.strip(punctuation) for x in stopwords if len(x)>2]

# get list of all PDFs supplied by NIPS
relpath = "nips25offline/content/"
allFiles = os.listdir(relpath)
pdfs = [x for x in allFiles if x.endswith(".pdf")]

# go over every PDF, use pdftotext to get all words, discard boring ones, and count frequencies
outf = open("allpapers.txt", "w")
for i,f in enumerate(pdfs):
	paperid = f[9:-4]
	fullpath = relpath + f

	print "processing %s, %d/%d" % (paperid, i, len(pdfs))

	# create text file
	cmd = "pdftotext %s %s" % (fullpath, "out.txt")
	print "EXEC: " + cmd
	os.system(cmd)

	txtlst = open("out.txt").read().split() # get all words in a giant list
	words = [x.lower() for x in txtlst if re.match('^[\w-]+$', x) is not None] # take only alphanumerics
	words = [x for x in words if len(x)>2 and (not x in stopwords)] # remove stop words

	wcount = {} 
	for w in words: wcount[w] = wcount.get(w, 0) + 1
	words = [x for x in words if wcount[x] >= 3] # only take words that occurr at least a bit (for efficiency)

	outf.write(" ".join(words))
	outf.write("\n")
	
outf.close()

