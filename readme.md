###Project name: is_carrot

###Author: Joshua Skootsky

###Year: 2015

###License: Boost 1.0 (See LICENSE file or http://www.boost.org/LICENSE_1_0.txt)

#Purpose:

To identify carrots

#Specification:

If there is a carrot in the picture, say so

#Motivation:

https://www.facebook.com/groups/1500321840185061/1579590368924874/

Athena Cocoves:
"is that a carrot" identification software

#Usage:

in the carrot.py file, change one (or two!) of the image path variables to
pictures you would like to compare to carrots, or anything else really.

Carrot.py when run will find the 10 most similar features between the two
images using the ORB algorithm from OpenCV

#Dependencies:

    Python 2.7
    OpenCV 2.6.11 (Put it in your PYTHONPATH)

This project could be re-written for Python 3 and OpenCV 3.0.0    

#Why is this hard?

http://xkcd.com/1425/

transcript

    [Ponytail sitting at a computer with Cueball standing behind her.]
    Cueball: When a user takes a photo,
    the app should check whether they're in a national park...
    Ponytail: Sure, easy GIS lookup. Gimme a few hours.
    Cueball: ...and check whether the photo is of a bird.
    Ponytail: I'll need a research team and five years.
    In CS, it can be hard to explain the difference between the easy
    and the virtually impossible.    



