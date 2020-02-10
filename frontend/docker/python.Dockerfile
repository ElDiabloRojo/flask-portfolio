FROM node:12.14-alpine as node

LABEL maintainer="ElDiabloRojo <holdens.uk@googlemail.com>"
LABEL version="1.3"
LABEL description="Docker image for apy."

ADD . /
WORKDIR /src
RUN apk add --no-cache --update python3 make g++ && \
	python3 -m ensurepip && \
	npm clean-install && \
	export PATH="$PATH:./node_modules/.bin" && \
	gulp && \
	pip3 install -r /requirements.txt

WORKDIR /
ENTRYPOINT [ "gunicorn" ]
CMD [ "--workers", "2", "--threads", "4", "--log-level", "info", "--bind", "0.0.0.0:5000", "run:app" ]