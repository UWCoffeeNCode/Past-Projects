const express = require('express')
const items = express.Router()

let id = 1
const itemsArr = [{
    title: 'Spider-Man: Homecoming',
    completed: false,
    type: 'Movie',
    createdAt: Date.now(),
    id: id
}]

// GET /items
items.get('/', function(request, response) {
    response.json(itemsArr)
})

items.post('/', function(request, response) {
    const title = request.body.title
    const type = request.body.type

    const item = {
        title: title,
        type: type,
        completed: false,
        createdAt: Date.now(),
        id: id + 1
    }

    itemsArr.push(item)
    response.json(item)
    id = id + 1
})

items.get('/:id', function(request, response) {
    const id = request.params.id
    console.log(id)

    for (let i = 0; i < itemsArr.length; i = i + 1) {
        const item = itemsArr[i]
        if (item.id == id) {
            response.json(item)
            return
        }
    }

    response.status(404).json({})
})

items.delete('/:id', function(request, response) {
    const id = request.params.id

    for (let i = 0; i < itemsArr.length; i = i + 1) {
        const item = itemsArr[i]
        if (item.id == id) {
            itemsArr.splice(i, 1)
            response.json(item)
            return
        }
    }

    response.status(404).json({})
})

// patch
// 1. find an item by id.
// 2. if the item matches the provided id ->
// 3. modify provided type, and/or title
// 4. return updated item via response
// 5. update the item in the array


module.exports = items