# deploy

this project uses [Travis] to deploy a static site to [GitHub pages].

when a PR is merged, Travis runs [`deploy.sh`], which runs the
[`build` script] and  then pushes the repo and newly built files to
the [`gh-pages` branch].

## generated files

built files (any file that is generated) should always be generated
via the [`build` script] and should not be commited to the
[`master` branch].

[Travis]: https://travis-ci.org/
[GitHub pages]: https://pages.github.com/
[`build` script]: https://github.com/ashleygwilliams/rustbridge-www/blob/master/package.json#L8
[`deploy.sh`]: https://github.com/ashleygwilliams/rustbridge-www/blob/master/deploy.sh
[`gh-pages` branch]: https://github.com/ashleygwilliams/rustbridge-www/tree/gh-pages
[`master` branch]: https://github.com/ashleygwilliams/rustbridge-www
