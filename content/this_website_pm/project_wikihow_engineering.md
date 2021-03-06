**Engineering**   

* This website is built using [streamlit.io](https://streamlit.io), very convenient way to build an analytical web app using mostly Python.   
* Visualizations in Resume section are built using [Altair](https://altair-viz.github.io/) data visualization library.    
* To make things look better and due to limitations of Streamlit caused by its simplicity, a lot of HTML/CSS were used.     
* The web app is deployed using [Docker](https://www.docker.com/):   
```dockerfile
FROM python:3.7-slim-buster

EXPOSE 8501

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .. .

LABEL maintainer="Adilet Gaparov <adilet.gaparov@gmail.com>" \
      version="1.0"

CMD streamlit run app.py --server.port $PORT
```
* Currently hosted on [Heroku](https://www.heroku.com/).            
    