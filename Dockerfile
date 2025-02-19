FROM python:3.8
HEALTHCHECK NONE
COPY . .
RUN pip install -r requirements.txt
RUN main.py
