FROM python:3.10-slim

# Install dependencies
RUN apt update && apt install -y \
	curl \
	unzip

# Get PocketBase
RUN curl -LO https://github.com/pocketbase/pocketbase/releases/download/v0.18.6/pocketbase_0.18.6_linux_amd64.zip \
	&& unzip pocketbase_0.18.6_linux_amd64.zip pocketbase -d /usr/local/bin \
	&& rm pocketbase_0.18.6_linux_amd64.zip

# Get Poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VERSION=1.6.1
ENV POETRY_VIRTUALENVS_IN_PROJECT=true

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/opt/poetry/bin:$PATH"

# Install dependencies (for faster builds)
WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry install --no-root

# Build project
COPY ./ ./

# Run backend
EXPOSE 8090

ENTRYPOINT [ "pocketbase", "serve", "--http=0.0.0.0:8090" ]
