# Lightbulb

Lightbulb is a blog offering users and guests a page to share their innovative ideas with interested contributors and spectators.

The blog takes a simple format and comprises of two pages, a landing page where posts are available and a review page for users to leave feedback.

The idea of the website is to provide a space where individuals can discuss ideas and find other like minded individuals, including potential collaborators and investors.

The project has been designed as a deliverable for the fourth project in the Code Institutes Diploma
in Full Stack Software Development.

Logged in users can make posts, comment and like posts. Individuals who are not logged in have read only access to all elements of the website. 

There is post approval in place in order to filter posts to assure all posts are keeping inline with what the blog endeavours to provide, this assures any distasteful posts are never seen by site users. Reviews can also be deleted by admin if they are distasteful.

Link to live website -

[Lightbulb](#)

place AMI RESPONSIVE HERE.

## Table of Contents

## Design

The Design is purposely simple, only options that are value adding are presented to site visitors, if logged in they can instantly post using the button presented to them. Individuals who are not logged in have the option to log in or register on the navigation bar, they can do this or they can scroll and browse posts without doing so. The bottom of the page allows the user to navigate to the review page where they can leave a review if they wish.

## Design Features

### Header

### Footer

### Main page

### Palette

The palette that has been used is a mix of solid, complimentary colours so as to not over complicate or take away from the blog aspect of the website

<img src= "media/readmeMedia/palettelightbulb.jpg">

### Fonts

Utilised the following fonts from google fonts -

font-family: 'Bebas Neue', cursive;
font-family: 'Roboto Slab', serif;


### Flowchart - intended website build 

<img src="/workspace/lightbulb/media/readmeMedia/Flowchart.jpg">

### Wireframes

<img src="/workspace/lightbulb/media/readmeMedia/wireframe1.jpg">
<img src="/workspace/lightbulb/media/readmeMedia/wireframe2.jpg">




<img src="/workspace/lightbulb/media/readmeMedia/wireframePhone.jpg">
<img src="/workspace/lightbulb/media/readmeMedia/wireframePhone2.jpg">


## Current Active Features

## Potential Future Features


## User Stories

Kanban board with user stories available at [User Stories Kanban board](https://github.com/users/john33mcd/projects/4), full list below.

* As a website user I can register for an account so that I can log in and add comments and posts

* As a Moderator I can assess posts and approve them so that posts are suitable for the website

* As Admin I can approve comments so that I can restrict content that should not be available on the site

* As a user I can view posts from other users and myself so that I can see and provide feedback if I want to

* As a user I can leave feedback for other users so that I can interact with the community

* As a website user I can log into my account so that I can use the website to post, edit and delete from my own personal account

* As a website user I can register for an account so that I can log in and add comments and posts

* As a website user I can leave a testimonial so that I can share my experience using the site

* As a user I can delete posts so that I can remove content from the website
 
* As a user I can edit a post so that I can change post details

* As a website user I can favorite posts so that I can see all my favorite posts in one place

* As a website user I can categorize posts so that I can see a unique selection of posts based on my own requirements


## Website Goals

### User Goals

### Admin Goals

## Testing

## Entity Relationship Diagram, Database

## validation

### Lighthouse

### W3C HTML

### W3C CSS

### python validation

## Bugs and Issues

* Had an issue in which database migration failed on one occasion, jumping a migration and not allowing for subsequent migrations. Issue was that a non INT value was passed for the default option on fields in a model which could not accept INT value. in order to rectify error, edited __init__ file with the issue to a number then submitted all changes.

__BUG__ - slug = models.SlugField(default="", max_length=200, unique=True, null=False)

__FIX__ -

0003_post_author.py - changed default to 1.

* Had bug where no reverse match was available, this was due to a post with the title '-' throwing the error, rectified by removing this post in admin.

* Ran out of gitpod hours and received extra permissions through tutor support, migration of project resulted in env.py file being removed from new workspace causing project not to load, rectified by rebuilding env.py file.


## Deployment

- Install all dependencies to begin, add all dependencies to requirements.txt file using the pip3 freeze --local > requirements.txt command.

- Create django project and app using the relevant commands.

- Go to Heroku, click New on the dashboard, create new app, name the app and click create.

- link database on the elephantSQL.com website, create, name and plan was selected for new instance.

- set environment variables using env.py file in order to keep sensitive keys and files secure.

- get API key from external media host Cloudinary and add it to project.

- Add config vars on heroku for database, secret key and external media host (Cloudinary).

- connect to github account on Heroku, search for relevant repo on this project page and then build.

## Credits and References

- [Django To Do List App](https://www.youtube.com/watch?v=llbtoQTt4qw&t=90s), Dennis Ivy. Used to understand MVC relationships and implementation, to test views and url connection, used to set up model for users. Also utilised to understand login/registration functionality.

- Used Code Institutes I think therefore I blog sample project as a starting template, utilising models, admin, comments, posts and template codes as a foundation for my own project

- Palette taken from [mycolor](https://mycolor.space/)

- Footer positioning learned from [dev.to](https://dev.to/nehalahmadkhan/how-to-make-footer-stick-to-bottom-of-web-page-3i14)

- Used [Corey Schafer](https://www.youtube.com/watch?v=-s7e_Fy6NRU&t=1398s) to create post and delete functions.

- Used the following to implement unique [slugs](https://studygyaan.com/django/how-to-create-a-unique-slug-in-django?utm_content=cmp-true)

- [Stackoverflow](https://stackoverflow.com/questions/43879330/djangounable-to-compare-the-logged-in-user-with-the-author-of-the-post) utilized to check author and user authentication for buttons edit and delete.

- [Pexels](https://www.pexels.com/) used for post and detail images.

- Dropdown for review list learned from [stackoverflow](https://stackoverflow.com/questions/31130706/dropdown-in-django-model) and [stackoverflow2](https://stackoverflow.com/questions/66302329/how-to-create-dropdown-box-with-forms-modelform-in-django)

- codeblock for hero image area taken from [W3Schools](https://www.w3schools.com/howto/howto_css_hero_image.asp)

- [Wireframes](https://wireframe.cc/) created on Wireframes.cc.

- [Charts](https://lucidchart.com) created using Lucid chart.