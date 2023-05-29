FROM python:3.10

MAINTAINER tlsabara

ENV APP_ROOT_DIR=/home/app_ping/
#ENV PATH /home/${USERNAME}/.local/bin:${PATH}
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
ENV DEV_ENV=${DEV_ENV}
ENV TEST_ENV=${TEST_ENV}

WORKDIR $APP_ROOT_DIR

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install fastapi uvicorn

EXPOSE 8000

CMD uvicorn api.entry:app --host 0.0.0.0 --port 8000
