FROM python:3.7-buster

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=application

ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--port=8080"]
