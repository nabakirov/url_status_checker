FROM python:3.8-alpine

RUN set -ex && mkdir /app
WORKDIR /app
RUN pip3 install pipenv

COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy --system

COPY . /app

CMD python manage.py migrate && gunicorn url_checker.wsgi -b 0.0.0.0:80 -w 3