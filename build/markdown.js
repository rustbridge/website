#!/usr/bin/env node
const fs = require('fs')
const path = require('path')

const md = require('markdown-it')()

if (process.argv.length < 3) {
  console.log('Usage:\n\nmarky-markdown some.md > some.html')
  process.exit()
}

const filePath = path.resolve(process.cwd(), process.argv[2])

fs.readFile(filePath, function (err, data) {
  if (err) throw err
  const html = md.render(data.toString())
  process.stdout.write(html)
})
