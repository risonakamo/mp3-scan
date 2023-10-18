mp3 dir scan program for helping with reviewing mp3s in a dir

# setup
1. activate env with python 3.10+
2. `poetry install`

# usage
1. edit `mp3_scan.py`
2. set `targetDir` to folder with your mp3s
3. run the program
4. check the parent folders output to make sure all the parent folders are readable
5. check the csv output. copy into google sheets and use that for determining mp3 review order

# mp3 folder structure requirements
your mp3 folder must be full of folders, and each mp3 file within these folders must be under a folder that has an easy to find name