
# docker_tutorial/backend/Dockerfile
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /aplicativio
WORKDIR /aplicativio
RUN pip3 install -r requirements.txt
RUN pip3 install Django psycopg2