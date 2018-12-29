var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('/Users/Gagan/trendstock_data/trendstock.db');
 
db.serialize(function() {
 
  db.all('SELECT symbol symbol, open open FROM stocks_raw where symbol = ?', ['PIH'], (err, results) => {
    if(err)
    {
        throw err;
    }
    results.forEach((row) => {
        console.log("Record: " + row.symbol + " : " + row.open);
    });

  });
});
 
db.close();