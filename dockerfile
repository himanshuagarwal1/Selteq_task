FROM python:3.8

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
CMD celery -A yourproject worker --loglevel=info & celery -A yourproject beat --loglevel=info
COPY . /code/