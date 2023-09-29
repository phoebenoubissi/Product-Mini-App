
#phoebe-products is the name of my app -t is the tag, -f is ...
build-image:
	sudo docker build -t phoebe-products -f Dockerfile .

run-image:
	sudo docker run -p 5000:5000 -d phoebe-products

# -d is detach, to run in the backend, -p is port of the docker to connect with port of host_id
#http://localhost:5000 (the app will be running at that url)