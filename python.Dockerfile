FROM node:12.14-alpine as node

LABEL maintainer="ElDiabloRojo <holdens.uk@googlemail.com>"
LABEL version="1.3"
LABEL description="Docker image for apy."

ENV PATH="./node_modules/.bin:${PATH}"

ADD . /app
WORKDIR /app
RUN apk add --no-cache --update python3 make g++ && \
	python3 -m ensurepip && \
	npm clean-install && \
	pip3 install -r requirements.txt

WORKDIR /app/frontend
ENTRYPOINT [ "gunicorn" ]
CMD [ "--workers", "2", "--threads", "4", "--log-level", "info", "--bind", "0.0.0.0:5000", "run:app" ]