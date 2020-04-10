const mongoose = require('./../db/mongoose')

const TYPES = ['Movies', 'TV Shows', 'Video Games', 'Books']

const ItemSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    type: {
        type: String,
        required: true,
        enum: TYPES
    },
    completed: {
        type: Boolean,
        required: true
    },
    addedAt: {
        type: Date,
        required: true
    }
})

const Item = mongoose.model('Item', ItemSchema)
module.exports = { Item, TYPES }