# Rates visualization project

This is a simple python project using the django framework. It fetches currency rates from an API and displays the information in a chart.


## Running

First makes sure your system have python installed:

    python -V

The response should be something like this:

    Python 3.8.5

After this, run the following commands in the folder of the project:

    python -m pip install -r requirements.txt
    python  manage.py  migrate
    python  manage.py  runserver

The project will start running in your localhost in port 8000

[http://127.0.0.1:8000/view/](http://127.0.0.1:8000/view/)

## Docker alternative

Or, if you're in a Linux environment with docker installed, just run the script deploy.sh

    ./deploy.sh
It'll start a docker instance listening in port 8000

[http://127.0.0.1:8000/view/](http://127.0.0.1:8000/view/)

## How to use

The server is listening in the */view*  address. If you go to this address, it'll automatically take the last 5 work days to show the rates.

From there you can change the currency and the dates. If you first select the start date, the end date will be automatically calculated for you.

## Bookmarkable URLs 

There's another way to use the project, inputting the information direct in the URL, like this

  [/view/eur/20211129/20211203](/view/eur/20211129/20211203)

 The first part is the currency, it accepts eur, brl and jpy. The second and third parts are the start and end dates, in YYYYMMDD format.

## API

The project also exposes an API to get the rates that are saved in its database. The endpoint is

[/api/20211129](/api/20211129)

Where the date desired is used in the YYYYMMDD format. If the database still don't have the values, it'll return an error message.

## Demo

The project is running in my server.

[https://www.zilioti.dev/demo_visualiza/view/](https://www.zilioti.dev/demo_visualiza/view/)


