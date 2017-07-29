# Shop Score Page


#### The service has been done for dushboard purpose. It allows monitor KPI of internet shop


## KPI Specifications
  - Primary KPI information
  - Supplementary KPI infromation


### Primary information
- If unconfirmed order waiting time not more 7 minutes,the score indicator filled as **green**
- If unconfirmed order waiting time not more 30 minutes,the score indicator filled as **yellow**
- If unconfirmed order waiting time  more 30 minutes,the score indicator filled as **red**


### Supplementary KPI infromation
- Displays a count of **unconfirmed orders**
- Shows a count of **confirmed orders** for current day


### The web-service  features
- Mobile first
- Disallow for all user agents 

### Deploy on localhost

Example of frontend launch on Linux, Python 3.5:

```bash

python3 server.py
```

Open page [localhost:5000](http://localhost:5000) in browser.

The sample page you can find out on hosted heroku by this adress [devman-shop-score.herokuapp.com](http://devman-shop-score.herokuapp.com)


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)