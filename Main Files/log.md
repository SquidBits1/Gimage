# My Log

## 2023

### April 26 
Started implementing a pixel sorting algorithm, using numpy to quickly do matrix calculations.
The first thing I did was make a function that takes a pixel value (rgb) in and outputs the intensity. (Initially my own 
arbitrary function of just summing the three rgb values)

Then I sorted an array of pixels using this intensity functions with both rows and columns.

### April 27 
My implementation above uses a for loop which is very inefficient, but using only matrix
manipulation would be much more efficient. I started trying to make it work without for loops,
failed so far.

### May 4 
The original pixel sorting algorithm was done by an artist called Kim Asendorf. Today I tried using his method,
which involves doing thresholding the original image to create a binary image and categorise
where the darkest part of the image are. It then only sorts the dark parts of the image. I haven't got it working yet.

I also fixed my function which outputs a pixels intensity by outputting the luminance of the pixel. This is a 
standard value which is calculated from an rbg pixel with the formula
#### (0.2126*R + 0.7152*G + 0.0722*B)

### May 9 

I redid the file system so that each different main task is in a different file.
I also started creating a new editing method by implementing some thresholding. There are multiple different modes you 
can do. 


## Thresholding
### Sources
[Wikipedia Thresholding](https://en.wikipedia.org/wiki/Thresholding_(image_processing))  
[A Brief Study of Image Thresholding Algorithms](https://www.analyticsvidhya.com/blog/2022/07/a-brief-study-of-image-thresholding-algorithms/#:~:text=Image%20thresholding%20is%20a%20type,is%20done%20in%20grayscale%20images.)

### Summary
Thresholding is when you take a greyscale image (one channel) and apply a function to each of the pixels according to an
input threshold. For example, you could make any pixels with a value higher than the threshold black and the pixels with
a value smaller than the threshold white. This turns it into a binary image which looks like this:

![Binary Image](Thresholding/threshold.png)

Check [A Brief Study of Image Thresholding Algorithms](https://www.analyticsvidhya.com/blog/2022/07/a-brief-study-of-image-thresholding-algorithms/#:~:text=Image%20thresholding%20is%20a%20type,is%20done%20in%20grayscale%20images.)
for algorithms used. 

### Otsu's Method

This is a method that attempts to find an optimal thresholding value for an image. It calculates the threshold which
makes the largest variance in intensity between foreground (the would-be white pixels) and background
(the would-be light pixels). [Some nice source code for Otsu's method](https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html).


## 28 June
I want to create a UI before carrying on with anything else, the problem is having a UI that
allows you to see how your edits effect the image whilst you are editing it. I'm not sure if you can
do that with tkinter. PyQT may work better.