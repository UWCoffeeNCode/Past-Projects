const express = require('express')
const items = require('./items')

const api = express.Router()

api.use('/items', items)

api.get('/ping', function(request, response) {
    response.json({
        message: 'pong'
    })
})

module.exports = api