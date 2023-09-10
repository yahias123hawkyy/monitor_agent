Hey!
 
In order to start the program, all you have to do is:
 
1. Download the source code to your local machine.


2. using the shell, Enter the directory of the flask application, /flask_python , create the image " sudo docker build -t flaskweb-app -f Dockerfile-flaskweb . " then run the container " docker run -d --name flaskweb-app -p 83:80 flaskweb-app "
3. using the shell, Enter the directory of the nodejs application, /nodejs , create the image " sudo docker build -t nodeapp -f Dockerfile-nodeweb . " then run the container "    sudo docker run -d --name nodeapp -p 3000:3000 nodeapp  "

 
4. Enter the monitor folder, to find the Dockerfile (image implementation file), then create an image using the command " docker build -t monitoring-agent . " 
5. Run a container out of the image using the command " docker run -d --name monitoring-agent --privileged --pid=host --net=host -v /var/run/docker.sock:/var/run/docker.sock monitoring-agent . "
  Please note that in this command there are many parameters, which are put there only to give the monitoring agent permission to access whatever resources it needs to do its job!


Note : Please consider running the web apps first, then the monitoring agent.
Note 2: The monitoring agent is calculating the average during first 5 seconds, you can change it if you want , but you will have to re-do the process of creating an updated Docker image. and then a new container of it.
 
 
 
