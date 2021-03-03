build:
	docker build -t thomasj27/iris_api . 

run:
	docker run -it -p 5000:5000 --network=host thomasj27/iris_api 

update:
	docker push thomasj27/iris_api