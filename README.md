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
It also contains the function to search for a language or linguistic unit in the language tree. And it can print the information of all the ancestors
of a language in e lineage. It can print the metadata of any language in the tree. 

complextree.ipynb contains more functions of my project. It can show a more complex graph of the tree using networkx. It can show a graph 
of the languages with similar languages connected by lines and form into clusters using networkx. It can show the dendrogram of languages
using their similarity distance matrix to visualize the evolution and divergence of language. This is done by using dendrogram, and linkage in 
scipy.cluster.hierarchy, and squareform in scipy.spatial.distance. 

interactive.ipynb is the file that a user could use to interact with the program. It use command line prompt to help you explore the linguistic 
dataset. It import all the functions from complextree.py.

There are many packages that are required for my program to work:

In the two scraping files, urllib3, bs4, re, numpy, collections, time, json is required. 

In complextree.py, json, re, treelib, collections, networkx, matplotlib, pydot, itertools, scipy and numpy are required.

You need to install these packages to successfully run my program. 

I build both graph and tree for my project. In show_simple_tree and show_complex_tree, I used packages treelib, and networkx to visualize the tree. 
For networkx, though I build tree, I visualize them using a graph. I build two classes, Tree and Simplified_Tree. In Tree, the elements are instances 
of a new class called Language. In Simplified_Tree, the elements are instances of a new class called Simplified_Language. Tree class build more complex tree.
It has more metadata of each Language instance. It does not contain Language instance that is a dialect. Simplified_Tree class build simpler tree.
It has only the parent and children as metadata of each Simplified_Language instance. It contains dialects as Simplified_Language instance. The tree is constructed
by specifying the children and parent of each node in the tree. 

In lang_graph function, I used networkx to build a graph. Every node is a language in the list of 242 languages. Language paries that have similarity 
distance higher than the threshold are connected by a line. The result will show similar languages form clusters. 

complextree.py is the python file that constructs my graphs or trees from your stored data using classes.

build_tree.py is the file I used to build tree from my json file.

Because I am using class to build the tree rather than tuple, I do not have a json file for the tree.





