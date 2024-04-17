#FROM python:3.12
#
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
#RUN pip install --upgrade pip "poetry==1.7.0"
#RUN poetry config virtualenvs.create false --local
#COPY pyproject.toml poetry.lock ./
#RUN poetry install
#
#COPY . .


#FROM python:3.12
#
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
#COPY requirements.txt requirements.txt
#
#RUN pip install --upgrade pip
#
#RUN pip install -r requirements.txt
#
#COPY .env .
#
#COPY django_crm .


FROM python:3.12
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY .env .
COPY django_crm .