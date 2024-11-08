FROM python:latest

WORKDIR /app
COPY . .

RUN pip install flask
RUN pip install sqlalchemy
RUN pip install nats-py
RUN pip install httpx
RUN pip install psycopg2
RUN pip install pyjwt
RUN pip install requests

CMD ["python", "main.py"]
