FROM python:3.7.3-stretch
ENV PYTHONUNBUFFERED 1
RUN mkdir /price_prediction
WORKDIR /price_prediction
COPY requirements.txt /price_prediction/
RUN pip install -r requirements.txt
COPY . /price_prediction/

EXPOSE $PORT
CMD python train.py
CMD ["gunicorn"  , "-b", "0.0.0.0:$PORT", "API:app"] 