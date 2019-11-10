<div align="center">

![hng](https://res.cloudinary.com/iambeejayayo/image/upload/v1554240066/brand-logo.png)

<br>

</div>

## :page_with_curl: _About_
- This is the source code for the job confidence checker on [ITARJ](itarj.com)
- You will need the Python Imaging Library (PIL) (or the [Pillow](https://pypi.org/project/Pillow/) fork). Under Debian/Ubuntu, this is the package python-imaging or python3-imaging.
- Install [Google Tesseract OCR](https://github.com/tesseract-ocr/tesseract) (additional info how to install the engine on Linux, Mac OSX and Windows). You must be able to invoke the tesseract command as tesseract. If this isn’t the case, for example because tesseract isn’t in your PATH, you will have to change the “tesseract_cmd” variable pytesseract.pytesseract.tesseract_cmd. Under Debian/Ubuntu you can use the package tesseract-ocr. For Mac OS users. please install homebrew package tesseract.
- You'll need [chromedriver](https://chromedriver.chromium.org/getting-started) for the selenium processes

## :page_with_curl: _Installation Guide_

**1)** Fire up your favourite console & clone this repo somewhere:

__`❍ git clone https://github.com/vahiwe/isthisarealjob-API.git`__

**2)** Enter this directory:

__`❍ cd isthisarealjob-API`__

**3)** Install other python packages/dependencies using the requirement file:

__`❍ pip3 install -r requirements.txt`__

**4)** Run the App:

__`❍ python app.py`__

**5)** Open your API Request Client such as Postman or Advanced Rest Client to make a post request

__*Happy developing!*__
