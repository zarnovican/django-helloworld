FROM python:2.7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt requirements.freeze.txt requirements.static.txt /usr/src/app/
RUN \
    pip install pip setuptools --upgrade && \
    pip install --no-cache-dir -r requirements.txt && \
    wget -O /usr/local/bin/confd https://github.com/zarnovican/confd/releases/download/v0.12.0-alpha3-51-g7ac1091/confd && \
    chmod 755 /usr/local/bin/confd

ENV PORT=8000

HEALTHCHECK --interval=5s --timeout=2s --retries=1 CMD /bin/bash -c 'set -e; [ "`curl -sSf http://localhost:$PORT/mgmt/health`" == "ok" ]'

ENTRYPOINT ["/bin/bash", "run.sh"]

COPY . /usr/src/app
