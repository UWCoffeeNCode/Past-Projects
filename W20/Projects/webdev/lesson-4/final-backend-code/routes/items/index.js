const express = require('express')
const items = express.Router()

const { Item, TYPES } = require('./../../models/item')
const { createQuery, createUpdateQuery } = require('./../../utils/routes/items')

const FILTERS = ['current', 'completed', 'suggested']

items.get('/', function (req, res) {
    Item.find().then(function(items) {
        res.send(items)
    })
    .catch(function() {
        res.status(500).send({ // 500: Internal Server Error
            message: 'something went wrong'
        })
    })
})

items.get('/:id', function (req, res) {
    const id = req.params.id

    if (id != null) {
        Item.findById(id).then(function(item) {
            if (item != null) {
                res.send(item)
            } else {
                res.status(404).send({ // 404: Not Found
                    message: 'no item found'
                })
            }
        })
    } else {
        res.status(400).send({ // 400: Bad Request
            message: 'please provide `id` as a param'
        })
    }
})

items.get('/:type/:filter', function (req, res) {
    const type = req.params.type
    const filter = req.params.filter

    if (type != null && filter != null) {
        if (TYPES.includes(type) && FILTERS.includes(filter)) {
            const query = createQuery(type, filter)

            Item.find(query).then(function (items) {
                res.send(items)
            })
        } else {
            res.send({
                message: 'please provide a valid `type` and `filter`'
            })
        }
    } else {
        res.send({
            message: 'please provide `type` and `filter` as params'
        })
    }
})

items.get('/meta', function (req, res) {
    res.send({
	types: TYPES,
	filters: FILTERS
    })
})

items.post('/', function(req, res) {
    const name = req.body.name
    const type = req.body.type

    if (name != null && type != null && TYPES.includes(type)) {
        const item = new Item({
            name,
            type,
            completed: false,
            addedAt: Date.now()
        })

        item.save().then(function() {
            res.send(item)
        })
        .catch(function(e) {
            console.log(e)
            res.status(500).send({
                message: 'something went wrong'
            })
        })
    } else {
        res.status(400).send({
            message: 'please provide `title` and `type`'
        })
    }
})

items.delete('/:id', function(req, res) {
    const id = req.params.id

    if (id != null) {
        Item.findByIdAndDelete(id).then(function(item) {
            if (item != null) {
                res.send(item)
            } else {
                res.status(404).send({
                    message: 'no item found'
                })
            }
        })
        .catch(function(e) {
            console.log(e)
            res.status(500).send({
                message: 'something went wrong'
            })
        })
    } else {
        res.status(400).send({
            message: 'please provide `id` as a param'
        })
    }
})

items.patch('/:id', function (req, res) {
    const { id } = req.params
    const { name, type, completed } = req.body

    if (id != null) {
        const updateQuery = createUpdateQuery(name, type, completed)
        Item.findByIdAndUpdate(
            id,
            { $set: updateQuery },
            { new: true }
        )
        .then(function(item) {
            if (item != null) {
                res.send(item)
            } else {
                res.status(404).send({
                    message: 'no item found'
                })
            }
        })
        .catch(function(e) {
            console.log(e)
            res.status(500).send({
                message: 'something went wrong'
            })
        })
    } else {
        res.status(400).send({
            message: 'please provide `id` as a param'
        })
    }
})

module.exports = items
