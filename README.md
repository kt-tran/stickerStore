# Sticker Store website
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
[![SQLAlchemy][sqlal-shield]][sqlal-url]
<br>
[![Bootstrap][Bootstrap.com]][Bootstrap-url]


<!-- PROJECT LOGO -->
<div align="center">
  <a href="https://github.com/kt-tran/stickerStore">
  <img src="/img_README/cart4.svg" width="100" height="100">
</svg>
  </a>

<h3 align="center">eCommerce Website</h3>
  <p align="center">
    Rapid Web Development
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
University assignment for a 5-week web development course using MVC.

Progression: <br>
Front end > Back end > Database

Overview:
- Home page
- navbar + footer
- cart + checkout (no user verification yet)
- product details page (only one at the moment)
- browse by category/artist
- search by product name

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Features -->
## Features

### Welcome!
![welcome](/img_README/welcome_modal.gif)
Welcome GIF button in overlaid footer that disappears upon return to homepage (i.e. if session in order) <br>

### Have a look around
![browse](/img_README/browse_all.gif) <br>

### Browse by category
![category](/img_README/navbar_categories.gif)
Support an artist by buying more of their stickers, or build your animal sticker collection by browsing through the animal section.

### Want something specific?
Search for a sticker by title: <br>
![search](/img_README/search.gif)

### How to use the cart
![cart](/img_README/cart.gif)

### Ready to purchase?
![place_order](/img_README/verification_order.gif)
Leave your details and we'll get back to you. <br>
NOTE: order completion outlined by task requirements

### Incomplete:
- unable to access footer before dismissing modal button (GIF in bottom right corner) as footers are overlayed ontop of each other
- personal artist pages
- add multiple of one sticker/item to cart
- category "more" buttons for item cards on homepage

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

QUT code snippets were provided & used throughout.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[year-shield]: https://img.shields.io/badge/Year-2022-blue
[python-shield]: https://img.shields.io/badge/Flask-lightgrey
[css-shield]: https://img.shields.io/badge/CSS-orange
[CSS-url]: https://www.w3.org/TR/CSS/#css
[sqlal-shield]: https://img.shields.io/badge/SQLAlchemy-red
[sqlal-url]: https://www.sqlalchemy.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com