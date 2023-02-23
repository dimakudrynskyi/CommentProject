# CommentProject

This is project where you can create chat and write comment there. It is written in Python and Django.
## About functionality
On the main page, you can see all chats which already been created also you can create a new one.

When you click on chat link you will see all comment with was written.

To write a new comment, you need to enter some information about yourself and pass a captcha

## Prerequisites

[Install Docker](https://docs.docker.com/install/).

Install Python

## How to use

1. Clone git repository
    ```
        git clone https://github.com/dimakudrynskyi/CommentProject.git
    ```
2. Set up your secrets in settings.py
    ```
    SECRET_KEY = os.environ.get("SECRET_KEY") #django secret key

    #public and private key for google captcha
    RECAPTCHA_PUBLIC_KEY =  os.environ.get("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY =  os.environ.get("RECAPTCHA_PRIVATE_KEY")

    #information about db
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get("NAME"),
            'USER': os.environ.get("USERNAME"),
            'PASSWORD': os.environ.get("PASSWORD"),
            'HOST': os.environ.get("HOST"),
            'PORT': '5432',
        }
    }
    ```
3. Create docker image 
    ```
        docker build . -t comment_app
    ```
4. Run the image
    ```
        docker run comment_app
    ```
