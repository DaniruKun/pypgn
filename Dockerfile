FROM python:3.8.0
MAINTAINER Daniils Petrovs

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "make", "test" ]