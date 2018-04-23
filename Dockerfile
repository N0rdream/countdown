FROM python:3
RUN mkdir /countdown
WORKDIR /countdown
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /countdown