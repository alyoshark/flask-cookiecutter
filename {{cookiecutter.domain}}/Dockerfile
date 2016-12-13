FROM python:2.7-slim

ADD requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y gcc nginx && \
    pip install -r requirements.txt && \
    apt-get autoremove -y gcc && apt-get clean && rm -fr /var/lib/apt/lists/*
