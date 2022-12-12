# SI507_Final_Project
In this repository, I uploaded all the files and codes for my SI 507 final project.

All the json files are data I scraped from web.

Indo-European language data.json, Sino-Tibetan language data.json, Uralic language data.json, Altaic language data.json, and 
Afroasiatic language data.json are 5 language families I scraped from Wikipedia. They are scraped using the python script 
scraping results wikipedia.ipynb. You can see the scrpaing process if you open the file. All the scraped and rejected Wikipedia page
are printed in the scraping phase. 

lang_list.json, new_language_distance_data_1-30.json, new_language_distance_data_1-78.json, and new_language_distance_data_total.json
are the data I scraped from www.elinguistics.net. They are scraped using the python script scraping results wikipedia.ipynb. You can 
open the file and see the language pairs that are scraped. 

simpletree.ipynb contains the most basic function of my project, which is to show the tree of a linguistic tree using a package called treelib. 

complextree.ipynb contains more functions of my project. It can show a more complex graph of the tree using networkx. It can show a graph 
of the languages with similar languages connected by lines and form into clusters using networkx. It can show the dendrogram of languages
using their similarity distance matrix to visualize the evolution and divergence of language. This is done by using dendrogram, and linkage in 
scipy.cluster.hierarchy, and squareform in scipy.spatial.distance. 


