FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt requirements.freeze.txt requirements.static.txt /usr/src/app/
RUN \
    pip install pip setuptools --upgrade && \
    pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT ["/bin/bash", "run.sh"]
