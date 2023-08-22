FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY requirements.txt /workspace/requirements.txt

RUN pip install -r requirements.txt

COPY ./ /workspace
