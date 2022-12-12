#!/usr/bin/env python
# coding: utf-8

# In[4]:


def write_to_json(data,file_name):
    """write a nested dictionary and list into a json file"""
    import json
    data_json = json.dumps(data)
    with open(file_name, "w") as outfile:
        outfile.write(data_json)

def read_from_json(file_name):
    """read a json file into a nested dictionary and list"""
    import json
    with open(file_name, "r",encoding="UTF-8") as outfile:
        read_data = outfile.read()
    return json.loads(read_data)


# In[6]:


def get_list_from_json(json,status,start=None,remove_duplicate=False,branch=None):
    """read the json file into nested dictionary and list, get the field related to language classification
    and proto language. These fields are a list. Collect all these list into a big list and return. If there is
    redundant element in the list, remove them. If there is unnecessary letter or symbol in the text, remove them.
    If there are dialects under one language, for every dialect, create a list and append to the big list. If there is 
    unclear element, make them clear. This big list will be used to build the classification tree."""
    import re
    dictionary = read_from_json(json)
    list_2 = []
    if status == "classification":
        for i in dictionary:
            dict_1 = dictionary[i]
            list_1 = []
            if dict_1.get("Language family corrected")!= None:
                list_1 = dict_1.get("Language family corrected")
            if dict_1.get("Linguistic classification corrected")!= None:
                list_1 = dict_1.get("Linguistic classification corrected")
            if dict_1.get("Dialects")!= None:
                for dialect in dict_1.get("Dialects"):
                    if re.findall(r",|·",dialect)!=[]:
                        dialect_list = re.split(r" *, *| *· *",dialect)
                        for dialect_1 in dialect_list:
                            list_2.append(list_1+[dialect_1])
                    else:
                        dialect_1 = re.sub(r" *◇ *| *◆ *|\*","",dialect)
                        list_2.append(list_1+[dialect_1])
            else:
                list_2.append(list_1)
    if status == "proto":
        for i in dictionary:
            dict_1 = dictionary[i]
            if dict_1.get("Early forms corrected")!= None:
                list_4 = dict_1.get("Early forms corrected")
                if dict_1.get("English Name") != None:
                    list_4.append(dict_1.get("English Name"))
                elif ddict_1.get("Name") != None:
                    list_4.append(dict_1.get("Name"))
                list_2.append(list_4)
            if dict_1.get("Early form corrected")!= None:
                list_4 = dict_1.get("Early form corrected")
                if dict_1.get("English Name") != None:
                    list_4.append(dict_1.get("English Name"))
                elif dict_1.get("Name") != None:
                    list_4.append(dict_1.get("Name"))
                list_2.append(list_4)
    list_3 = [i for i in list_2 if i != []]
    list_3.sort(key=lambda x: len(x)) 
    list_4 = []
    for i in range(len(list_3)):
        a = 0
        for j in range(i+1,len(list_3)):
            if list_3[i] == list_3[j][:len(list_3[i])]:
                a += 1
        if a == 0:
            list_4.append(list_3[i])
    list_4.sort(key=lambda x: len(x),reverse=True)  
    if re.findall(r"altaic",json,re.I|re.M)!=[]:
        list_10 = []
        for i in list_4:
            i = ["Altaic"]+i
            list_10.append(i)
        list_4 = list_10
    if remove_duplicate!=False:
        list_6 = []
        for i in list_4:
            list_5 = []
            for j in range(len(i)):
                if j == 0:
                    list_5.append(i[j])
                else:
                    if i[j-1] == i[j]:
                        pass
                    else:
                        list_5.append(i[j])
            list_6.append(list_5) 
        list_4 = list_6
    list_7 = []
    for i in list_4:
        list_8 = []
        for j in i:
            if j != "" and j != "?":
                list_8.append(re.sub(r" *\? *| *† *|\(.*\)|(\d)+| *\( *| *\) *","",j))
        list_7.append(list_8)
    if start != None:
        list_9 = []
        for i in list_7:
            try:
                list_9.append(i[i.index(start):])
            except:
                pass
        list_7 = list_9
    list_11 = []
    for i in range(len(list_7)):
        list_12 = []
        for j in range(len(list_7[i])):
            if re.findall(r"^ *eastern *$|^ *western *$|^ *southern *$|^ *northern *$|^ *central *$|^ *northeastern *$|^ *northwestern *$|^ *southeastern *$|^ *southwestern *$|^ *insular *$|^ *canadian *$|^ *Costeño *$|^ *Llanero *$|^ *Mainland *$",list_7[i][j],re.I|re.M)!=[]:
                list_12.append(list_7[i][j]+" "+list_7[i][j-1])
            else:
                list_12.append(list_7[i][j])
        list_11.append(list_12)
    list_7 = list_11
    if branch == "Koreanic":
        list_7 = [ x for x in list_7 if 'Koreanic' in x]
    if branch == "Japonic":
        list_7 = [ x for x in list_7 if 'Japonic' in x]
    if branch == "Turkic":
        list_7 = [ x for x in list_7 if 'Turkic' in x]
    if branch == "Mongolic":
        list_7 = [ x for x in list_7 if 'Mongolic' in x]
    if branch == "Tungusic":
        list_7 = [ x for x in list_7 if 'Tungusic' in x]
    return list_7  


# In[7]:


def get_parent_child_pair(json,status,start=None,branch=None):
    list_of_pairs = []
    list_of_list = get_list_from_json(json,status,start,remove_duplicate=True)
    if branch == "Koreanic":
        list_of_list = [ x for x in list_of_list if 'Koreanic' in x]
    if branch == "Japonic":
        list_of_list = [ x for x in list_of_list if 'Japonic' in x]
    if branch == "Turkic":
        list_of_list = [ x for x in list_of_list if 'Turkic' in x]
    if branch == "Mongolic":
        list_of_list = [ x for x in list_of_list if 'Mongolic' in x]
    if branch == "Tungusic":
        list_of_list = [ x for x in list_of_list if 'Tungusic' in x]
    for list_1 in list_of_list:
        for i in range(len(list_1)):
            if i+1!=len(list_1):
                if (list_1[i],list_1[i+1]) not in list_of_pairs:
                    list_of_pairs.append((list_1[i],list_1[i+1])) 
    list_of_pairs.sort(key=lambda x: x[0])        
    return list_of_pairs


# In[2]:


import re
class Language:
    def __init__(self, dictionary):
        self.information = dictionary
        self.proto = {}
        self.classification = {}
        self.proto["parents"] = {}
        self.proto["sole parent"] = []
        self.proto["children"]= {}
        self.proto["depth"] = 0
        self.classification["parents"] = {}
        self.classification["sole parent"] = []
        self.classification["children"] = {}
        self.classification["depth"] = 0
        for i in dictionary:
            if re.findall(r"linguistic classification|language family",i,re.I|re.M) != []:
                if isinstance(dictionary[i],list):
                    self.classification["depth"] = len(dictionary[i])
                else:
                    self.classification["depth"] = 1
            if re.findall(r"early form",i,re.I|re.M) != []:
                if isinstance(dictionary[i],list):
                    self.proto["depth"] = len(dictionary[i])
                else:
                    self.proto["depth"] = 1
 
    def __str__(self):
        return_info = ""
        for i in self.information:
            if re.findall(r"Name|English Name",i,re.I|re.M)!=[] and re.findall(r"Other|Local",i,re.I|re.M)==[]:
                if isinstance(self.information.get(i),list):
                    info = '\033[91m\033[1m'+i+'\033[0m\033[0m'+": "+", ".join(self.information.get(i))+"\n"
                    return_info += info
                else:
                    info = '\033[91m\033[1m'+i+'\033[0m\033[0m'+": "+self.information.get(i)+"\n"
                    return_info += info
            elif re.findall(r"early form",i,re.I|re.M)!=[]:
                info = '\033[1m'+i+'\033[0m'+": "+" ——> ".join(self.information.get(i)+[self.information.get("English Name")                                                         or self.information.get("Name")])+"\n"
                return_info += info
            elif re.findall(r"linguistic classification|proto.*language|language family",i,re.I|re.M) != []:
                info = '\033[1m'+i+'\033[0m'+": "+" ——> ".join(self.information.get(i))+"\n"
                return_info += info
            elif isinstance(self.information.get(i),list):
                info = '\033[1m'+i+'\033[0m'+": "+", ".join(self.information.get(i))+"\n"
                return_info += info
            elif isinstance(self.information.get(i),dict):
                string = "\n".join([key+": "+", ".join(self.information.get(i)[key]) for key in self.information.get(i)])
                info = '\033[1m'+i+'\033[0m'+": "+string+"\n"
                return_info += info
            else:
                info = '\033[1m'+i+'\033[0m'+": "+self.information.get(i)+"\n"
                return_info += info
        #return_info += "\033[1mProto-Language Parents\033[0m: "+str(self.proto["parents"])+"\n"
        return_info += "\033[1mProto-Language Parent\033[0m: "+", ".join(self.proto["sole parent"])+"\n"
        #return_info += "\033[1mProto-Language Lineage\033[0m: "\
        #               +str(self.information.get("Early form corrected"))+"\n"
        #return_info += "\033[1mProto-Language Lineage\033[0m: "\
        #               +str(self.information.get("Early forms corrected"))+"\n"
        #return_info += "\033[1mProto-Language Lineage\033[0m: "\
        #               +str(self.information.get("Reconstructed ancestors"))+"\n"
        return_info += "\033[1mProto-Language Children\033[0m: "+", ".join(self.proto["children"])+"\n"
        return_info += "\033[1mProto-Language Depth\033[0m: "+str(self.proto["depth"])+"\n"
        #return_info += "\033[1mLanguage Classification Parents\033[0m: "+str(self.classification["parents"])+"\n"
        return_info += "\033[1mLanguage Classification Parent\033[0m: "                       +", ".join(self.classification["sole parent"])+"\n"
        #return_info += "\033[1mLanguage Classification Lineage\033[0m: "\
        #               +str(self.information.get("Language family corrected"))+"\n"
        #return_info += "\033[1mLanguage Classification Lineage\033[0m: "\
        #               +str(self.information.get("Linguistic classification corrected"))+"\n"
        return_info += "\033[1mLanguage Classification Children\033[0m: "                       +", ".join(list(self.classification["children"].keys()))+"\n"  
        return_info += "\033[1mLanguage Classification Depth\033[0m: "+str(self.classification["depth"])+"\n"
        return return_info
    
    def get_all_attributes(self):
        return self.__dict__

class Tree:
    def __init__(self):
        self.langList = {}
        self.numLangs = 0
        
    def addLang(self,dictionary):
        self.numLangs = self.numLangs + 1
        newLang = Language(dictionary)
        if dictionary.get("English Name") != None:
            self.langList[re.sub(r"\[\d+\]","",dictionary.get("English Name"))] = newLang
        elif dictionary.get("Name") != None: 
            self.langList[re.sub(r"\[\d+\]","",dictionary.get("Name"))] = newLang
        return newLang
    
    def getLang(self,name):
        if name in self.langList:
            return self.langList[name]
        else:
            return None
        
    def searchLang(self,name):
        lang_list = []
        for lang in self.langList:
            if re.findall(name,lang,re.I|re.M) != []:
                lang_list.append(lang)
        for i in lang_list:
            print(self.langList[i],"\n")  
        
    def __contains__(self,name):
        return name in self.langList
    
    def getLangs(self):
        return self.langList.keys()
    
    def __iter__(self):
        return iter(self.langList.values())
    
def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res        

def create_tree(json,start=None): 
    dictionary = read_from_json(json)
    lang_list = []
    if start != None:
        for i in get_parent_child_pair(json,status="classification",start=start):
            for j in i:
                if j not in lang_list:
                    lang_list.append(j)
    else:
        lang_list = dictionary.keys()
    lang_tree = Tree()
    for i in lang_list:
        try:
            new_lang = lang_tree.addLang(dictionary[i])
        except:
            pass
    for pair in get_parent_child_pair(json,status="classification",start=start):
        if pair[0] in lang_tree.langList.keys() and pair[1] in lang_tree.langList.keys():
            if pair[1] not in lang_tree.langList[pair[0]].classification["children"]:
                lang_tree.langList[pair[0]].classification["children"][pair[1]] = 1
            else:
                lang_tree.langList[pair[0]].classification["children"][pair[1]] += 1
            if pair[0] not in lang_tree.langList[pair[1]].classification["parents"]:
                lang_tree.langList[pair[1]].classification["parents"][pair[0]] = 1
            else:
                lang_tree.langList[pair[1]].classification["parents"][pair[0]] += 1
    for pair in get_parent_child_pair(json,status="proto",start=start):
        if pair[0] in lang_tree.langList.keys() and pair[1] in lang_tree.langList.keys():
            if pair[1] not in lang_tree.langList[pair[0]].proto["children"]:
                lang_tree.langList[pair[0]].proto["children"][pair[1]] = 1
            else:
                lang_tree.langList[pair[0]].proto["children"][pair[1]] += 1
            if pair[0] not in lang_tree.langList[pair[1]].proto["parents"]:
                lang_tree.langList[pair[1]].proto["parents"][pair[0]] = 1
            else:
                lang_tree.langList[pair[1]].proto["parents"][pair[0]] += 1
    for lang in lang_tree.langList:
        class_parents = lang_tree.langList[lang].classification["parents"]
        class_parents_list = []
        if class_parents != {}:
            prepared_list_1 = []
            if len(class_parents) == 1:
                lang_tree.langList[lang].classification["sole parent"] += list(class_parents.keys())
            else:
                for class_parent in class_parents:
                    class_parent_children = list(lang_tree.langList[class_parent].classification["children"].keys())
                    other_class_parents = list(class_parents.keys())
                    n = 0
                    for other_class_parent in other_class_parents:
                        if other_class_parent in class_parent_children:
                            n += 1
                    if n == 0:
                        if class_parent not in prepared_list_1:
                            prepared_list_1 += [class_parent]  
            prepared_list_1 = [*set(prepared_list_1)]
            if len(prepared_list_1)<=1: 
                lang_tree.langList[lang].classification["sole parent"] += prepared_list_1
            else:
                if lang_tree.langList[lang].information.get("Language family corrected"):
                    if len(lang_tree.langList[lang].information.get("Language family corrected")) > 1:
                        for i in prepared_list_1:
                            if i == lang_tree.langList[lang].information.get("Language family corrected")[-2]:
                                if i not in lang_tree.langList[lang].classification["sole parent"]:
                                    lang_tree.langList[lang].classification["sole parent"].append(i)
                if lang_tree.langList[lang].information.get("Linguistic classification corrected"):
                    if len(lang_tree.langList[lang].information.get("Linguistic classification corrected")) > 1:
                        for i in prepared_list_1:
                            if i == lang_tree.langList[lang].information.get("Linguistic classification corrected")[-2]:
                                if i not in lang_tree.langList[lang].classification["sole parent"]:
                                    lang_tree.langList[lang].classification["sole parent"].append(i)
    for lang in lang_tree.langList:
        class_parents = lang_tree.langList[lang].proto["parents"]
        class_parents_list = []
        if class_parents != {}:
            prepared_list_2 = []
            if len(class_parents) == 1:
                lang_tree.langList[lang].proto["sole parent"] += list(class_parents.keys())
            else:
                for class_parent in class_parents:
                    class_parent_children = list(lang_tree.langList[class_parent].proto["children"].keys())
                    other_class_parents = list(class_parents.keys())
                    n = 0
                    for other_class_parent in other_class_parents:
                        if other_class_parent in class_parent_children:
                            n += 1
                    if n == 0:
                        if class_parent not in prepared_list_2:
                            prepared_list_2 += [class_parent]  
            prepared_list_2 = [*set(prepared_list_2)]
            if len(prepared_list_2)<=1:
                lang_tree.langList[lang].proto["sole parent"] += prepared_list_2
            else:
                if lang_tree.langList[lang].information.get("Early forms corrected"):
                    if len(lang_tree.langList[lang].information.get("Early forms corrected")) > 0:
                        for i in prepared_list_2:
                            if i == lang_tree.langList[lang].information.get("Early forms corrected")[-1]:
                                if i not in lang_tree.langList[lang].proto["sole parent"]:
                                    lang_tree.langList[lang].proto["sole parent"].append(i)
                if lang_tree.langList[lang].information.get("Early form corrected"):
                    if len(lang_tree.langList[lang].information.get("Early form corrected")) > 0:
                        for i in prepared_list_2:
                            if i == lang_tree.langList[lang].information.get("Early form corrected")[-1]:
                                if i not in lang_tree.langList[lang].proto["sole parent"]:
                                    lang_tree.langList[lang].proto["sole parent"].append(i) 
                if lang_tree.langList[lang].information.get("Reconstructed ancestors"):
                    if len(lang_tree.langList[lang].information.get("Reconstructed ancestors")) > 0:
                        for i in prepared_list_2:
                            if i == lang_tree.langList[lang].information.get("Reconstructed ancestors")[-1]:
                                if i not in lang_tree.langList[lang].proto["sole parent"]:
                                    lang_tree.langList[lang].proto["sole parent"].append(i) 
    for lang in lang_tree.langList:
        if (len(lang_tree.langList[lang].classification["sole parent"])==0 and             len(lang_tree.langList[lang].classification["parents"])!=0):
            if lang_tree.langList[lang].information.get("Language family corrected"):
                if len(lang_tree.langList[lang].information.get("Language family corrected")) > 1:  
                    lang_tree.langList[lang].classification["sole parent"] +=                    [lang_tree.langList[lang].information.get("Language family corrected")[-2]]
            if lang_tree.langList[lang].information.get("Linguistic classification corrected"):
                if len(lang_tree.langList[lang].information.get("Linguistic classification corrected")) > 1:  
                    lang_tree.langList[lang].classification["sole parent"] +=                    [lang_tree.langList[lang].information.get("Linguistic classification corrected")[-2]]
        if (len(lang_tree.langList[lang].proto["sole parent"])==0 and             len(lang_tree.langList[lang].proto["parents"])!=0):    
            if lang_tree.langList[lang].information.get("Early forms corrected"):
                if len(lang_tree.langList[lang].information.get("Early forms corrected")) > 0:  
                    lang_tree.langList[lang].proto["sole parent"].                    append(lang_tree.langList[lang].information.get("Early forms corrected")[-1])
            if lang_tree.langList[lang].information.get("Early form corrected"):
                if len(lang_tree.langList[lang].information.get("Early form corrected")) > 0:  
                    lang_tree.langList[lang].proto["sole parent"].                    append(lang_tree.langList[lang].information.get("Early form corrected")[-1])
            if lang_tree.langList[lang].information.get("Reconstructed ancestors"):
                if len(lang_tree.langList[lang].information.get("Reconstructed ancestors")) > 0:  
                    lang_tree.langList[lang].proto["sole parent"].                    append(lang_tree.langList[lang].information.get("Reconstructed ancestors")[-1])
    return lang_tree       


# In[ ]:





# In[1]:


import re
class Simplified_Language:
    def __init__(self,name):
        self.name = name
        self.parents = {}
        self.parent = []
        self.children = {}
        self.real_children = []
    
    def __str__(self):
        string = "\n".join(("\033[91m\033[1mLanguage Name\033[0m\033[0m: "+self.name,                            "\033[1mParent\033[0m: "+", ".join(self.parent),                            "\033[1mParents\033[0m: "+str(self.parents),                            "\033[1mChildren\033[0m: "+", ".join(self.real_children)))
        return string
        
class Simplified_Tree():
    def __init__(self):
        self.langList = {}
        self.numLangs = 0
    def addLang(self,name):
        self.numLangs = self.numLangs + 1
        newLang = Simplified_Language(name)
        self.langList[name] = newLang
        return newLang
    def searchLang(self,name):
        list_1 = []
        for lang in self.langList:
            if re.findall(name,lang,re.I|re.M) != []:
                list_1.append(lang)
        for i in list_1:
            print(self.langList[i],"\n")
            
def creat_simple_tree(json,status,start=None,branch=None):
    longTree = create_tree(json,start=start)
    list_of_pair = get_parent_child_pair(json,status,start=start,branch=branch)
    lang_tree = Simplified_Tree()
    for pair in list_of_pair:
        if pair[0] not in lang_tree.langList:
            lang_tree.addLang(pair[0])
            lang_tree.langList[pair[0]].children[pair[1]] = 1
        else:
            if pair[1] not in lang_tree.langList[pair[0]].children:
                lang_tree.langList[pair[0]].children[pair[1]] = 1
            else:
                lang_tree.langList[pair[0]].children[pair[1]] += 1
        if pair[1] not in lang_tree.langList:
            lang_tree.addLang(pair[1])
            lang_tree.langList[pair[1]].parents[pair[0]] = 1
        else:
            if pair[0] not in lang_tree.langList[pair[1]].parents:
                lang_tree.langList[pair[1]].parents[pair[0]] = 1
            else:
                lang_tree.langList[pair[1]].parents[pair[0]] += 1
    for lang in lang_tree.langList:
        parents = lang_tree.langList[lang].parents
        if len(parents) <= 1:
            lang_tree.langList[lang].parent += parents
        else:
            for parent in parents:
                parent_children = list(lang_tree.langList[parent].children.keys())
                other_parents = list(parents.keys())
                n = 0
                for other_parent in other_parents:
                    if other_parent in parent_children:
                        n += 1
                if n == 0:
                    lang_tree.langList[lang].parent += [parent]
    for lang in lang_tree.langList:
        if len(lang_tree.langList[lang].parent) > 1:
            if lang in longTree.langList:
                if status == "classification":
                    lang_tree.langList[lang].parent = longTree.langList[lang].classification["sole parent"]
                if status == "proto":
                    lang_tree.langList[lang].parent = longTree.langList[lang].proto["sole parent"]
    for lang in lang_tree.langList:
        if len(lang_tree.langList[lang].parent) > 1:
            lang_tree.langList[lang].parent = [lang_tree.langList[lang].parent[0]]
    for lang in lang_tree.langList:
        children = lang_tree.langList[lang].children
        for child in children:
            child_parent = list(lang_tree.langList[child].parents.keys())
            child_parent_parent = []
            for x in list(lang_tree.langList[child].parents.keys()):
                child_parent_parent += list(lang_tree.langList[x].parents.keys())
            other_children = list(children.keys())
            n = 0
            for other_child in other_children:
                if other_child in child_parent or other_child in child_parent_parent:
                    n += 1
            if n == 0:
                lang_tree.langList[lang].real_children += [child]
    for lang in lang_tree.langList:
        if len(lang_tree.langList[lang].parent)==0 and len(lang_tree.langList[lang].parents)>0:
            lang_tree.langList[lang].parent = [list(lang_tree.langList[lang].parents.keys())[0]]
    return lang_tree


# In[8]:


langTree = create_tree("Indo-European language data.json",start=None)


# In[9]:


simplelangTree = creat_simple_tree("Indo-European language data.json",status="classification")


# In[10]:


simplelangTree.searchLang("Russian")


# In[11]:


langTree.searchLang("Russian")


# In[ ]:




