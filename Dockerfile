FROM python:3.8

# Create a user and switch to it
RUN useradd -m hota
USER hota

HEALTHCHECK NONE
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
