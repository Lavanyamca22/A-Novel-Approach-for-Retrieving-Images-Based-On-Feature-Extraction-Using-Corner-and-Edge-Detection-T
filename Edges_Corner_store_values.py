import cv2
import numpy as np
import sqlite3
import os
def Gradient(image_name):
    global gradient_values
    global image
    gradient_values = []
    image = image_name
    img = cv2.imread(image)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img1 = img.copy()
    # Structuring Element
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    # Erosion
    erode = cv2.erode(img1, kernel)
    # Opening on eroded image
    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)
    gradient1 = dilation - erosion

    img = gradient1
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image',gray)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 5, 3, 0.04)
    ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    harris = []
    list_2 = []
    for i in range(0, len(corners)):
        for j in range(0, len(corners[i])):
            list_2.append(round(corners[i][j]))
        harris.append(list_2)
        list_2 = []

    #Gradient magnitude
    gradient1_edge = cv2.Canny(gradient1, 100, 200)
    gradient_edge_values = []
    for i in range(0, len(gradient1_edge)):
        for j in range(0, len(gradient1_edge[i])):
            if (gradient1_edge[i][j] == 255):
                gradient_edge_values.append([i, j])
    m = harris
    ce_gm_gradient = []
    for i in range(0,len(m)):
        for j in range(0,len(gradient_edge_values)):
            if(m[i]==gradient_edge_values[j]):
                #print(m[i],gradient_edge_values[j])
                n = gradient_edge_values[i]
                ce_gm_gradient.append(sum(img[n[0]][n[1]]))

    #Threshold
    ce_th_gradient = []
    img_1 = cv2.medianBlur(gradient1, 5)
    ret, gradient1_edge = cv2.threshold(img_1, 127, 255, cv2.THRESH_BINARY)
    gradient_edge_values = []
    for i in range(0, len(gradient1_edge)):
        for j in range(0, len(gradient1_edge[i])):
            if (sum(gradient1_edge[i][j]) == 0):
                gradient_edge_values.append([i, j])
    # print(m)
    for i in range(0, len(m)):
        for j in range(0, len(gradient_edge_values)):
            if (m[i] == gradient_edge_values[j]):
                # print(m[i],gradient_edge_values[j])
                n = gradient_edge_values[i]
                ce_th_gradient.append(sum(img[n[0]][n[1]]))

    #Watershed
    ce_ws_gradient = []
    ws_img = cv2.cvtColor(gradient1, cv2.COLOR_BGR2GRAY)
    ret, gradient1_edge = cv2.threshold(ws_img, 0, 255,
                                        cv2.THRESH_BINARY_INV +
                                        cv2.THRESH_OTSU)
    gradient_edge_values = []
    for i in range(0, len(gradient1_edge)):
        for j in range(0, len(gradient1_edge[i])):
            if (gradient1_edge[i][j] == 0):
                gradient_edge_values.append([i, j])
    for i in range(0,len(m)):
        for j in range(0,len(gradient_edge_values)):
            if(m[i]==gradient_edge_values[j]):
                #print(m[i],gradient_edge_values[j])
                n = gradient_edge_values[i]
                ce_ws_gradient.append(sum(img[n[0]][n[1]]))
    gradient_values.append(ce_gm_gradient)
    gradient_values.append(ce_th_gradient)
    gradient_values.append(ce_ws_gradient)

def Tophat(image_name):
    global tophat_values
    tophat_values = []
    image = image_name
    img = cv2.imread(image)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img1 = img.copy()
    kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_1)

    img = tophat
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image',gray)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 5, 3, 0.04)
    ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    harris = []
    list_2 = []
    for i in range(0, len(corners)):
        for j in range(0, len(corners[i])):
            list_2.append(round(corners[i][j]))
        harris.append(list_2)
        list_2 = []

    # Gradient magnitude
    tophat1_edge = cv2.Canny(tophat, 100, 200)
    tophat_edge_values = []
    for i in range(0, len(tophat1_edge)):
        for j in range(0, len(tophat1_edge[i])):
            if (tophat1_edge[i][j] == 255):
                tophat_edge_values.append([i, j])
    m = harris
    ce_gm_tophat = []
    for i in range(0, len(m)):
        for j in range(0, len(tophat_edge_values)):
            if (m[i] == tophat_edge_values[j]):
                # print(m[i],tophat_edge_values[j])
                n = tophat_edge_values[i]
                ce_gm_tophat.append(sum(img[n[0]][n[1]]))

    # Threshold
    ce_th_tophat = []
    img_1 = cv2.medianBlur(tophat, 5)
    ret, tophat1_edge = cv2.threshold(img_1, 127, 255, cv2.THRESH_BINARY)
    tophat_edge_values = []
    for i in range(0, len(tophat1_edge)):
        for j in range(0, len(tophat1_edge[i])):
            if (sum(tophat1_edge[i][j]) == 0):
                tophat_edge_values.append([i, j])
    # print(m)
    for i in range(0, len(m)):
        for j in range(0, len(tophat_edge_values)):
            if (m[i] == tophat_edge_values[j]):
                # print(m[i],tophat_edge_values[j])
                n = tophat_edge_values[i]
                ce_th_tophat.append(sum(img[n[0]][n[1]]))

    # Watershed
    ce_ws_tophat = []
    ws_img = cv2.cvtColor(tophat, cv2.COLOR_BGR2GRAY)
    ret, tophat1_edge = cv2.threshold(ws_img, 0, 255,
                                        cv2.THRESH_BINARY_INV +
                                        cv2.THRESH_OTSU)
    tophat_edge_values = []
    for i in range(0, len(tophat1_edge)):
        for j in range(0, len(tophat1_edge[i])):
            if (tophat1_edge[i][j] == 0):
                tophat_edge_values.append([i, j])
    for i in range(0, len(m)):
        for j in range(0, len(tophat_edge_values)):
            if (m[i] == tophat_edge_values[j]):
                # print(m[i],tophat_edge_values[j])
                n = tophat_edge_values[i]
                ce_ws_tophat.append(sum(img[n[0]][n[1]]))
    tophat_values.append(ce_gm_tophat)
    tophat_values.append(ce_th_tophat)
    tophat_values.append(ce_ws_tophat)

def Blackhat(image_name):
    global blackhat_values
    blackhat_values = []
    image = image_name
    img = cv2.imread(image)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img1 = img.copy()
    kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_1)

    img = blackhat
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('image',gray)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, 5, 3, 0.04)
    ret, dst = cv2.threshold(dst, 0.1 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    harris = []
    list_2 = []
    for i in range(0, len(corners)):
        for j in range(0, len(corners[i])):
            list_2.append(round(corners[i][j]))
        harris.append(list_2)
        list_2 = []

    # Gradient magnitude
    blackhat1_edge = cv2.Canny(blackhat, 100, 200)
    blackhat_edge_values = []
    for i in range(0, len(blackhat1_edge)):
        for j in range(0, len(blackhat1_edge[i])):
            if (blackhat1_edge[i][j] == 255):
                blackhat_edge_values.append([i, j])
    m = harris
    ce_gm_blackhat = []
    for i in range(0, len(m)):
        for j in range(0, len(blackhat_edge_values)):
            if (m[i] == blackhat_edge_values[j]):
                # print(m[i],blackhat_edge_values[j])
                n = blackhat_edge_values[i]
                ce_gm_blackhat.append(sum(img[n[0]][n[1]]))

    # Threshold
    ce_th_blackhat = []
    img_1 = cv2.medianBlur(blackhat, 5)
    ret, blackhat1_edge = cv2.threshold(img_1, 127, 255, cv2.THRESH_BINARY)
    blackhat_edge_values = []
    for i in range(0, len(blackhat1_edge)):
        for j in range(0, len(blackhat1_edge[i])):
            if (sum(blackhat1_edge[i][j]) == 0):
                blackhat_edge_values.append([i, j])
    # print(m)
    for i in range(0, len(m)):
        for j in range(0, len(blackhat_edge_values)):
            if (m[i] == blackhat_edge_values[j]):
                # print(m[i],blackhat_edge_values[j])
                n = blackhat_edge_values[i]
                ce_th_blackhat.append(sum(img[n[0]][n[1]]))

    # Watershed
    ce_ws_blackhat = []
    ws_img = cv2.cvtColor(blackhat, cv2.COLOR_BGR2GRAY)
    ret, blackhat1_edge = cv2.threshold(ws_img, 0, 255,
                                      cv2.THRESH_BINARY_INV +
                                      cv2.THRESH_OTSU)
    blackhat_edge_values = []
    for i in range(0, len(blackhat1_edge)):
        for j in range(0, len(blackhat1_edge[i])):
            if (blackhat1_edge[i][j] == 0):
                blackhat_edge_values.append([i, j])
    for i in range(0, len(m)):
        for j in range(0, len(blackhat_edge_values)):
            if (m[i] == blackhat_edge_values[j]):
                # print(m[i],blackhat_edge_values[j])
                n = blackhat_edge_values[i]
                ce_ws_blackhat.append(sum(img[n[0]][n[1]]))
    blackhat_values.append(ce_gm_blackhat)
    blackhat_values.append(ce_th_blackhat)
    blackhat_values.append(ce_ws_blackhat)
    Store_values()

def Store_values():
    db = sqlite3.connect('Modified_pixel_content.db')
    Image = image
    print(Image)
    gd_val = str(gradient_values)
    th_val = str(tophat_values)
    bh_val = str(blackhat_values)
    cursor = db.cursor()
    cursor.execute('insert into GM_TH_WT_CCED_CORNER_EDGES_VALUES'
                   '(IMAGE_NAME,Gradient,Tophat,Blackhat)'
                   'values(:IMAGE_NAME,:Gradient,:Tophat,:Blackhat)',
                   {'IMAGE_NAME': Image, 'Gradient': gd_val, 'Tophat': th_val,
                    'Blackhat': bh_val})
    db.commit()

path = 'C:\\Users\\user\\PycharmProjects\\Modified_Project\\Image_set'

files = os.listdir(path)
for name in files:
    Gradient(name)
    Tophat(name)
    Blackhat(name)
