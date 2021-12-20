FROM python:3.10-bullseye

COPY ./requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

ADD . /app

WORKDIR /app

CMD [ "python", "habrRSSparser.py" ]

