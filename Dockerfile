FROM python:3.6-alpine as builder

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev \
                       python3-dev \
                       \musl-dev \
                       libmagic \
                       build-base \
                       openssl \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev

# copy project
COPY . /usr/src/app/

# install dependencies
RUN python -m pip install -U --force-reinstall pip
# RUN pip install --upgrade pip
RUN pip install flake8
COPY . /usr/src/app/
RUN flake8 .

COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


# #################
# Final Container #
# #################
FROM python:3.6-alpine 

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

RUN apk update && apk add postgresql-dev \
                       python3-dev \
                       \musl-dev \
                       libmagic \
                       build-base \
                       openssl \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev

COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .

# copy entrypoint.sh
COPY ./entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chmod 755 $APP_HOME/entrypoint.sh
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

RUN pip install --upgrade pip
RUN pip install --no-warn-script-location --no-cache /wheels/*

EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]