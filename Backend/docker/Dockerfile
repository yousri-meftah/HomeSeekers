FROM python:3.11-alpine

WORKDIR /backend

RUN pip install --upgrade pip

COPY /Backend/requirements.txt /backend/requirements.txt

RUN pip install -r requirements.txt

COPY Backend /backend

ENV PYTHONPATH=/backend

EXPOSE 8000