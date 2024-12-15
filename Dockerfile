#This is my first docker file

FROM python:latest

RUN pip install pandas numpy matplotlib

WORKDIR /desktop/Docker

CMD "pwd"

RUN useradd -ms /bin/bash sahiluser

USER sahiluser
ENV app_host="0.0.0.0"
ENV app_port=5000

CMD "env"
COPY app.py /desktop/Docker
LABEL environment = production
LABEL team=banking-app

EXPOSE 5000
