FROM python:3.7-alpine3.11

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python3", "app.py" ]
