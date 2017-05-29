import csv
# open the file - and read all of the lines.
changes_file = 'changes_python.txt'
# use strip to strip out spaces and trim the line.


data = [line.strip() for line in open(changes_file, 'r')]
return data
# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements 
class Commit:
    'class for commits'
 #      Adding the = None sets the default. It means that you do not have to specify a variable name at each point.  
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment

a_commit= Commit('r1551925', 'Thomas', '2015/11/27', 1, None, 'Renamed folder to the correct name')

print a_commit.author
print a_commit.comment
#   Analyse the data
def analyse_data(data):
# Create lists and set index to zero
	commits = []
	current_commit = None
	index = 0
	revisions = []
	authors = []
	dates = []



while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = details[0].strip()
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int (details[3].strip().split(' ')[0])
        print current_commit.comment_line_count
        index = data.index(sep, index + 1)
        current_commit.changes = data[index - current_commit.comment_line_count : index]
        commits.append(current_commit)
    except IndexError:
        break
 	return (commits, revisions, authors, dates)

commits, revisions, authors, dates = analyse_data(data)       
print len(commits)

commits.reverse()
