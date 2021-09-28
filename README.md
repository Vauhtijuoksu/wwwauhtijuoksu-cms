# WWWauhtijuoksu-CMS

This is a CMS-enabled website for Vauhtijuoksu ry and its speedrun marathons.a

The project is built using Django and Django CMS.

**Note**: The project is currently a work in progress, and not in production.

## Technologies

* [Django](https://www.djangoproject.com/) 3.2
* [Django CMS](https://www.django-cms.org/en/) 3.9 
* [Bootstrap](https://getbootstrap.com/) 5

## Dependencies

**Required**:
* Python 3.9 (recommended), 3.7 or later is likely to work.
* pip
* NodeJS/NPM

OR use Docker for development (see below)

**Recommended**:
* [Pipenv](https://github.com/pypa/pipenv) is recommended for package & environment management

## Installing & running

1. Install NPM dependencies with `npm install`
1. Python dependencies are defined in the `Pipfile`, and can be installed with Pipenv:
    `pipenv install`
1. Activate the virtual env created by pipenv with:
    `pipenv shell`
1. Initialize database
    `python manage.py migrate`
1. Create the admin user
    `python manage.py createsuperuser`
1. Run the development server
    `python manage.py runserver`
1. Server should now be up running at http://localhost:8080

### Using docker

1. `docker-compose build`
1. `docker-compose up` should build & start the app in a Docker container.
1. `docker-compose exec web migrate`
1. `docker-compose exec web createsuperuser`

This is intended for development only!

## Using the CMS

### First time

After installing & running the server for the first time, there is not yet any content on our webpage, so we must start by creating some.

1. Navigate to the admin site at http://localhost:8000/admin and log in with your newly created superuser credentials
1. The default page creation wizard won't work here, so close it. Press "example.com" in the cms toolbar at the top of the page
1. Go to "Pages" and press Add new Page. Give it a name ("frontpage" or whatever) and press Save at the Bottom
1. In the page listing, press the eye symbol to navigate to the new page. It has no content yet, but the menu should pop up including the page itself.

### Adding content

1. In the CMS toolbar, open the sidebar from the top right
1. In the sidebar, you can press the "plus" button to add Plugins to your CMS page. Plugins are basically pieces of content that will be rendered on the page.
1. Select the type of plugin you want to add, then modify the content to whatever you want

Plugins can be reordered and modified however you want. Some plugins can even be nested!

### Publishing

Any changes you make to your pages won't actually go live until you publish the changes. Publishing is easy, just press the button in the upper right corner!

You can see the status of all pages in the Pages listing visited before

