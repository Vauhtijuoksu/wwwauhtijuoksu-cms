FROM python:3.9.7 as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install

FROM node:lts-slim as npm-deps

WORKDIR /npm
COPY ["package.json", "package-lock.json", "./"]
# Install npm dependencies
RUN npm ci

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home cms
WORKDIR /home/cms

COPY --from=npm-deps /npm/node_modules ./node_modules


# Install application into container
COPY . .

RUN ["chmod", "+x", "/home/cms/scripts/docker_entrypoint.sh"]

