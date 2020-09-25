import cv2
import numpy as np

def Morph(image_name):
    print("image_name", image_name)
    global image
    image = image_name
    img = cv2.imread(image)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img1 = img.copy()
    # Structuring Element
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    thin = np.zeros(img.shape, dtype='uint8')
    # Erosion
    erode = cv2.erode(img1, kernel)
    # Opening on eroded image
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)
    # output_image = cv2.morphologyEx(erode, cv2.MORPH_HITMISS, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)
    gradient1 = dilation - erosion
    kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_1)
    # Apply the black hat transform
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_1)
    cv2.waitKey(0)
    filename = "gradient.jpg"
    cv2.imwrite(filename, gradient1)
    filename = "tophat.jpg"
    cv2.imwrite(filename, tophat)
    filename = "blackhat.jpg"
    cv2.imwrite(filename, blackhat)
def Corner_Edge(image_name,num):
    global image
    image = image_name
    img = cv2.imread(image)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img1 = img.copy()
        # Structuring Element
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    thin = np.zeros(img.shape, dtype='uint8')
    # Erosion
    erode = cv2.erode(img1, kernel)
    # Opening on eroded image
    opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)
    # output_image = cv2.morphologyEx(erode, cv2.MORPH_HITMISS, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    erosion = cv2.erode(img, kernel, iterations=1)
    dilation = cv2.dilate(img, kernel, iterations=1)
    gradient1 = dilation - erosion
    kernel_1 = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 25))
    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel_1)
    # Apply the black hat transform
    blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel_1)
    cv2.waitKey(0)
    filename = "gradient.jpg"
    cv2.imwrite(filename,gradient1)
    filename = "tophat.jpg"
    cv2.imwrite(filename, tophat)
    filename = "blackhat.jpg"
    cv2.imwrite(filename, blackhat)
    list_1 = [opening,closing,erosion,dilation,gradient1,tophat,blackhat]
    harris_1 =[]
    for i in range(0,len(list_1)):
        img = list_1[i]
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
        img[dst > 0.1 * dst.max()] = [0, 0, 255]
        filename = 'corner'+'_'+str(i)+".jpg"
        cv2.imwrite(filename,img)
        for i in range(0, len(corners)):
            for j in range(0,len(corners[i])):
                list_2.append(round(corners[i][j]))
            harris.append(list_2)
            list_2 = []
        #print(harris)
        harris_1.append(harris)
    #print(harris_1)
    #print(harris_1)
    if(num=="1"):
        gradient_edge = cv2.Canny(gradient1,100,200)
        filename = 'GM_gradient_edge' + ".jpg"
        cv2.imwrite(filename, gradient_edge)

        img_5 = cv2.medianBlur(gradient1, 5)
        ret, gradient_edge = cv2.threshold(img_5, 127, 255, cv2.THRESH_BINARY)
        filename = 'TH_gradient_edge' + ".jpg"
        img = cv2.cvtColor(gradient_edge, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(filename, img)

        gray_5 = cv2.cvtColor(gradient1, cv2.COLOR_BGR2GRAY)
        ret, gradient_edge = cv2.threshold(gray_5, 0, 255,
                                           cv2.THRESH_BINARY_INV +
                                           cv2.THRESH_OTSU)
        filename = 'WS_gradient_edge' + ".jpg"
        cv2.imwrite(filename, gradient_edge)



    elif(num=="2"):
        tophat_edge = cv2.Canny(tophat, 100, 200)
        filename = 'GM_tophat_edge' + ".jpg"
        cv2.imwrite(filename, tophat_edge)

        img_6 = cv2.medianBlur(tophat, 5)
        ret, tophat_edge = cv2.threshold(img_6, 127, 255, cv2.THRESH_BINARY)
        filename = 'TH_tophat_edge' + ".jpg"
        img = cv2.cvtColor(tophat_edge, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(filename, img)


        gray_6 = cv2.cvtColor(tophat, cv2.COLOR_BGR2GRAY)
        ret, tophat_edge = cv2.threshold(gray_6, 0, 255,
                                         cv2.THRESH_BINARY_INV +
                                         cv2.THRESH_OTSU)
        filename = 'WS_tophat_edge' + ".jpg"
        cv2.imwrite(filename, tophat_edge)

    if(num=="3"):
        blackhat_edge = cv2.Canny(blackhat, 100, 200)
        filename = 'GM_blackhat_edge' + ".jpg"
        cv2.imwrite(filename, blackhat_edge)

        img_7 = cv2.medianBlur(blackhat, 5)
        ret, blackhat_edge = cv2.threshold(img_7, 127, 255, cv2.THRESH_BINARY)
        filename = 'TH_blackhat_edge' + ".jpg"
        img = cv2.cvtColor(blackhat_edge, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(filename, img)

        gray_7 = cv2.cvtColor(blackhat, cv2.COLOR_BGR2GRAY)
        ret, blackhat_edge = cv2.threshold(gray_7, 0, 255,
                                           cv2.THRESH_BINARY_INV +
                                           cv2.THRESH_OTSU)
        filename = 'WS_blackhat_edge' + ".jpg"
        cv2.imwrite(filename, blackhat_edge)


