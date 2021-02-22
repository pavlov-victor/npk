FROM python:3
COPY ./npk_project/requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY ./npk_project /code
WORKDIR /code/