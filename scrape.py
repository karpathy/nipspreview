# scrape the NIPS25.html file looking for authors names, titles
# and create a database of all papers. This is necessary because
# extracting the authors and titles from PDFs directly is tricky.

from HTMLParser import HTMLParser
import cPickle as pickle

class Paper:
	def __init__(self):
		self.paper = "" # the id of the paper
		self.title = "" # the title of the paper
		self.authors = "" # the author list of the paper

# create a subclass of HTMLParser and override handler methods
# this is an event-driven parser so we maintain a state etc.
# this is super hacky and tuned to the specifics of the .html 
# page provided by NIPS.
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.firstPaperEncountered = False
		self.curPaper = Paper()
		self.allPapers = []

	def handle_starttag(self, tag, attrs):
		if not tag == 'a': return

		# attrs is a list of (key, value) pairs
		for k,v in attrs:
			if k == 'name':
				print "New paper: " + v
				
				if self.firstPaperEncountered:
					# push current paper to stack
					self.allPapers.append(self.curPaper) 

				# this signals new paper being read
				self.curPaper = Paper() # start a new paper
				self.curPaper.paper = v[1:] # for some reason first character is P, then follows the 4-digit ID
				self.firstPaperEncountered = True

	def handle_endtag(self, tag):
		if not self.firstPaperEncountered: return

	def handle_data(self, data):
		if not self.firstPaperEncountered: return

		# there are many garbage data newlines, get rid of it
		s = data.strip()
		if len(s) == 0: return

		# title is first data encountered, then authors
		if self.curPaper.title == "": 
			self.curPaper.title = data
			print 'title ' + data
			return

		if self.curPaper.authors == "": 
			self.curPaper.authors = data
			print 'authors ' + data
			return


parser = MyHTMLParser()
f = open('nips25offline/nips25.html').read()
parser.feed(f)

outdict = {}
for p in parser.allPapers:
	outdict[p.paper] = (p.title, p.authors)

# dump a dictionary indexed by paper id that points to (title, authors) tuple
pickle.dump(outdict, open("papers.p", "wb"))

