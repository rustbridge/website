# rustbridge-www
[![Build Status](https://travis-ci.org/ashleygwilliams/rustbridge-www.svg?branch=master)](https://travis-ci.org/ashleygwilliams/rustbridge-www)
[![Greenkeeper badge](https://badges.greenkeeper.io/ashleygwilliams/rustbridge-www.svg)](https://greenkeeper.io/)

> the website for rustbridge

## prerequisites

this is a static site. it is built using a [node.js] workflow. you'll need
node.js and npm to build the site. to get these tools, follow 
[these instructions].

[node.js]: https://nodejs.org
[these instructions]: https://www.npmjs.com/get-npm

## up and running

once you have node.js and npm installed, follow these steps to get the site
up and running locally:

1. fork and clone this repository
2. `cd rustbridge-www`
3. `npm prune && npm install`
4. `npm start`

`npm start` will start a local dev server at [`http://127.0.0.1:8080`].
this script uses [`live server`] to automatically refresh your browser
window when changes are made to files in the project.

[`http://127.0.0.1:8080`]: http://127.0.0.1:8080
[`live server`]: https://github.com/tapio/live-server

## templating

templating is done using [`mustache.js`]. templates are compiled using the 
[`build` script].

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

### partials

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
