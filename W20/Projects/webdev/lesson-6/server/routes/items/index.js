const express = require('express')
const items = express.Router()

const { Item, TYPES } = require('./../../models/item')
const FILTERS = ['Current', 'Completed', 'Suggested' ]


items.get('/meta', function (_, res) {
    res.send({
        types: TYPES,
        filters: FILTERS
    })
})

// GET /items
items.get('/', function(_, res) {
    Item.find().then(function(items) {
        res.send(items)
    })
})


// GET /items/:id
items.get('/:id', function(req, res) {
    const id = req.params.id

    if (id != null) {
        Item.findById(id).then(function(item) {
            if (item != null) {
                res.send(item)
            } else {
                res.status(404).send({
                    message: 'item not found'
                })
            }
        }).catch(function(e) {
            console.log(e)
            res.status(500).send({
                message: 'something went wrong'
            })
        })
    } else {
        res.status(400).send({
            message: 'please provide `id`'
        })
    }    
})

const getTypeFilterQuery = function (type, filter) {
    if (FILTERS[0] == filter) { // current
        return {
            completed: false,
            type: type
        }
    } else if (FILTERS[1] == filter) { //completed
        return {
            completed: true,
            type: type
        }
    } else {
        return { // default
            type: type
        }
    }
}

items.get('/:type/:filter', function(req, res) {
    const type = req.params.type
    const filter = req.params.filter

    if (type != null && filter != null) {
        if (TYPES.includes(type) && FILTERS.includes(filter)) {
            const query = getTypeFilterQuery(type, filter)
            Item.find(query).then(function(items) {
                res.send(items)
            }).catch(function(e) {
                console.log(e)
                res.status(500).send({
                    message: 'something went wrong'
                })
            })
        } else {
            res.status(400).send({
                message: 'please provide a valid `type` and `filter`'
            })
        }
    } else {
        res.status(400).send({
            message: 'please provide `type` and `filter`'
        })
    }
})

// then: happy paths
// catch: unhappy paths

items.post('/', function(req, res) {
    const { name, type } = req.body

    if (name != null && type != null && TYPES.includes(type)){
        const item = new Item({
            name,
            type,
            completed: false,
            createdAt: Date.now()
        })
    
        item.save().then(function(item) {
            res.send(item)
        }).catch(function(e) {
            console.log(e)
            res.status(500).send({
                message: 'something went wrong'
            })
        })
    } else {
        res.status(400).send({
            message: 'please provide `type` and `name`'
        })
    }
})


items.delete('/:id', function(req, res) {
    const { id } = req.params

    if (id != null) {
        Item.findByIdAndDelete(id).then(function(item) {
            if (item != null) {
                res.send(item)
            } else {
                res.status(404).send({
                    message: 'item not found'
                })
            }
        }).catch(function(e) {
            console.log(e)
            res.status(500).send({
                message: 'something went wrong'
            })
        })
    } else {
        es.status(400).send({
            message: 'please provide `id`'
        })
    }
})

const createUpdateQuery = function (name, type, completed) {
	const updateQuery = {
        completed
    }

    if (name) updateQuery.name = name
    if (type) updateQuery.type = type

	return updateQuery
}

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
