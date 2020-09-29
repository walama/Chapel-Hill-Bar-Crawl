var express = require('express');
var app = express();
var mysql = require('mysql');
const port = 3000;

var connection = mysql.createConnection({
    host        :'localhost',
    user        :'root',
    password    :'hasanyoneseenmomar',
    database    :'bar_crawl'
});

app.set("view engine", "ejs");
app.use(express.static(__dirname + "/public"));
 
app.get("/", function(req, res){
    var q = 'SELECT bar, id FROM bars ORDER BY bar';
    connection.query(q, function (error, results) {
        if (error) throw error;
        var count =  results.length;
        var bars = [];
        var bar_ids = [];
        for (let i = 0; i < results.length; i++) {
            bars.push(results[i].bar);
            bar_ids.push(results[i].id);
        }
        res.render("index", {count: count, bars: bars, ids: bar_ids});
    }); 
});

app.get("/bar/:id", function(req, res){
    var q = 'SELECT drink, drinks.id AS id, vibes, drink_type, ounces, price, apv, bar, comments, ((ounces * (apv/100)) /price) AS deal FROM bars' +
    ' JOIN drinks' +
    ' ON bar_id = bars.id AND bar_id =' + req.params.id +
    ' ORDER BY deal DESC;';
    connection.query(q, function (error, results) {
        if (error) throw error;
        console.log(results);
        res.render("bar", {data: results})
    });
});

app.get("/drink/:id", function(req, res){
    var q = 'SELECT bar, bar_id, drink_type, price, ounces, (100*price)/(ounces*apv) AS ppo, drink FROM drinks'+
            ' JOIN bars'+
            ' ON drinks.drink = (SELECT drink FROM drinks WHERE id = ' + req.params.id+
            ') AND bar_id = bars.id'+
            ' ORDER BY ppo;';
    connection.query(q, function (error, results) {
        if (error) throw error;
        console.log(results);
        res.render("drink", {data: results})
    }); 
});

app.get("/type/:drink_type", function(req, res){
    var q = 'SELECT bar, bar_id, drink_type, price, ounces, (100*price)/(apv*ounces) AS ppo, drink FROM drinks'+
            ' JOIN bars'+
            ' ON drinks.drink_type =  "' + req.params.drink_type+'" AND bar_id = bars.id'+
            ' ORDER BY ppo;';
    connection.query(q, function (error, results) {
        if (error) throw error;
        console.log(results);
        res.render("type", {data: results})
    }); 
});


 
app.listen(port, function () {
 console.log('App listening on port 3000');
});