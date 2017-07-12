# templating

templating is done using [`mustache.js`]. templates are compiled using the 
[`build` script].

## templates

templates live in the [`templates` directory]. create new templates here with
the `.mustache` extension.

to insert a value into the template, use the following syntax:

```
<p>{{ content }}</p>
```

then in [`data/data.json`], add a key that matches the identifier you put in
the template. using our previous example:

```
{
  "content": "hello! i am some content"
}
```

when compiled this will render:

```
<p>hello! i am some content</p>
```

## partials

partials live in the [`partials` directory]. create a new partial here with
the `.mustache` extension.

to include a partial in another template, use the following syntax:

```
{{> mypartial }}
```

then be sure to pass it to the [`build` script] by adding the following:

```
"scripts": {
  "build": "mustache -p ./templates/mypartial.mustache ./data/data.json ./templates/index.mustache > ./index.html"
}
```

note: the current script already passes partials to the script. make sure
not to remove those! you can add your new partial at any point in the script,
the order doesn't matter so long as it appears before the `./data/data.json`
portion.

⚠️ this will be refactored into a build script soon so it'll be less complicated

[`mustache.js`]: https://github.com/janl/mustache.js
[`build` script]: https://github.com/ashleygwilliams/rustbridge-www/blob/master/package.json#L8
[`templates` directory]: https://github.com/ashleygwilliams/rustbridge-www/tree/master/templates
[`data/data.json`]: https://github.com/ashleygwilliams/rustbridge-www/blob/master/data/data.json
[`partials` directory]: https://github.com/ashleygwilliams/rustbridge-www/tree/master/templates/partials
