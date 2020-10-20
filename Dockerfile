FROM python:3.6

EXPOSE 9000

WORKDIR /stocks

RUN apt-get update \
    && apt-get install -y python3-dev libffi-dev libxslt-dev libxml2-dev gcc musl-dev g++ \
    && apt-get install -y  ca-certificates wget


ADD ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ADD . /stocks
ENTRYPOINT ["./run.sh"]
