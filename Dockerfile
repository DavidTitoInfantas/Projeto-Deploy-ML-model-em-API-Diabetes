## V1
FROM python:3.10

ADD . /app

WORKDIR /app

RUN pip3 install -r ./app/requirements.txt

#COPY . .

CMD ["python",  "app/index.py"]