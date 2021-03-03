FROM ubuntu:18.04

WORKDIR /Api/

RUN apt-get update && \
  apt-get -y install python3-pip && \
  pip3 install --upgrade pip 

COPY iris_api .
RUN pip install -r requirements.txt

CMD python3 api.py