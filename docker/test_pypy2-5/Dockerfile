FROM pypy:2-5
MAINTAINER steven.e.cutting@linux.com

RUN pip install --upgrade pip
RUN pip install pytest toolz pytest-runner coverage
RUN pip install click


VOLUME /app

WORKDIR /app

CMD ["/app/docker/docker_pytest.sh"]
