def proportion(csv_path,x):
    import csv
    import matplotlib.pyplot as plt
    
    csvfile = csv.reader(open(csv_path,'r'))
    
    column = []
    
    for line in csvfile:
        column.append(line[x])
    
    elements = set(column)
    ele_list = []
    
    for ele in elements:
        ele_list.append(ele)
    length = len(ele_list)
    sort_list = []
    
    for eachone in range(1,length+1):
        sort_list.append([])
    
    for obj in column:
        for each in range(1,length+1):
            if obj == ele_list[each-1]:
                sort_list[each-1].append(obj)
                
    size = []
    
    for entities in sort_list:
        size.append(len(entities))
        
    la_list = []
    for one in range(1,length+1):
        lab = str(one)
        la_list.append(lab)
    
    la = tuple(la_list)
    
    col = ['black']
    for single in range(2,length+1):
        if single%2 == 1:
            col.append('red')
        col.append('yellow')
    
    chart = plt.pie(x=size,labels=la,colors=col)
    plt.axis('equal')
    return plt.show(chart)

def get_element_list(csv_folder,x):
    import csv
    
    csvfile = csv.reader(open(csv_folder,'r'))
    
    column = []
    
    for line in csvfile:
        column.append(line[x])
    
    elements = set(column)
    ele_list = []
    
    for ele in elements:
        ele_list.append(ele)
    return print(ele_list)


proportion('C:/userFeature.csv',20)
get_element_list('C:/userFeature.csv',20)
proportion('C:/userFeature.csv',21)
get_element_list('C:/userFeature.csv',21)
proportion('C:/userFeature.csv',22)
get_element_list('C:/userFeature.csv',22)
proportion('C:/userFeature.csv',23)
get_element_list('C:/userFeature.csv',23)