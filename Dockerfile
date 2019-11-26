FROM python:3


ADD quiz.py /
ADD quiz.json /


RUN pip install pystrich 

CMD ["python", "./quiz.py","quiz" ]
