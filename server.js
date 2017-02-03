var express = require('express')
  , logger = require('morgan')
  , app = express()
  , path = require('path')
  , dashboard = require('jade').compileFile(__dirname + '/source/templates/dashboard.jade')



app.use(logger('dev'))
app.use(express.static(__dirname + '/static'))
app.use(express.static(__dirname + '/bower_components'))

app.get('/', function (req, res, next) {
  try {
    var html = dashboard({ title: 'Dashboard' })
    res.send(html)
  } catch (e) {
    next(e)
  }
})

app.listen(process.env.PORT || 3000, function () {
  console.log('Listening on http://localhost:' + (process.env.PORT || 3000))
})