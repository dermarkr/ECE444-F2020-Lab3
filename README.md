# ECE444-F2020-Lab3

Repo Owner: Robert Dermarkar

This Branch is for UofT ECE444 Lab4 for learning Docker

This repo is a clone of https://github.com/miguelgrinberg/flasky

Activity 1:

I have read these pieces of documentation

Activity 2:

To run this image first ensure that Docker in properly installed on your computer. 

1) Open Command Prompt/Powershell/Terminal in root folder ("\ECE444-F2020-Lab3")

2) Run Command "docker build -t ece444-f2020-lab3_web:latest .". This should build the image.

3) Run Command "docker run -d -p 5000:5000 ece444-f2020-lab3_web". 

4) You should now be able to go the website with URL "http://localhost:5000/"

![Screenshot 2](/images/ECE344_Lab4_Part2_Screenshot1.jpg)

![Screenshot 3](/images/ECE344_Lab4_Part2_Screenshot2.jpg)


Activity 3:

Virtual Machines (VMs) are used to emulate hardware and an Operating System (OS) on a device which does not have those specification or enabaling the complete isolation of processes from one another.

Docker on the other hand generally use the host's OS and libraries with some alterations to ensure the correct environment. 

VMS have the following hierarchy Host OS -> Hypervisor -> Guest OS -> Bins/Libs -> App 

whereas Docker Containers have the following hierarchy Host OS -> Docker Engine -> Bins/Libs -> App.

The need for VMs to have their own OSs means that they have a much higher overhead.

Docker Containers can also be shared easily due to their small size with the image being constructed locally . 

VMs on the other hand need the entire image to shared which can be several GB versus KBs for Docker.
