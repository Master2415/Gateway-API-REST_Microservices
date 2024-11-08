FROM python:latest

WORKDIR /app
COPY . .

RUN pip install flask
RUN pip install sqlalchemy
RUN pip install nats-py
RUN pip install httpx

CMD ["python", "main.py"]
