## Making my GUI

A GUI is one of the most important parts of my project, the user must be able to view how their edits are changing
 the image being edited.

[tutorial I'm following](https://towardsdev.com/create-a-simple-gui-image-processor-with-pyqt6-and-opencv-1821e1463691) |
[a great youtube tutorial for this kind of thing](https://www.youtube.com/watch?v=4B3kYF5BhB4) | [really good QMainWindows tutorial](https://realpython.com/python-menus-toolbars/#creating-actions-for-python-menus-and-toolbars-in-pyqt)

I want to be able to continue making edits to a photo, and the gui continually shows you these changes on the photo
as you make them.

In order to load the image into the gui, I will abstract out the process of converting an image
into a numpy array so that I can make it all work nice.

I create a 'main_layout' which contains most of the widgets for the screen. Inside this layout
is 'top_bar_layout', 'image_bar_layout', 'bottom_bar_layout'. 