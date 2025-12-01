# Virtual Env for project build
## commands
1. conda create -n helmet python=3.9 -y
[-y means yes permission, it will execute in the place where anaconda is installed. It will download only the required version files. helmet is the env name. we can put any name but not any build-ins.]

2. conda activate helmet
[use for switching the env. We can activate this for any folder.]

3. conda env list
[our create env that is existed]

4. conda deactivate
[switch back to (default) base]

5. pip install pandas==2.3.2
[manually install required lib from pypi.org]

6. pip list
[to show installed lib]

7. conda remove --name helmet --all
[firstly deactivate the env then execute or manually delete the folder from the location]

8. conda create --prefix .\helmet python=3.9 -y
[open cmd in the specific loc where we want to install our env. It will only take the space on the specific path not in C drive.]

9. conda activate .\helmet

10. python
[to see the version]

11. requirements.txt
[very important part for project building. While handover a project, it will install all the necessary lib and its version by exacuting the command from this file only.]

12. pip install -r requirements.txt
[to install all the lib from requirements.txt in one go. Here -r means read line by line. If a certain lib don't have the version mentioned, it will by default install the latest version]

[we can also use 'uv' instead of 'pip' for installing the lib]