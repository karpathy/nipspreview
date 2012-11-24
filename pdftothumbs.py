# go over all pdfs in NIPS and use imagemagick to convert 
# them all to a sequence of thumbnail images
# requires sudo apt-get install imagemagick

import os

relpath = "nips25offline/content/"
allFiles = os.listdir(relpath)
pdfs = [x for x in allFiles if x.endswith(".pdf")]

for i,f in enumerate(pdfs):
	paperid = f[9:-4]
	fullpath = relpath + f

	print "processing %s, %d/%d" % (paperid, i, len(pdfs))

	# this is a mouthful... 
	# take first 8 pages of the pdf ([0-7]), since 9th page are references
	# tile them horizontally, use JPEG compression 80, trim the borders for each image
	cmd = "montage %s[0-7] -mode Concatenate -tile x1 -quality 80 -resize x230 -trim %s" % (fullpath, "thumbs/" + f + ".jpg")
	print "EXEC: " + cmd
	os.system(cmd)
	

# an alternate, more roundabout alternative that is worse and requires temporary files, yuck!
#cmd = "convert -thumbnail x200 %s[0-7] test.png" % (fullpath, )
# os.system(cmd)
#cmd = "montage -mode concatenate -quality 80 -tile x1 test-*.png %s" % ("thumbs/" + f + ".jpg", )
# os.system(cmd)
