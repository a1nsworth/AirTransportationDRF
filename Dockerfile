FROM python:3.12 as python-base
RUN mkdir air_transportation_image
WORKDIR  /air_transportation_image
COPY /pyproject.toml /air_transportation_image
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

RUN chmod a+x ./scripts/setup.sh
CMD ./scripts/setup.sh