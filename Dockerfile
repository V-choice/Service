FROM ubuntu:20.04

RUN apt-get update -y
# RUN apt-get install -y python-pip python-dev
RUN apt-get install python3-pip python3-dev -y
COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD ["run.py"]