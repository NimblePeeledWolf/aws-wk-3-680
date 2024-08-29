FROM python: 3.9-slim
#set working directory
WORKDIR /app
#copy th current directory contents into the containter
COPY . /app
#install needed packages
RUN pip install --no-cache-dir -r requirements.txt
#make port 5000 available to world
EXPOSE 5000
#define environment variable
ENV PORT 5000
#run app.py when container launches
CMD ["python", "app.py"]