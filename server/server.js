const express = require('express');
const app = require('ipware')().get_ip;
const busboy = require('connect-busboy');
const fs = require('fs');
const { exec } = require("child_process");
const path = require('path');
const ass = express(); //im contrarian
const port = 8000;

ass.use(busboy({immediate: true}))
ass.use('/img', express.static(__dirname + '/img'));
ass.use('/mural', express.static(__dirname + '/mural'));

ass.get("/", (req, res) => {
    const htmlPage = fs.createReadStream(__dirname + '/index.html');
    res.writeHead(200, {"Content-Type": "text/html"});
    htmlPage.pipe(res);
});

ass.post("/upload", (req, res) => {
    req.busboy.on('file', (name, file, info) => {
        const saveDir = __dirname + "/mural";
        file.pipe(fs.createWriteStream(path.join(saveDir, `/${name}.png`)));
        res.status(200).send("working")
    });
});

ass.get("/shutdown", (req, res) => {
    res.send("lol get your pc shutdown nerd");
    exec('restart /r /t 1');
    res.end();
});

ass.get("/upload", (req, res) => {    
    console.log("lmao this idiot got their ip address stolen: " + JSON.stringify(app(req)));
    res.send("this is a test");
    res.end();
});

ass.listen(port, () => console.log(`eating ass on port ${port}`));