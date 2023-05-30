FROM python:3.10
ARG compose
MAINTAINER tlsabara

ENV APP_ROOT_DIR=/code
#ENV DEV_ENV=$DEV_ENV
#ENV TEST_ENV=$TEST_ENV

WORKDIR $APP_ROOT_DIR

COPY ./ $APP_ROOT_DIR

RUN pip install --upgrade pip

RUN pip install -r ./requirements.txt

RUN pip install fastapi uvicorn

EXPOSE 8000
EXPOSE 80
CMD uvicorn api.entry:app --host 0.0.0.0 --port 8000

#RUN echo "#!/bin/sh" >> ./start.sh
#RUN echo "nohup uvicorn api.entry:app --host 0.0.0.0 --port 8000" >> ./start.sh
#CMD sh -c "sh ./start.sh"
# CMD ["/bin/bash", "-c", "cd", "$APP_ROOT_DIR", "|", "uvicorn .api.entry:app", "--host", "0.0.0.0", "--port", "8000"]