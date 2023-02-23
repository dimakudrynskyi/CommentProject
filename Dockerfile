# pull official base image
FROM python:3.10 

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .
# install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

#run database migrations
RUN python manage.py makemigrations \
    && python manage.py migrate 


EXPOSE 8000


CMD [ "python", "manage.py", "runserver" ]
