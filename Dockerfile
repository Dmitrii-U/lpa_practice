FROM python:3.12-alpine

WORKDIR /app

COPY . /app

RUN apk add gcc musl-dev libffi-dev

RUN pip install -U pip
RUN pip install poetry

RUN poetry install --no-root

CMD ["python", "tic_tac_toe.py"]