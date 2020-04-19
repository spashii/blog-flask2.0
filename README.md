# blog-flask2.0
an update(to-be) to the original blog-flask with new and updated features
* all new explore page
* the homepage now has posts from followed users only
* users need to login to see the homepage
* users can post straight from the homepage
* users can now follow and unfollow other users
* users get a cool unique profile picture by default(change through gravatar)
* posts no longer have a title field
### setup (Ubuntu) //incomplete
* install **python3.7** and **python3.7-venv**
  ```bash
  # may need to use sudo for these commands
  $ apt install python3.7       
  $ apt install python3.7-venv
  ```
* create a virtual environment **venv**
  ```bash
  $ python3.7 -m venv path/to/new/venv
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
   FLASK_APP=blog.py
   SECRET_KEY=your-secret-key
   SQLALCHEMY_DATABASE_URI=sqlite:///your/database/example.db
   # if you want to use Google  
   MAIL_SERVER=smtp.googlemail.com
   MAIL_PORT=587
   MAIL_USERNAME=example-email@gmail.com
   MAIL_PASSWORD=example-password
  ```
### how to run
* activate the virtual environment with required packages
  ```bash
  $ source path/to/new/venv/bin/activate
  ```
* run the app
  ```bash
  flask run
  ```
### todo
* update README.md
* add database setup instructions
* make lower-casing usernames and emails client-side
* one session per user
* ~bug:edit_profile:when entering pre-existing usernames~
* post/redirect/get everything
