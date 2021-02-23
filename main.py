import bs4, requests
page = requests.get('https://studentsandwriters.com/2014/12/24/list-of-1000-adjectives-no-repeats/')
lfile = bs4.beautifulSoup(page.txt,'html.parser') # adds page data to a text file and pasrese it

elem = lfile.select('div.textwidget p')
print(f"NUmber of elements: {len(elem)}")
# print(f"elem[0] = {str(elem[0].getText()}"))