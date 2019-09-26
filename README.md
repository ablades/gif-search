# Gif Search

![Gif Site Demo](gifsearch.gif)

## About
This Gif search project was assigned in  Backend Web (BEW1.1) it displays gifs in a grid format using [Tenor's API](https://tenor.com/gifapi). This is the bootstrap branch that I did solo to get more experience with front end technologies improve. To see the group variant done with [Megan O'Bryan](https://github.com/atleastzero) please refer to the [master branch](https://github.com/ablades/gif-search/tree/master). I used Bootstrap to build the front end of the website. Flask and Jinja were used to build the backend.

## Authors

Bootstrap Branch
* Audaris 'Audi' Blades

Master Branch
* Megan O'Bryan and Audi Blades

Check out more of Megan's work on her [GitHub](https://github.com/atleastzero)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Make sure python3.x is installed along with pip3 package manager
```bash
sudo apt-get install python3-pip3
```
Install flask and requests with pip3
```bash
pip3 install flask
pip3 install requests
```

### Running the Server

1. Open your terminal and clone the respository
```bash
git clone https://github.com/ablades/gif-search.git
```
2. Verify that you are on the bootstrap branch
```
git checkout bootstrap
```
3. Start the Web server
```
flask run
```
Flask will warn you that this is a development server.
To view the website open a browser window to your[localhost](localhost:5000)

## Built With

* [Flask](https://palletsprojects.com/p/flask/) - Lightweight web application framework
* [Jinja](https://palletsprojects.com/p/jinja/) - Template engine for python
* [Bootstrap](https://getbootstrap.com) - Front end framework
* [Tenor API](https://tenor.com/gifapi) - Used Tenor's API for Gifs

## Acknowledgments

* [Make School's starter code](https://github.com/Make-School-Labs/Gif-Search-Starter)