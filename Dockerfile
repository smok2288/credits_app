FROM python:3.10

COPY requirements.txt /temp/requirements.txt
COPY credits_app /credits_app

WORKDIR /credits_app

# Устанавливаем зависимости через pip
RUN pip install -r /temp/requirements.txt

EXPOSE 8000

RUN adduser --disabled-password service-user

USER service-user
