FROM python:3.12 as python-base
#RUN sudo apt update
#RUN sudo apt install cron
#RUN sudo systemctl enable cron
RUN mkdir air_transportation_image
WORKDIR  /air_transportation_image
COPY /pyproject.toml /air_transportation_image
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

RUN chmod a+x ./setup.sh
CMD ./setup.sh