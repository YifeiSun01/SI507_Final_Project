#!/usr/bin/env python
# coding: utf-8

# In[1]:


from complextree import *


# In[2]:


print("Welcome to Yifei Sun's final project for SI 507!")
print("Here you will explore languages and linguistics using trees and graphs.")
print("Here I have prepared 5 language family for you to explore:")
exit = False
while exit!= True:
    print("Press 1 for Indo-European languages")
    print("Press 2 for Sino-Tibetan languages")
    print("Press 3 for Altaic languages")
    print("Press 4 for Uralic languages")
    print("Press 5 for Afroasiatic languages")
    print("Press 6 to exit")
    answer_1 = int(input("Which language family do you want to explore?"))
    if answer_1 == 1:
        json = "Indo-European language data.json"
    elif answer_1 == 2:
        json = "Sino-Tibetan language data.json"
    elif answer_1 == 3:
        json = "Altaic language data.json"
    elif answer_1 == 4:
        json = "Uralic language data.json"
    elif answer_1 == 5:
        json = "Afroasiatic language data.json"
    elif answer_1 == 6:
        print("Thank you for playing this game!")
        exit = True
    else:
        print("Your choice does not exist! Please try agian!")
    if answer_1 in [1,2,3,4,5]:
        lang_tree = create_tree(json)
        class_simple_lang_tree = creat_simple_tree(json,status="classification")
        proto_simple_lang_tree = creat_simple_tree(json,status="proto")
        exit_2 = False
        while exit_2!=True:
            print("Here you have two options: show the whole tree or only a part of the tree")
            print("Show the whole linguistic tree for "+json.split(" ")[0]+", please press 1")
            print("Show the a part of the linguistic tree for "+json.split(" ")[0]+", please press 2")
            print("If you want exit from this language family, please press 3")
            answer_2 = int(input("Do you want to explore the whole tree or only part of it, or exit?"))
            if answer_2 == 3:
                exit_2 = True
                break
            answer_3 = int(input("Press 1 to show linguistic classification tree\nPress 2 to show Proto language tree"))
            if answer_3 == 1:
                status="classification"
            elif answer_3 == 2:
                status="proto"
            else:
                print("This is not a valid answer")
            if answer_2 == 1:
                show_simple_tree(json,status)
            elif answer_2 == 2:
                answer_6 = int(input("Do you want to search the language tree for a language or linguistic unit? Press 1 for Yes, 2 for No"))
                if answer_6 == 1:
                    lang = input("Please enter the name of the language or linguistic unit that you want to search")
                    answer_7 = int(input("Press 1 if you want simple information\nPress 2 if you want detailed information"))
                    if answer_7 == 1:
                        class_simple_lang_tree.searchLang(lang)
                    elif answer_7 == 2:
                        lang_tree.searchLang(lang)
                    else:
                        print("This not a balid answer")
                    answer_8 = int(input("Do you want to show the lineage of that language?\nPress 1 for Yes\nPress 2 for No"))       
                    if answer_8 == 1:
                        answer_9 = int(input("Press 1 for short information\nPress 2 for detailed information"))
                        if answer_9 == 1:
                            try:
                                find_lineage(json,lang,status,form="short")   
                            except:
                                print("That language you entered does not exist in the tree, probably a misspelling")
                        elif answer_9 == 2:
                            try:
                                find_lineage(json,lang,status,form="long") 
                            except:
                                print("That language you entered does not exist in the tree, probably a misspelling")
                        else:
                            print("This not a valid answer")
                    elif answer_8 == 2:
                        pass
                elif answer_6 == 2: 
                    pass
                else:
                    print("This not a valid answer")
                answer_4 = input("Which sub-branch do you want to explore?")
                answer_5 = int(input("Press 1 for simple tree\nPress 2 for complex tree"))
                if answer_5 == 1:
                    try:
                        show_simple_tree(json,status,start=answer_4)
                    except:
                        print("The branch you enter does not exist. Maybe it is a misspelling. Please check again.")
                elif answer_5 == 2:
                    try:
                        show_complex_tree(json,status,start=answer_4)
                    except:
                        print("The branch you enter does not exist. Maybe it is a misspelling. Please check again.")
                else:
                    print("This is not a valid answer")
            else:
                print("This is not a valid answer")
    


# In[4]:


print("Search a language or linguistic unit")
exit = False
tree_list = []
class_simple_tree_list = []
proto_simple_tree_list = []
json_list = ["Indo-European language data.json","Sino-Tibetan language data.json","Altaic language data.json",             "Uralic language data.json","Afroasiatic language data.json"]
for json in json_list:   
    lang_tree = create_tree(json)
    tree_list.append(lang_tree)
    class_simple_lang_tree = creat_simple_tree(json,status="classification")
    class_simple_tree_list.append(class_simple_lang_tree)
    proto_simple_lang_tree = creat_simple_tree(json,status="proto")
    proto_simple_tree_list.append(proto_simple_lang_tree)
while exit!= True:
    answer_1 = input("Enter a keyword that you would like to search, or press 1 to exit")
    try:
        if int(answer_1) == 1:
            print("Thank you for playing this game!")
            exit=True
    except:
        answer_2 = input("Press 1 for detailed information\nPress 2 for simple information")
        if int(answer_2)==1:
            for lang_tree in tree_list:
                lang_tree.searchLang(answer_1)
            answer_3 = input("Do you want to show the lineage of the language?\nPress 1 for Yes\nPress 2 for No")
            answer_4 = input("Do you want to show the linguistic classification lineage or Proto language lineage of the language?\nPress 1 for linguistic classification\nPress Proto language for No")
            if int(answer_4)==1:
                status="classification"
            elif int(answer_4)==2:
                status="proto"
            if int(answer_3)==1:
                try:
                    for json in json_list:
                        find_lineage(json,answer_1,status=status,form="long")
                except:
                    print("The name of the language you entered does not exist. May be a misspelling. Please try again!")
            elif int(answer_3)==2:
                print("Thank you for playing this game!")
                exit=True
        elif int(answer_2)==2:
            for lang_tree in class_simple_tree_list:
                lang_tree.searchLang(answer_1)
            answer_3 = input("Do you want to show the lineage of the language?\nPress 1 for Yes\nPress 2 for No")
            answer_4 = input("Do you want to show the linguistic classification lineage or Proto language lineage of the language?\nPress 1 for linguistic classification\nPress Proto language for No")
            if int(answer_4)==1:
                status="classification"
            elif int(answer_4)==2:
                status="proto"
            if int(answer_3)==1:
                try:
                    for json in json_list:
                        find_lineage(json,answer_1,status=status,form="short")
                except:
                    print("The name of the language you entered does not exist. May be a misspelling. Please try again!")
            elif int(answer_3)==2:
                print("Thank you for playing this game!")
                exit=True  


# In[5]:


print("Find the lineage of a language or linguistic unit")
exit = False
tree_list = []
class_simple_tree_list = []
proto_simple_tree_list = []
json_list = ["Indo-European language data.json","Sino-Tibetan language data.json","Altaic language data.json",             "Uralic language data.json","Afroasiatic language data.json"]
while exit!= True:
    answer_1 = input("Enter a language or linguistic unit that you would like to search, or press 1 to exit")
    try:
        if int(answer_1) == 1:
            print("Thank you for playing this game!")
            exit=True
    except:
        answer_4 = input("Do you want to show the linguistic classification lineage or Proto language lineage of the language?\nPress 1 for linguistic classification\nPress Proto language for No")
        if int(answer_4)==1:
            status="classification"
        elif int(answer_4)==2:
            status="proto"
        answer_5 = input("Press 1 to get detailed information\nPress 2 to get simple information")
        if int(answer_5)==1:
            form="long"
        elif int(answer_5)==2:
            form="short"
        try:
            for json in json_list:
                find_lineage(json,answer_1,status=status,form=form)
        except:
            print("The name of the language you entered does not exist. May be a misspelling. Please try again!")
            


# In[6]:


print("Visualize the cluster of 242 languages")
exit = False
while exit!= True:
    answer_1 = input("Enter a similarity threshold\nLanguages that have smaller similarity distance value will be connected\nOr press 1 to exit")
    try:
        if int(answer_1) == 1:
            print("Thank you for playing this game!")
            exit=True
    except:
        lang_graph("new_language_distance_data_total.json","lang_list.json",threshold=float(answer_1))
            


# In[ ]:


import re
print("Draw dendrogram of languages")
json_list = ["Indo-European language data.json","Sino-Tibetan language data.json","Altaic language data.json",             "Uralic language data.json","Afroasiatic language data.json"]
exit = False
while exit!= True:
    answer_1 = input("Enter one or more linguistic units that you would like to draw a dendrogram of (separated by commas)\nOr press 1 to exit")
    try:
        if int(answer_1) == 1:
            print("Thank you for playing this game!")
            exit=True
    except:
        if "," in answer_1:
            start = re.split(r" *, *",answer_1)
        else:
            start = answer_1
        try:
            for json in json_list:
                try:
                    lang_dendrogram("new_language_distance_data_total.json","lang_list.json",json=json,start=start)
                except:
                    pass
        except:
            print("The linguistic units you entered can not be drawn. Maybe a misspelling.")


# In[ ]:




