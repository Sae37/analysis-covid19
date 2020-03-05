import tabula

file = "20200121_COVID-19_SR001.pdf"

tables = tabula.read_pdf(file, pages = "all", multiple_tables = True)
