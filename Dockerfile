FROM python:3.7-slim-buster

EXPOSE 8501

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

LABEL maintainer="Adilet Gaparov <adilet.gaparov@gmail.com>" \
      version="0.1"

CMD streamlit run app.py --server.port $PORT

