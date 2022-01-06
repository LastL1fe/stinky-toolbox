const http = require('http');
const express = require('express')

const port = 8000;

const server = http.createServer(function(req, res){
    console.log(`request was made from: ${req.socket.remoteAddress}`)
    res.writeHead(200, {'Content-Type':'text/html'});
    //res.write('fuck me right in the ass');
    res.write('ding dong i have your ip address now smiley face :)')
    res.end();
})

server.listen(port, function(error){
    if (error){
        console.log("cannot start, reason: " + error);
        server.close();
    } else{
        console.log(`eating ass on port ${port}`);
    }
})