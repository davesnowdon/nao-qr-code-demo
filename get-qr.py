#! /usr/bin/python

import sys
import urllib


SIZE=512

# https://developers.google.com/chart/infographics/docs/qr_codes#details
CHART_URL="https://chart.googleapis.com/chart?cht=qr&chs={}x{}&choe=TUF-8&chl=".format(SIZE, SIZE)

args = sys.argv[1:]
text=args[0]
filename = args[1]

print "Encoding '{}' into image {}".format(text, filename)
url = CHART_URL + urllib.quote(text)
print url
urllib.urlretrieve(url, filename)
