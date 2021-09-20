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

io.on('connection', (socket) => {

    // temp join some room and print each room available
    socket.join('some room');
    var counter = 0;

    socket.rooms.forEach(r => {
        if (counter > 0)    
            console.log(r);
        counter += 1;
    });

    app.get('/rooms', (req, res) => {
        //var room_data = socket.rooms;
        //res.render('rooms.ejs');

        //var roomData = "roomData";
        res.render('rooms.ejs', {"roomData": socket.rooms});
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
