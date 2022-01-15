const express = require('express');
const app = require('ipware')().get_ip;
const axios = require('axios');
const ass = express(); //im contrarian
const port = 8000;

ass.use('/img', express.static(__dirname + '/img'));

ass.get("/", (req, res) => {
    let ip = app(req)
    console.log(ip)
    //console.log(req)
    res.send("This was a test of your intelligence and sense of security. If you're seeing this screen, then your IP address has already been stolen and logged. This shows just how easy and quick it is for criminals to steal your IP address, log it, and use it for nefarius reasons. (I don't save IP addresses. My web server simply records IP addresses and deletes them when it's refreshed.)");
    res.end()
});

ass.post("/img", (req, res) => {
    //nothing yet
});

ass.get("/img", (req, res) => {
    res.send("ye")
    console.log(req)
    res.end()
});

ass.listen(port, () => console.log(`eating ass on port ${port}`));