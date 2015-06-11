# coding=utf8
import urllib2
import urllib


url = 'http://192.0.0.6/cgi-bin/do_login'
count = 1

headers = {'User-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'}
success = False
while not success:
	user = "linshi%03d" % count
	print user
	post_data = {'username': user, 'password': '123321'}
	data = urllib.urlencode(post_data)
	req = urllib2.Request(url, data, headers)
	response = urllib2.urlopen(req)
	page = response.read()
	try:
		# print page
		int(page)
		success = True
		print "%s login success!" % user
	except ValueError:
		count += 1
		continue

