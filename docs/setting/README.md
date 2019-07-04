---
setting = True
---

# Miscellaneous

## Get Running in Windows

running DIY in Windows is very different when running on Linux or Mac, because the OS itself does not support `Gunicorn`, DIY provides a feature that can run in Windows just by typing the command :

```sh
python serve.py
```

where the command will run the `waitress` function on the `serve.py` file. 

:::tip
by default, DIY will run on localhost `:8080` but you can changed it at `serve.py` on the port section and localhost section.
:::

## Project structure

for now, the new project settings can only be done by doing it in the same root directory (`diy` directory). That is, if you want to try creating a new project, make sure the file to be executed is in the root directory. This is because DIY still hasn't been packaged and published officially through the python index *(please be patient)*.

you only need to use the function available on `api.py` then import the function into your program like these :

```python
# your main program, example `main.py`
from api import UserRequestHandler
```

for `serve.py` file is an optional file if you are using a Windows operating system, but the file **must be** in conjunction with your program

## Alternative project structure <Badge text="Advanced" type="danger"/>

or if you are already familiar with the python environment, you can put your program outside the DIY root directory with the following options :

```python
# your main program but it's outside the root directory
from diy.api import UserRequestHandler
```

<Setting/>