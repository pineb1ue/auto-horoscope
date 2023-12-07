# Builder Stage
FROM python:3.11-slim AS builder
COPY pyproject.toml poetry.lock ./

# Install build-essential for building pyswisseph
RUN apt update && \
    apt install -y build-essential && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip &&  \
    pip --no-cache-dir install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Runner Stage
FROM builder AS runner
WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY ./data ./data
COPY ./app ./app

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]