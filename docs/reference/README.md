---
reference = true
---

# Guides

## `app.route()`

a decorator that allows users not to change the main functions provided in the DIY feature, where users can freely change the parameters.

**Note** 
Params given are of type `str`

## `route_url()`

alternative way to routing, using this `route_url()` method, it allows whether the route is available or not.
if the route is available, a message will appear as follows :

```
Routes Already Exists
```

**Note**
Params given are of type `str`

## `response.text`

a function taken from a [webob](https://docs.pylonsproject.org/projects/webob/en/stable/api/response.html) library, which will respond to an object given by the user which will be converted into text.

**Note**
Params given are of type `str`

## Get Running in Windows

running DIY in Windows is very different when running on Linux or Mac, because the OS itself does not support `Gunicorn`, DIY provides a feature that can run in Windows just by typing the command :

```sh
python serve.py
```

where the command will run the `waitress` function on the `serve.py` file. 

:::tip
by default, DIY will run on localhost `:8080` but you can changed it at `serve.py` on the port section and localhost section.
:::



<Reference/>