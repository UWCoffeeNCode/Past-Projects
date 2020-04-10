const createUpdateQuery = function(name, type, completed) {
    const updateQuery = {
        completed: completed
    }
    if (name != null) {
        updateQuery.name = name
    }
    if (type != null) {
        updateQuery.type = type
    }
    return updateQuery
}

const createQuery = function (type, filter) {
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

module.exports = { 
    createUpdateQuery, 
    createQuery
}