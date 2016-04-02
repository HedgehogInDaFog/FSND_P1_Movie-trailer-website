# FSND_P1_Movie-trailer-website
This is a Project 1 for Udacity FSND

## Information for Users

### Description

Application generates HTML-page, which shows to user a number of movies with some useful info. User can also watch movie trailer by clicking on a movie poster

### General Usage Notes

To run the application you need to:
1. [Download Python](https://www.python.org/downloads/) and install it
2. [Download this project](https://github.com/TrueZarathustra/FSND_P1_Movie-trailer-website)
3. Run entertainment_center.py from project, using your python interpreter. The particular way 
depends on your OS and python package, but generally 
```
python entertainment_center.py 
```
in your command line should work
4. After that you should see a new page in the browser with the "Movie Trailer Website"

## Information for Developers

### Main technologies
Main technologies used:
 - HTML&CSS
 - JS
 - Python

### Files and their description
1. fresh_tomatoes.py
This file contains:
 - HTML templates
 - python functions to fill HTML templates with actual information and create HTML page
 - python functions to open created HTML page in the webbrowser
 You should change it if you want to change web page appeareance and style.
 
2. media.py
The file contains Movie class. 
You should change it in case you want to add more attributes to the movie (btw it will lead changing all other files also)

3. entertainment_center.py
This file contains data about every movie, which is shown. If you want tot add new movie you should modify movie_data
This file also initiate new instancies of Movie class and uses functions from fresh_tomatoes.py to generate HTML and show it in the web browser

## Contact information

Author: Vladmir Vorotnikov

E-mail: v.s.vorotnikov@gmail.com

Feel free to contact me.
