FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python3 -m nltk.downloader -d /usr/share/nltk_data stopwords
RUN python3 -m nltk.downloader -d /usr/share/nltk_data wordnet
COPY .env /.env
#ENV NLTK_DATA /Categorizer/nltk_data/
#ADD . $NLTK_DATA
#RUN python setup.py
#RUN python3 -m nltk.downloader -d /Categorizer/nltk_data stopwords
