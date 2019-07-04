---
how-to = true
---

# How-to-Guides

Much more documented as well as take a fundamental level to getting started into **DIY** Framework based on [guide](/reference/).

---

## Define your application

The first things to do is settings up your application, what name will our application be given.
It is highly recommended to give the appropriate name based on guide, here's take a look

```python
app = # pass the class from your api
```

or you can also freely give his name

```python
main = # pass the class
```

## Give the response object

we can create a respond to objects in the functions that we make and the result given will depend on what class you are calling based on the `api`. As in the following example

```python
# function to create a hello world
def post(request, response):
    response.text = "Hello World"
```

:::tip
You can also abbreviate syntax `request` and `response` to `req` and `resp`
:::

## Customize port

You can also change the default port and host by changing the `serve.py` file in the following section like this

```python
serve(app.app, host='', port=8000)
```

## Running in `gunicorn`

if you use the `Gunicorn` server, all you need to note is that when you run the server it must match the name of the application that you initialized. For example, if your name application is `app` then your file name must be `app.py`. if your name application is missmatch with file name, server will not run because there is no match.

```
gunicorn <your_file_name>:<your_application_name>
```

Here's the example

```sh
gunicorn main:main
```



<Guide/>