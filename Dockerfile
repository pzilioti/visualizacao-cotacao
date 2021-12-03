FROM python:3.8

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:8000", "visualizacao_cotacao.wsgi"]
  