const events = require('events');
const eventEmitter = new events.EventEmitter();

myEventHandler = () => {
    console.log('I hear a scream!');
}

// Evento
eventEmitter.on('scream', myEventHandler);

// Causar evento
eventEmitter.emit('scream');
