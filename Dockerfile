FROM alpine:3.11
WORKDIR /myapp-service
ADD requirements/dev.txt requirements.txt

RUN apk update
RUN apk add --no-cache gcc g++ python3 python3-dev musl-dev alpine-sdk linux-headers postgresql-dev \
    && pip3 install -U pip \
    && pip3 install -U setuptools \
    && pip3 install -U cython \
    && pip3 install -U kiwisolver \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del gcc g++ python3-dev musl-dev alpine-sdk linux-headers

COPY . /myapp-service
COPY .env /myapp-service/.env

VOLUME /logs