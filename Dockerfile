FROM python:3.12.13 as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

# Install uv
RUN pip install uv

# Install python dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

FROM node:lts-slim as npm-deps

WORKDIR /npm
COPY ["package.json", "package-lock.json", "./"]
# Install npm dependencies
RUN npm ci

FROM base AS runtime
# Needed by production image, but better for caching to install it before code
RUN apt-get update && apt-get install -y gettext

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home cms
WORKDIR /home/cms

COPY --from=npm-deps /npm/node_modules ./node_modules

# Install application into container
COPY . .

FROM runtime as develop

ENTRYPOINT ["/home/cms/scripts/docker_entrypoint.sh"]

FROM runtime AS production

ENTRYPOINT ["/home/cms/scripts/docker_entrypoint_gunicorn.sh"]
