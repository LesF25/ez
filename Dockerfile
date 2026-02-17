FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY conf/requirements.txt .
COPY conf/constraints.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt -c constraints.txt && \
    apt-get purge -y --auto-remove gcc

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]
