LABEL authors="Maxim Sergeev <maxsergeev39@gmail.com>"

FROM python:3.12-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.3

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
COPY ../src ./src

RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root --no-interaction --no-ansi && \
    poetry build

FROM base as final

COPY --from=builder /app/.venv ./.venv
COPY --from=builder /app/dist .
COPY docker-entrypoint.sh .

RUN ./.venv/bin/pip install *.whl
CMD ["./docker-entrypoint.sh"]