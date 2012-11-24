
# NIPS papers pretty html

This is a set of scripts for creating nice preview page (see here: http://cs.stanford.edu/~karpathy/prettynips/ ) for all papers published at NIPS. I hope these scripts can be useful to others to create similar pages for other conferences. They show how one can manipulate PDFs, extract image thumbnails, analyze word frequencies, etc.

#### Installation

0. Clone this repository to $FOLDER `git clone https://github.com/karpathy/nipspreview.git`

1. Download nips25offline from `http://books.nips.cc/nips25.html` and move it into $FOLDER.

2. Install ImageMagick: `sudo apt-get install imagemagick`

3. Run `pdftowordcloud.py` (to generate top words for each paper. Output saved in topwords.p as pickle)

4. Run `pdftothumbs.py` (to generate tiny thumbnails for all papers. Outputs saved in thumbs/ folder)

5. Run `scrape.py` (to generate paperid, title, authors list by scraping NIPS .html page)

6. Finally, run `generatenice.py` (to create the nipsnice.html page)

#### Licence

WTFPL licence
