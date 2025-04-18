FROM python:3.12-slim-bullseye
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod a+x docker/*.sh