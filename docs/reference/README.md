---
reference = true
---

# References

## `app`

- function that define your application what is to be named. This will be override `__call__` method in `api` and converted to a new simple class it depends on what class is you're called.

You can see the more explanation of each class below.

## `response.text`

- a function taken from a [webob](https://docs.pylonsproject.org/projects/webob/en/stable/api/response.html) library, which will respond to an object given by the user which will be converted into text.

## `app.route()`

- a decorator that allows users not to change the main functions provided in the DIY feature, where users can freely change the parameters.

## `route_url()` <Badge text="stable" type="warn"/>

- alternative way to routing, using this `route_url()` method, it allows whether the route is available or not.
if the route is available, a message will appear as follows :

```
Routes Already Exists
```

## `url()` <Badge text="beta" type="danger"/>

- alternative look for routing, make it simple whereas the function is similar to `route_url()`

## `API()`

- one of the classes of `api` which aims to provide a simple response in the form of text based, to a web browser.

## `RequestAPI()`

- one of the classes of `api` which aims to provide a simple response in the form of text based, to a web browser.

## `UserRequest()`

- one of the classes of `api` useful for getting information related to `user_agent`. See more [explanation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent).

## `UserRequestHandler()`

- one of the classes of `api`. Provides a function to give a response to an object and display it in the browser in the form of text based. Get an error when it fails to routing a function, and also provides dynamic routing.

## `UserRequestBasedHandler()` <Badge text="beta" type="danger"/>

- one of the classes of `api`. Provides a function to give a response to an object and display it in the browser in the form of text based. Get an error when it fails to routing a function, provides dynamic routing, and inspect whether the routing has been used or not. For advanced user, you can use the class based handlers when going to route. See [class based handlers](/index/)

## Params type

these are list of params type are given to each classes as follows :

| Class       | Parameters Type |
| ------------- |:-------------:|
| `app.route()`      | `string` |
| `route_url()`      | `string`      |
| `url()` | `string`     |
| `API()`      | `string` |
| `RequestAPI()`      | `string`      |
| `UserRequest()` | `string`     |
| `UserRequestHandler()`      | `string`, `*args`, and `**kwargs`      |
| `UserRequestBasedHandler()` | `string`,   `*args`, and `**kwargs`  |


<Reference/>