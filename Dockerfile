FROM python:3.8
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD ["uwsgi.ini"]