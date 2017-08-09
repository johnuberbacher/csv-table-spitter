# Libraries
from cgi import escape

# Load data from CSV
with open ("data.csv", "r") as myfile:
    csvData=myfile.read()

# Generate Table	
def escapeData(row, attr=None):
    cols = escape(row).split(',')
    return ('  <tr>\n'
            + ''.join('    <td>%s</td>\n' % data for data in cols)
            + '  </tr>')
 
def displayTable(txt):
    htmltxt = '<table>\n'
    for rownum, row in enumerate(txt.split('\n')):
        htmlrow = escapeData(row)
        htmlrow = '%s\n' % htmlrow
        htmltxt += htmlrow
    htmltxt += '</table>\n'
    return htmltxt
 
htmltxt = displayTable(csvData)
print (htmltxt)