import webbrowser
search_terms = ["toy"]

# ... construct your list of search terms ...

for term in search_terms:
    url = "https://www.google.com.tr/search?q={}".format(term)
    webbrowser.open_new_tab(url)