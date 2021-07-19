FROM python:3.9

ADD requirements.txt /Categorizer/requirements.txt

WORKDIR /Categorizer/

RUN pip install -r requirements.txt

#RUN adduser --disabled-password --gecos '' myuser