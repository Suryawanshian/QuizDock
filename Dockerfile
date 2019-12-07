FROM ubuntu:18.04


RUN apt-get update 

RUN apt-get install -y build-essential python3.7 python3.7-dev python3-pip python3.7-venv

ADD  . /app

WORKDIR /app


CMD ["python3.7", "quiz.py"]
