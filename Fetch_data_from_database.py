import sqlite3
import math
from scipy.spatial import distance

# for i in range(0,7):
def Morphological(i,j,filename):
    conn = sqlite3.connect('Modified_pixel_content.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GM_TH_WT_CCED_CORNER_EDGES_VALUES")
    rows = cursor.fetchall()
    user_name = filename[-11:]
    euclidean_distance_values = []
    canberra_distance_values = []
    jensenshannon_distance_values = []
    chebyshev_distance_values = []
    jaccard_distance_values = []
    if(j == 0):
        print("GMCCED")
    elif(j == 1):
        print("THCCED")
    elif(j==2):
        print("WSCCED")
    x1 = []
    u = i
    # print(u)
    for row in rows:
        if (row[0] == user_name):
            string = row[u]
            mono = []
            num_string = ""
            lists = []
            for i in range(1, len(string)):
                if (string[i] == '[' and string[i + 1] == ']'):
                    m = []
                    lists.append(m)
                if (string[i] == ',' or string[i] == ']'):
                    if (num_string != ""):
                        mono.append(int(num_string))
                        num_string = ""
                        if (string[i] == ']'):
                            lists.append(mono)
                            mono = []
                    continue
                elif (string[i] == ' ' or string[i] == '['):
                    continue
                elif (int(string[i]) >= int(0) and int(string[i]) <= int(9)):
                    num_string += string[i]
    x1 = lists[j]
    if (x1 == []):
        return 0
    else:
        # print("x1",x1)
        image_names = []
        for row in rows:
            image_names.append(row[0])
        count = 0
        for row in rows:
            # count = count+1
            string_1 = row[u]
            # print(string_1)
            y1 = []
            mono = []
            num_string = ""
            lists = []
            for i in range(1, len(string_1)):
                if (string_1[i] == '[' and string_1[i + 1] == ']'):
                    m = []
                    lists.append(m)
                if (string_1[i] == ',' or string_1[i] == ']'):
                    if (num_string != ""):
                        mono.append(int(num_string))
                        num_string = ""
                        if (string_1[i] == ']'):
                            lists.append(mono)
                            mono = []
                    continue
                elif (string_1[i] == ' ' or string_1[i] == '['):
                    continue
                elif (int(string_1[i]) >= int(0) and int(string_1[i]) <= int(9)):
                    num_string += string_1[i]
            y1 = lists[j]
            if (y1 == []):
                continue
            else:
                # print("y1", y1)
                count = count + 1
                if (len(x1) > len(y1)):
                    n = len(x1) - len(y1)
                    for i in range(0, n):
                        y1.append(0)
                elif (len(x1) < len(y1)):
                    n = len(y1) - len(x1)
                    for i in range(0, n):
                        x1.append(0)
                euclidean_distance = distance.euclidean(x1, y1)
                euclidean_distance_values.append(euclidean_distance)
                canberra_distance = distance.canberra(x1, y1)
                canberra_distance_values.append(canberra_distance)
                jensenshannon_distance = distance.jensenshannon(x1, y1)
                jensenshannon_distance_values.append(jensenshannon_distance)
                chebyshev_distance = distance.chebyshev(x1, y1)
                chebyshev_distance_values.append(chebyshev_distance)
                jaccard_distance = distance.jaccard(x1, y1)
                jaccard_distance_values.append(jaccard_distance)

    merger = euclidean_distance_values
    sorted_distance_values = sorted(euclidean_distance_values)
    euclidean_sort_distance = []
    for i in range(0, 30):
        var = merger.index(sorted_distance_values[i])
        merger[var] = 100000
        euclidean_sort_distance.append(image_names[var])
    if (euclidean_sort_distance.count(user_name) == 0):
        euclidean_sort_distance.insert(0, user_name)
        #print(euclidean_sort_distance)
    elif (euclidean_sort_distance[0] != user_name):
        n = euclidean_sort_distance.index(user_name)
        pos_image = euclidean_sort_distance[0]
        euclidean_sort_distance[0] = user_name
        euclidean_sort_distance[n] = pos_image
        # euclidean_sort_distance.insert(n,)
    '''print(len(euclidean_sort_distance))
    print("euclidean_list", euclidean_sort_distance)'''

    # canberra distance
    merger = canberra_distance_values
    sorted_distance_values = sorted(canberra_distance_values)
    # print(sorted_distance_values)
    canberra_sort_distance = []
    for i in range(0, 30):
        var = merger.index(sorted_distance_values[i])
        merger[var] = 100000
        canberra_sort_distance.append(image_names[var])
    if (canberra_sort_distance.count(user_name) == 0):
        canberra_sort_distance.insert(0, user_name)
    elif (canberra_sort_distance[0] != user_name):
        n = canberra_sort_distance.index(user_name)
        pos_image = canberra_sort_distance[0]
        canberra_sort_distance[0] = user_name
        canberra_sort_distance[n] = pos_image

    merger = jensenshannon_distance_values
    sorted_distance_values = sorted(jensenshannon_distance_values)
    # print(sorted_distance_values)
    jensenshannon_sort_distance = []
    for i in range(0, 30):
        var = merger.index(sorted_distance_values[i])
        merger[var] = 100000
        jensenshannon_sort_distance.append(image_names[var])
    if (jensenshannon_sort_distance.count(user_name) == 0):
        jensenshannon_sort_distance.insert(0, user_name)
    elif (jensenshannon_sort_distance[0] != user_name):
        n = jensenshannon_sort_distance.index(user_name)
        pos_image = jensenshannon_sort_distance[0]
        jensenshannon_sort_distance[0] = user_name
        jensenshannon_sort_distance[n] = pos_image

    # Chebyshev distacnce
    # print("chybyshev")

    merger = chebyshev_distance_values
    sorted_distance_values = sorted(chebyshev_distance_values)
    # print(sorted_distance_values)
    chebyshev_sort_distance = []
    for i in range(0, 30):
        var = merger.index(sorted_distance_values[i])
        merger[var] = 100000
        chebyshev_sort_distance.append(image_names[var])
    if (chebyshev_sort_distance.count(user_name) == 0):
        chebyshev_sort_distance.insert(0, user_name)
    elif (chebyshev_sort_distance[0] != user_name):
        n = chebyshev_sort_distance.index(user_name)
        pos_image = chebyshev_sort_distance[0]
        chebyshev_sort_distance[0] = user_name
        chebyshev_sort_distance[n] = pos_image

    merger = jaccard_distance_values
    sorted_distance_values = sorted(jaccard_distance_values)
    # print(sorted_distance_values)
    jaccard_sort_distance = []
    for i in range(0, 30):
        var = merger.index(sorted_distance_values[i])
        merger[var] = 100000
        jaccard_sort_distance.append(image_names[var])
    if (jaccard_sort_distance.count(user_name) == 0):
        jaccard_sort_distance.insert(0, user_name)
    elif (jaccard_sort_distance[0] != user_name):
        n = jaccard_sort_distance.index(user_name)
        pos_image = jaccard_sort_distance[0]
        jaccard_sort_distance[0] = user_name
        jaccard_sort_distance[n] = pos_image
    sort_distance = []
    sort_distance.append(euclidean_sort_distance)
    sort_distance.append(canberra_sort_distance)
    sort_distance.append(jensenshannon_sort_distance)
    sort_distance.append(chebyshev_sort_distance)
    sort_distance.append(jaccard_sort_distance)
    #print(len(sort_distance))
    
    distances = ["euclidean","canberra","jensenshanoon","chebyshev","jaccard"]
    for i in range(0, len(sort_distance)):
        im = sort_distance[i]
        count = 0
        for j in range(0, len(im)):
            n = im[j]
            if (n[0:2] == filename[-11:-9]):
                count = count + 1
        #print(distances[i]," : ",count)
    return sort_distance

#Morphological(2,0,"11_1101.jpg")