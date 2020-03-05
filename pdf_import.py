import os
import sys
import tabula

## pdf file location
## file = "20200121_COVID-19_SR001.pdf"

## Add relative path to py script to provide full path for pdf file.
file = os.path.join(sys.path[0], "20200121_COVID-19_SR001.pdf")
print(file)

tables = tabula.read_pdf(file, pages = "all", multiple_tables = True)
