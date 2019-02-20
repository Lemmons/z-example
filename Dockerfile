FROM python:3-slim

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /src/z-example
WORKDIR /src/z-example

RUN pip install -e .
CMD bash
