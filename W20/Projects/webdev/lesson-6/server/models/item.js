const mongoose = require('./../db/mongoose')
const TYPES = ['Movies', 'TV Shows', 'Video Games', 'Books']

const ItemSchema = mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    completed: {
        type: Boolean,
        required: true
    },
    type: {
        type: String,
        enum: TYPES,
        required: true
    },
    createdAt: { 
        type: Date,
        required: true
    }
})

const Item = mongoose.model('Item', ItemSchema)
module.exports = { Item, TYPES }