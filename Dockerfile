FROM python:3.10

MAINTAINER tlsabara

ENV APP_ROOT_DIR=/code

WORKDIR $APP_ROOT_DIR

COPY ./ $APP_ROOT_DIR

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

RUN pip install fastapi uvicorn

EXPOSE 8000
EXPOSE 80
CMD uvicorn api.application:app --host 0.0.0.0 --port 8000
