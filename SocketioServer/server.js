const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const path = require('path');

app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

//app.get('/rooms', (req, res) => {
//    res.sendFile(__dirname + '/rooms.html');
//});

// create staticly named rooms
io.of("/").adapter.on("create-room", (room = 'test') => {
    console.log(`room ${room} was created`);
});

io.on('connection', (socket) => {


    app.get('/rooms', (req, res) => {
        var counter = 0;
        var rooms_arr = [];
        
        socket.rooms.forEach(r => {
            if (counter > 0)    
                rooms_arr.push(r);
            counter += 1;
        });

        res.render('rooms.ejs', {"roomData": rooms_arr});
    });

    // below 2 are websocket specific functions
    socket.on('chat message', (msg) => {
        console.log('message: ' + msg);
        io.emit('chat message', msg);
    });
    
    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
    
});


server.listen(3000, () => {
    console.log('listening on *:3000');
});
