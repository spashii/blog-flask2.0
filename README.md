# blog-flask2.0
an update to the original blog-flask with new and updated features
### setup (Ubuntu)
* install **python3.7** and **python3.7-venv**
  ```bash
    $ apt install python3.7
    $ apt install python3.7-venv
  ```
* create a virtual environment **venv/**
  ```bash
  $ python3 -m venv path/to/new/venv
  ```
* activate the virtual environment
  ```bash
  $ source path/to/new/venv/bin/activate
  ```
* install all the requirements 
   ```bash
   (venv)$ pip install -r requirements.txt
   ```
* create a _.flaskenv_ file in **blog-flask2.0/** containing
   ```
   SECRET_KEY='your-secret-key'
   ```
### how to run
* run the app
  ```bash
  python blog.py
  ```
