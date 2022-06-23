import cv2
import numpy as np
import types
from PIL import Image 
import scipy.misc
from colorsys import hsv_to_rgb

image = cv2.imread('nature.jpg')
#stark=cv2.imread('mark5.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)


cv2.waitKey(0)
cv2.destroyAllWindows()
''''''
def gk(s, k):
    '''this function takes the strings and password and generates a key of length
    equal to the string'''
    k = list(k) #list key
    #if length of password and string is same we return the password
    if len(s) == len(k):
        return (k)
    else: #otherise we need to use a loop and generate a key
        for i in range(len(s) -
                       len(k)):
            k.append(k[i % len(k)])
    return ("".join(k))


def ciphertext(s, k):
    '''this function generates the ciphertext'''
    cipher_text = [] #empty ciphertext list
    #loop for traversing through the string
    for i in range(len(s)):
        #we add the numerical values of string and key and takes its remainder when divided by 26 and then use that to
        #get the ciphertext alphabet
        xa = (ord(s[i]) +
             ord(k[i])) % 26
        xa =xa+ ord('A')
        cipher_text.append(chr(xa))
    return ("".join(cipher_text))

def vigenere_encrypt(s,password):
    '''Encrypt the string s based on the password the vigenere cipher way and
    return the resulting string'''
    string_in = s #input string 
    keyword_in = password #input password
    string=string_in.upper()
    keyword=keyword_in.upper()
    key = gk(string, keyword)
    cipher_text = ciphertext(string, key)
    #returning the ciphertext
    return cipher_text

######################################################
def origtext(cipher_text, k):
    '''this function uses the key and ciphertext and gets the original text that was encrypted'''
    otext = []
    ##loop for traversing through the cipher_text
    for i in range(len(cipher_text)):
        ##calculating the original text alphabet
        xa = (ord(cipher_text[i]) - ord(k[i]) + 26) % 26
        xa =xa + ord('A')
        otext.append(chr(xa))
    return ("".join(otext))

def vigenere_decrypt(s,password):
    '''Decrypts the string s based on the password the vigenere cipher way and
    returns the resulting string'''
    cipher_text_in = s
    keyword_in = password
    cipher_text=cipher_text_in.upper()
    keyword=keyword_in.upper()
    key = gk(cipher_text, keyword)
    #returning original text
    return origtext(cipher_text,key)

def binary_converter(message):  
    if type(message) == str:  
        return ''.join([format(ord(i), "08b") for i in message])
    if type(message) == bytes or type(message) == np.ndarray:  
        return [format(i, "08b") for i in message] 
    if type(message) == int or type(message) == np.uint8:  
        return format(message, "08b")
     
#print(binary_converter("Hello"))
#for values in image:
 #   print(values)
#print(image.shape)
#print(len(gray[0]))
final=[]
#finalimage=[]


#def hd(retina, pro):  
    
pro='thisisimgsteganography'
    #noob = retina.shape[0] * retina.shape[1]*3// 8  
    #print(noob)  
    # checking whether the number of bytes for encoding is less  
    # than the maximum bytes in the image  
    #if len(pro) > noob:  
     #   raise ValueError("RUNTIME TERROR")  
pro =pro + 'zzzzz'       # we can utilize any string as the delimiter
cake=vigenere_encrypt(pro,"pan")
mendis=vigenere_encrypt('zzzzz','pan')
di = 0  #index=0
    # converting the input data to binary format using the msg_to_bin() function  
bsm = binary_converter(cake)
    
  
    # finding the length of data that requires to be hidden  
dls = len(bsm)  
for v in image:  
    ma=[]
        
    for pix in v:  
    
            # converting RGB values to binary format 
         
        if di<dls:
            r, g, b = binary_converter(pix)
              
            # modifying the LSB only if there is data remaining to store  
            if di < dls:  
                # hiding the data into LSB of Red pixel  
                pix[0] = int(r[:-1]+bsm[di],2)
                di += 1  
                
            if di < dls:  
                # hiding the data into LSB of Green pixel  
                pix[1] = int(g[:-1]+bsm[di],2)
                
                di += 1  
            if di < dls:  
                # hiding the data into LSB of Blue pixel  
                pix[2] = int(b[:-1]+bsm[di],2) 
                di += 1  
            ma.append([pix[0],pix[1],pix[2]])
            #finalimage.append(pix[0])
            #finalimage.append(pix[1])
            #finalimage.append(pix[2])
        else:
            ma.append([pix[0],pix[1],pix[2]])
            #finalimage.append(pix[0])
            #finalimage.append(pix[1])
            #finalimage.append(pix[2])
            
        #if di>=dls:
         #   ma.append([pix[0],pix[1],pix[2]])
            
        
        
            # if data is encoded, break out the loop  
            #if di == dls:  
             #   break  
    final.append(ma)
    
# defining function to encode data into Image  
def encodeText():  
    img_name = input("Enter image name (with extension): ")  
 #reading the input image using OpenCV-Python  
    img = cv2.imread('chill.jpg') 
 
 #printing the details of the image  
    print( img.shape) # checking the image shape to calculate the number of bytes in it   
 #resizing the image as per the need  
    #resizedImg = cv2.resize(image,(598,600))  
    # displaying the image  
    #cv2.imshow("ori",resizedImg)  
    data = input("Enter data to be encoded: ")  
    if (len(data) == 0):  
        raise ValueError('Data is Empty')  
      
    file_name = input("Enter the name of the new encoded image (with extension): ")  
     #calling the hide_data() function to hide the secret message into the selected image  
    #encodedImage = hd(image, data)  
    #cv2.imwrite(file_name, encodedImage)

############################################DECODER$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def showdata(img):  
    bindata = ""  
    for val in img:  
        for pix in val:  
            #print(pixels)
            # converting the Red, Green, Blue values into binary format  
            r, g, b = pix
            rb=str(binary_converter(r))
            gb=str(binary_converter(g))
            bb=str(binary_converter(b))
            
            # data extraction from the LSB of Red pixel  
            bindata =bindata+ rb[-1]  
            # data extraction from the LSB of Green pixel  
            bindata =bindata+ gb[-1]  
            # data extraction from the LSB of Blue pixel  
            bindata =bindata+ bb[-1]  
            
    # splitting by 8-bits  
    allbytes = [int(bindata[i: i + 8],2) for i in range(0, len(bindata), 8)]  
     #converting from bits to characters  
    decodedData = ""  
    for bytes in allbytes:  
        decodedData += chr(bytes)  
         #checking if we have reached the delimiter which is "#####" 
    #teak=vigenere_decrypt(decodedData,"pancake") 
    #teak=teak.lower()
    sauce=""
    
    for i in range(len(decodedData)):
        sauce=sauce+decodedData[i]
        if sauce[-5:] == mendis:  #delimeter
            
            break
    tennis=sauce[:-5]  
    colin=vigenere_decrypt(tennis,"pan")
    colin=colin.lower()
    for i in range(len(colin)):
        if colin[i:i+5] =='zzzzz':
            return colin[:i]
            
     #print(decodedData)  
    # removing the delimiter to display the actual hidden message  
    
    #return allBytes
    #return len(bin_data),bin_data

#print(show_data(encodedImage))



# defining the function to decode the data in the image  
def decoder():  
    # reading the image containing the hidden image  
    image_name=input("image name")
    imge = cv2.imread(image_name)  # reading the image using the imread() function  
  
    #print("The Steganographic image is as follow: ")  
    #resizedImg = cv2.resize(img, (500, 500))    # resizing the actual image as per the needs  
    #cv2.imshow(resizedImg)  # displaying the Steganographic image  
  
    text = showdata(imge)  
    print(text)  


#print((binary_converter("hello#####")))
#decodeText()
#print(showdata([[[1,110,11],[1,11,1],[1,1,11]],[[11,1,1],[1,11,1],[1,1,1]],[[11,11,1],[1,11,1],[1,1,1]]]))
#print(showdata(hd('chill.jpg','hello')))
'''k=binary_converter('hello#####')
d=0
li=[]
for a in stark:
    lm=[]
    for la in a:
        
        r, g, b = binary_converter(la)
        if d!=80:
            if d<80:
                r=int(r[:-1]+k[d],2)
                d+=1
            if d<80:
                g=int(g[:-1]+k[d],2)
                d+=1
            if d<80:
                b=int(b[:-1]+k[d],2)
                d+=1
        lm.append([r,g,b])
        if d==80:
            break
    if d==80:
        li.append(lm)
        break
print(showdata(li))'''

#print(len(stark[0]))

#print(len(final))
#print(len(image),len(image[0]))

'''de=0
print("")
for a in image:
    for b in a:
        if de<=8:
            print(b)
            de+=1'''
#encodeText()
#t=binary_converter("hi")
#print(t,t[1])

'''finalimage1=[]
for i in image:
    for j in i:
        finalimage1.append(j[0])
        finalimage1.append(j[1])
        finalimage1.append(j[2])
#print(len(finalimage))
#print(final[0:10])
#print(finalimage[0:10])'''
#print(len(final),len(final[0]))
'''colors = bytes(finalimage)
img = Image.frombytes('RGB',(806,1280),colors)
img.show()
img.save('new123.jpg')'''
#resizedImg = cv2.resize(image,(598,600))
#print(image.shape)
################################ show image #########################################
#function to show image
'''for i in final:
    for j in i:
        j.reverse()
w, h = image.shape[1],image.shape[0]
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:h, 0:w] = final 
img = Image.fromarray(data, 'RGB')
img.save('my.jpg')
img.show()'''

################################### show hidden message ###############################
#to show hidden message
#print(showdata(final))