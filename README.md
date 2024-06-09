
# LocomotiveDataAPI

LocomotiveDataAPI is a RESTful Web Service which aims to provide information Indian locomotives (Indian Railways) scraped from Wikipedia.


## Updating the Database

Update the database before making an API call.

```bash
  python manage.py updatemodels
```
    
## Demo

Endpoint demonstration of the API

https://localhost:8000/locomotives

![demo](./demo.png)

Lets search for a particular locomotive e.g. WAP-1

https://localhost:8000/locomotives/wap-1

![demo2](./demo2.png)