FROM python:3.10-alpine

WORKDIR /app

RUN apk update && apk upgrade --no-cache
RUN apk add gcc musl-dev mariadb-connector-c-dev
RUN apk add --no-cache tzdata
ENV TZ=Asia/Ho_Chi_Minh

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app

ENTRYPOINT ["python"]
CMD ["findomain.py"]
