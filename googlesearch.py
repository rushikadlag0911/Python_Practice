from googlesearch import search
query = "Rushi kiran kadlag"
for i in search(query, start=0, pause=2):
    print(i)
