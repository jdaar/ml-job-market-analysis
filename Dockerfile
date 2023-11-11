FROM alpine:latest

RUN mkdir /app

WORKDIR /app

RUN apk add --no-cache \
    bash \
    make \
    parallel \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel 

RUN python3 -m pip install --user pipx
RUN python3 -m pipx install poetry
ENV PATH="/root/.local/bin:${PATH}"

COPY ./pyproject.toml /app

RUN poetry install

COPY ./src /app
COPY ./Makefile /app

RUN make build

COPY ./run.sh /app
RUN chmod +x /app/run.sh

ENTRYPOINT ["./run.sh"]
