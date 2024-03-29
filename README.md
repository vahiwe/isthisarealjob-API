<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

## :page_with_curl: _About_
- This is the source code for the job confidence checker on [ITARJ](itarj.com)
- You'll need [chromedriver](https://chromedriver.chromium.org/getting-started) for the selenium processes. Once it's installed update the chrome_path variable in the cac_check file `chrome_path = 'path/to/chromedriver'`

- Gunicorn and Nginx configuration files are also included

## :page_with_curl: _Installation Guide_

**1)** Fire up your favourite console & clone this repo somewhere:

__`❍ git clone https://github.com/vahiwe/isthisarealjob-API.git`__

**2)** Enter this directory:

__`❍ cd isthisarealjob-API`__

**3)** Install other python packages/dependencies using the requirement file:

__`❍ pip3 install -r requirements.txt`__

**4)** Run the App:

__`❍ python app.py`__

**5)** Open your API Request Client such as [Postman](https://www.getpostman.com/downloads/) or [Advanced Rest Client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo) to make a post request using this json format

__`{
  "company": "NNPC",
  "address": "no. 21 adesanya aguda, surulere",
  "invite": "You are welcom"
}`__

**6)** The request should be sent to this URL to get a response:

__`❍ http://127.0.0.1:5000`__


__*Happy developing!*__
