[![Run Tests and Deploy Flask App to VPS Digital Ocean](https://github.com/AEAnninga/winc_assignment_cd/actions/workflows/deploy.yml/badge.svg)](https://github.com/AEAnninga/winc_assignment_cd/actions/workflows/deploy.yml)

# Flask calculator app overview

The web application itself is very basic, because that wasn’t the scope of this assignment. Just some simple arithmetic calculations. Adding new kind of calculations with corresponding tests should be very straightforward.
For the CD pipeline I wanted a couple of things:

##My own domain:

I have my own domain arisanninga.nl which I  wanted to use for this project. On digital ocean I added my domain and made arisanninga.nl redirect to the droplets ip. On my provider I added the NS records. Now I don’t have to type the ip address of my droplet (or some other funny name).
SSH into server with user instead of root
Then I wanted to have a user to ssh into my server instead of root. So I made the user anningast. The user has sudo/root privilages, but you need a password (also to ssh into the server a passphrase is required).
On the server I needed to be able to pull from github. So I installed a deploy key on my repository for this project and tested the connection. But with user anningast I still couldn’t pull from github or even see the git status. Therefore I made anningast (co) owner of the repo folder on the server. After this I was able to see the status and pull from my github repo from inside my server and I could ssh into the server with anningast instead of root. And when github actions ssh into the server, it can do stuff in the repo folder, but for sudo actions a password is still needed.


##Github actions:


At first I wanted 2 workflows, and when the first workflow succeeded, the second should be triggered. While this can be done, I found it too cumbersome. Instead I chose to put 2 jobs into one workflow. The problem was that I still couldn’t count on the first job also being processed first. The solution was to make the second job dependant of the first one. So the second job only fires when the first job has successfully finished.
So I put two jobs into a workflow/yaml file. First job for the pytest and the second job for the deployment. The pytest job must succeed and then the second job for deployment is fired.


##Github secrets:


I also didn’t want to get rid of the passphrase when using ssh to get into the server. So for the second job I made some secrets on github with my host, username and ssh key and passphrase. I needed those to ssh into my server. I used the action from appleboy/ssh-action to do this. This action uses secrets stored in my github.
Making the second job ssh into the server gave some problems at first. The error wasn’t entirely clear. It said it couldn’t authenticate and also that the ssh key was missing. It turned that I had put the wrong key in my secret, but it took a while before I found out what the problem was.


But now it all works. If I change for example the background color in the main.css on my pc and push it to github, it will run the tests and deploy it to the server. After the job is finished the background color on arisanninga.nl will have changed too. And if I make a test fail and try to push it, pytest job will fail, code will not be changed on github repo and nothing will be deployed.
