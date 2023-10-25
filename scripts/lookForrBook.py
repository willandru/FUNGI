from libgen_api import LibgenSearch
s = LibgenSearch()
results = s.search_title("Myxomycetes")
item_to_download = results[7]
download_links = s.resolve_download_links(item_to_download)
##print(item_to_download)
print(download_links)