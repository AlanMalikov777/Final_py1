# Final_py1

It is a program that contains 2 web pages. First, it works for logining user and if a database has a date about the user it will give and save token in a database and redirect them to the next page. Second, it works for searching and summarizing information about concrete token. It uses a bootstrap on each HTML page.

# Team

Asanuly Alikhan

Malikov Alan

Kurmangali Sanzhar

# Installation
You need to download these libraries: 'Flask', 'Flask-SQLAlchemy', 'requests', 'beautifulSoup', 'transformers ', 'jwt'
With using this codes:
```bash
pip install Flask
```
```bash
pip install Flask-SQLAlchemy
```
```bash
pip install requests 
```
```bash
pip install beautifulsoup4
```
```bash
pip install transformers
```
```bash
pip install pyjwt
```
# Usage
Run test.py from test folder, use a direcory to the folder test and run it with this command in cmd or other termianls (src and test folders should be lockated in one package)
``` bash
python test.py
```
Alternative is taking python files from src and use it by your own or copy code and use it.
# Test
Test:

Loginning:

![fp1](https://user-images.githubusercontent.com/77801087/142907646-9f50ec1d-d58f-4a61-b1b2-cddfc771cfc2.jpg)
Redirect to searching web page and processing a search:

![fp2](https://user-images.githubusercontent.com/77801087/142907977-920390d1-7d9c-4ca7-9017-955e4678ab08.jpg)
![fp3 (2)](https://user-images.githubusercontent.com/77801087/142908113-136ffcee-1692-4b5a-b1fa-6501ecfad5a6.jpg)

Results in PostgreSQL tables:

![fp4 (2)](https://user-images.githubusercontent.com/77801087/142911630-b1909c35-a8f8-4461-901c-f476c8434ec1.jpg)

It saves summary that huggingface has done:

![fp5](https://user-images.githubusercontent.com/77801087/142913691-d0162123-9b89-4f29-8472-aec0867eff53.jpg)

# License
[MIT](https://choosealicense.com/licenses/mit/)
