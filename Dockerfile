FROM python:3.6-alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev

WORKDIR /usr/src/app

# install requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy the application
COPY . .

# install the application
RUN pip install -e .

EXPOSE 8080

CMD ["python", "wsgi.py"]

