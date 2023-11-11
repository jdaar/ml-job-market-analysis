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
    py3-wheel \
    chromium

RUN python3 -m pip install --user pipx
RUN python3 -m pipx install poetry
ENV PATH="/root/.local/bin:${PATH}"

COPY ./pyproject.toml /app
COPY ./README.md /app

RUN poetry install -n --no-root

COPY ./market_analysis /app/market_analysis
COPY ./Makefile /app

RUN make build
RUN python3 -m pip install . 

COPY ./run.sh /app
RUN chmod +x /app/run.sh

ENV NODE_MAX_INSTANCE=4
ENV NODE_MAX_SESSION=4

ENTRYPOINT ["./run.sh"]
