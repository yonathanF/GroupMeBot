# GroupMe Bot for Scheduling 

### Basics 
The basic idea of the project is to create a bot for groupme that lets people in a group setup meeting times. It will ask each person in the group what day/time he/she can meet on, then use a simple algo to find a good meeting time for everyone. 

### Setup
1. Make sure you have pip (check version, current version is 9.0) 
```python 
pip -V 
```

2. Install all packages
```python 
pip install -r requirements.txt
```

### Documentation 
- Follow the PEP 8 standard when documenting your code 
- Look for a python linting plugin/lib for your IDE/system 
- Leave commit messages with helpful messages. Try to do a single subject line, followed by more descripiton
- Push to the right branch. Master is already locked so you need to do a pull request before merging into master
	- Try to stick to the Git Workflow [Details here](https://www.atlassian.com/git/tutorials/comparing-workflows)

### Testing 
- Write good unit test cases, and cover at least the happy path
- We have [Coverage.py](https://coverage.readthedocs.io/en/coverage-4.5.1/) for line coverage (shoot for 80% or so). The master branch will probably start rejecting anything below 80% 
- Use the standard python Unittest 
- Write your unit tests in the correct ```test.py``` file under the correct app

### Helpful commands 
- Running tests [go the right folder first] 
```python
python -m unittest test
```
- Running coverage (see coverage of the repair folder for example)
```python 
coverage run --source=source_py_file -m unittest test 
```

- Then use this to generate the html and view the report in your browser 
```python
coverage html
```

- To get style suggestions etc (if your IDE doesn't have a plugin)
```python 
pep8 python_file.py
```

- To update all your branches 
```
git pull --all 
```

- To see your branches 
```
git branch
```


