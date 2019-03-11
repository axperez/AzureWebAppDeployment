import argparse
import sys
import os
import mechanize # sudo pip3 install mechanize

# https://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size
def sizeof_fmt(num, suffix='B'):
	for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
		if abs(num) < 1024.0:
			return "%3.1f %s%s" % (num, unit, suffix)
		num /= 1024.0
	return "%.1f %s%s" % (num, 'Yi', suffix)

# parses command line arguments for URL, input file, and count
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', dest='URL', help='This specifies the URL to autofill.', default='http://127.0.0.1:8000/')
parser.add_argument('-f', '--file', dest='FILE', help='This specifies the file to read data from.', default='data.txt')
parser.add_argument('-c', '--count', dest='COUNT', help='This specifies the number of times to submit the form.', type=int, default=1)
args = parser.parse_args()

if args.COUNT <= 0:
	print('\nThe count must be greater than 0!\n')
	sys.exit(1)

statinfo = os.stat(args.FILE)
file_size = sizeof_fmt(statinfo.st_size)

print('\n\n')
print("Reading input file '" + args.FILE + "' (size: " + file_size + ")...")

# saves the contents of the input file into a String
with open(args.FILE, 'r') as myfile:
	file_data = myfile.read()

print('Input file has been read and stored into script memory.')

br = mechanize.Browser() # initiating a browser
br.set_handle_robots(False) # ignore robots.txt
br.addheaders = [("User-agent", "Mozilla/5.0")] # our identity

bot = br.open(args.URL)

print("\nThe url '" + args.URL + "' has been opened in mechanize.Browser().\n\n")

counter = 1
while counter <= args.COUNT:
	br.select_form(nr=0)
	br['data'] = file_data

	print('\nForm Submission ' + str(counter) + ' of ' + str(args.COUNT) + ':')
	print('\tSubmitting the form with data from the input file...')

	sign_up = br.submit()

	print('\tThe form has been submitted!')

	counter += 1

print('\n\n')