# rustbridge-www
[![Build Status](https://travis-ci.org/rustbridge/rustbridge.github.io.svg?branch=master)](https://travis-ci.org/rustbridge/rustbridge.github.io)
[![Greenkeeper badge](https://badges.greenkeeper.io/rustbridge/rustbridge.github.io.svg)](https://greenkeeper.io/)

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

## documentation

for more information about the specific workflows and builds in this project
checkout out the [`documentation` directory]:

- [templating]
- [deploy]

[`documentation` directory]: https://github.com/ashleygwilliams/rustbridge-www/tree/master/docs
[templating]: https://github.com/ashleygwilliams/rustbridge-www/tree/master/docs/templating.md
[deploy]: https://github.com/ashleygwilliams/rustbridge-www/blob/master/docs/deploy.md
