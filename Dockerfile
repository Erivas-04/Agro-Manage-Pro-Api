FROM python:3.10-slim

WORKDIR /app

RUN apt update \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN apt update && apt install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

COPY ./requirements.txt ./

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]