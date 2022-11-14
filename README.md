# Sticker Store website

*University Assignment* - Rapid Web Development (5 week course)

Assignment 1 & 2 - eCommerce website
- Front end: Bootstrap + CSS
- Backend: Flask, SQLAlchemy

Features:
- Home page
- navbar + footer
- cart + checkout (no user verification yet)
- product details page (only one at the moment)
- browse by category/artist
- search by product name

Incomplete:
- unable to access footer before dismissing modal button (GIF in bottom right corner) as footers are overlayed ontop of each other
- personal artist pages
- add multiple of one sticker/item to cart
- category "more" buttons for item cards on homepage


<a name="readme-top"></a>
<!--
*** Readme template from: https://github.com/othneildrew/Best-README-Template/
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

![year][year-shield] 
![python][python-shield]
[![css][css-shield]][CSS-url]
[![SQLAlchemy][sqlal-shield][sqlal-url]]
<br>
[![Bootstrap][Bootstrap.com]][Bootstrap-url]


<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/kt_tran/stickerStore">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cart4" viewBox="0 0 16 16">
  <path d="M0 2.5A.5.5 0 0 1 .5 2H2a.5.5 0 0 1 .485.379L2.89 4H14.5a.5.5 0 0 1 .485.621l-1.5 6A.5.5 0 0 1 13 11H4a.5.5 0 0 1-.485-.379L1.61 3H.5a.5.5 0 0 1-.5-.5zM3.14 5l.5 2H5V5H3.14zM6 5v2h2V5H6zm3 0v2h2V5H9zm3 0v2h1.36l.5-2H12zm1.11 3H12v2h.61l.5-2zM11 8H9v2h2V8zM8 8H6v2h2V8zM5 8H3.89l.5 2H5V8zm0 5a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0zm9-1a1 1 0 1 0 0 2 1 1 0 0 0 0-2zm-2 1a2 2 0 1 1 4 0 2 2 0 0 1-4 0z"/>
</svg>
  </a>

<h3 align="center">eCommerce Website</h3>
  <p align="center">
    Rapid Web Development <br>
    University 5-week Assignment
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
    <img src="img/final.jpg" width="300" height="400" >
</div>

<div align="center">
    <img src="img/green.jpg" width="300" height="400" >
    <img src="img/both.jpg" width="300" height="400" >
</div>

Inspired by a picture of Darren Tarbard's Bin Day Cator, I decided to create one of my own after finding a mini plastic bin for $5 at the store.

<div align="center">
    <img src="img/bin_purchase.jpg" width="300" height="400" >
</div>

This is my first electronics-type project so I decided not to overcomplicate it. <br>
We already have a Pi-hole set up and running at home so I thought to just run the bin program on the same Raspberry Pi as well. <br>
You could probably set this up on an Ardunio (which is much cheaper) too, somehow. A good idea could be to set up smart home LED lights to turn corresponding colours on bin day as well if you already have that set up.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

### Wiring
![First Attempt][wiring-pic]
My first attempt at preparing wires for soldering.

![LED][LED-wire]
After soldering and covering with heatshrink.
I followed this tutorial: [here][led-tutorial]

### Connecting to the Pi
<div align="center">
    <img src="img/pi-pins.jpg" width="300" height="400" >
</div>

<br>Hard to see, so the diagram is probably better:
![Pi GP-I/O][pi-diagram]

<div align="center">
    <img src="img/pi_case.jpg" width="300" height="400" >
</div>
Unfortunately the case no longer fits over the top.

### Inside the bin
<div align="center">
    <img src="img/inside_bin.jpg" width="300" height="400" >
</div>
I gave my sister my hot glue gun but a little bit of sticky tape was enough to fix the plush in place.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Cron -->
## Using Cron

Cron is an in-built Linux utility that allows you to schedule jobs to run periodically. <br> 
Cron is used to run the python file on bin day each week. See: https://crontab.guru/

Store this:
  ```sh
  0 0 * * 2 /usr/bin/python /home/pi/Documents/ledSimple.py
  ```

in the cron table using:
  ```sh
  crontab -e
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Idea: [Darren Tarbard](https://hackaday.com/2020/01/23/bindaycator-lets-you-know-when-to-take-out-the-trash/#:~:text=Having%20four%20LEDs%20both%20helps,segments%20in%20red%20and%20blue)
* Contributor: [Jamie Gee](https://github.com/gouu1)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[year-shield]: https://img.shields.io/badge/Year-2022-blue
[python-shield]: https://img.shields.io/badge/Flask-lightgrey
[css-shield]: https://img.shields.io/badge/CSS-orange
[CSS-url]: https://www.w3.org/TR/CSS/#css
[SQLal-shield]: https://img.shields.io/badge/SQLAlchemy-red
[SQLAl-url]: https://www.sqlalchemy.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com