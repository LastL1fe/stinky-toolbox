const http = require('http');
const port = 8000;

const server = http.createServer(function(req, res){
    res.writeHead(200, {'Content-Type':'text/html'});
    res.write('fuck me right in the ass');
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