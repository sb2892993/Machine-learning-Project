# Machine-learning-Project
This is first ML Project
Application url:
[HousingPredictor](https://ml-regression-app.herokuapp.com/)

## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

================================
create reporistory with some project folder name & apache some licence and then follow below steps: 


`clone git to local vs code to work: 

``GIT clone <copy link from code on github>

$ ls  -- to see whether Machine learning folder is created or not the name that we gave for project in reporistory git.

change the directory :  cd  Machinelearning project/

now it'll be in the ML Directory folder

==================================

now to open vs code from ml FOLDER itself ,we need to enter  -- code .  in terminal .
in mac if it doesnt work first install code path from vs code below r the steps:

When you type:
code .
and get:
zsh: command not found: code
…it means VS Code’s command-line tool isn’t installed in your shell path yet.
✅ Fix — Add “code” command to your PATH
Option 1 — (Recommended) Enable from inside VS Code
Open Visual Studio Code manually (from Applications or Spotlight).
Press Cmd + Shift + P to open the Command Palette.
Type:
Shell Command: Install 'code' command in PATH
Hit Enter — it’ll show:
Shell command 'code' successfully installed in PATH.
Close VS Code and Terminal, then reopen Terminal.
Now go to your ML folder and try again:
cd ~/ml
code .
✅ It should now open VS Code from that folder.
Option 2 — (If Option 1 doesn’t appear)
Add it manually:
Find where VS Code is installed: 
ls /Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin
(You should see a file named code.)
Add it to your PATH permanently:
echo 'export PATH="/Applications/Visual Studio Code.app/Contents/Resources/app/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
Test it:
code --version
If it prints a version number → success


=================================
check git VERSION : 
GIT  --version

er can install git on our system or else can work from browser.

=====================
create a folder inside the ML folder internally on localdisk.
open terminal by right click - terminal and then set the 
--  $pwd

now clone the git data into that folder by again clicking on 
-- GIT Clone <link from reporitory>

============================
Creating conda environment:
==> -P MEANS IN THE SAME FOLDER WHERE WE CREATED THE PROJECT FOLDER INSIDE.
==>-N MEANS IT WILL CREATE WHERE THE ANACONDA IS INSTALLED.
conda create -p venv python==3.7 -y
```


```To activate conda:
conda activate venv/
```
OR 
```
conda activate venv
```


```to install FLASK
pip install -r requirements.txt  
```

=================>To create a flask application =========
create app.py => Then code 

From flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET','POST])
def index():
return "Starting ML Project"

if __name__ = "__main__"
app.run(debug=True)

==============================================


To Add files to git
```
git add .  (to add all the files at once)
```

OR
```
git add <file_name>

we can also add multiple git files, we can(one by one add manually)
git add file1 file2 filen
```
==============================================
> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file
==============================================
To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```
=====================================================
To setup CI/CD pipeline in heroku we need 3 information

step 1 = created the app and sent to git 
step 2 = from git need to connect to heroku for deployemnet
need heroku app .and need to create DOCKER which is needed for Heroku.

1. HEROKU_EMAIL = anishyadav7045075175@gmail.com

2. HEROKU_API_KEY = <>  
- on heroku app its found

3. HEROKU_APP_NAME = ml-regression-app

===============================================
now,
DOCKER: 
CREATE docker folder in the vscode where we created everything.
write these lines :

for docker image creation we need all these:

FROM Python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

================================================

BUILD DOCKER IMAGE

docker build -t <image_name>:<tagname> . 
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift



## Write a function to get training file path from artifact dir