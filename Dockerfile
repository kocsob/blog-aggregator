FROM alpine:latest

MAINTAINER Balazs Kocso

RUN apk add -U python py-pip

ADD . /blog-aggregator
WORKDIR /blog-aggregator

RUN pip install -r requirements.txt

VOLUME [ "/data" ]
CMD [ "python", "__main__.py", "--input=/data/input.html", "--output=/data/output.json", "--log-level=DEBUG" ]
