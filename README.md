# WWWauhtijuoksu-CMS

This is a CMS-enabled website for Vauhtijuoksu ry and its speedrun marathons.a

The project is built using Django and Django CMS.

**Note**: The project is currently a work in progress, and not in production.

## Dependencies

**Required**:
* Python 3.9 (recommended), 3.7 or later is likely to work.
* pip

**Recommended**:
* [Pipenv](https://github.com/pypa/pipenv) is recommended for package & environment management

## Installing & running

1. Python dependencies are defined in the `Pipfile`, and can be installed with Pipenv:
    `pipenv install`
1. Initialize database
    `python manage.py migrate`
1. Create the admin user
    `python manage.py createsuperuser`
1. Run the development server
    `python manage.py runserver`
1. Server should now be up running at http://localhost:8080
