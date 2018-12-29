const express = require('express');

const app = express();

const sql = 'select c.symbol, c.name, c.sector, c.industry, \
round(avg(c.market_cap)) avg_market_cap, min(s.adjusted_close) min_stock_price, \
max(s.adjusted_close) max_stock_price, round(avg(s.adjusted_close), 2) avg_stock_price, \
round(avg(s.volume)) avg_volume \
from company_list c, stocks_raw s \
where c.symbol = s.symbol and \
    s.timestamp > date(\'now\', \'-90 days\') \
group by c.symbol, c.name, c.sector, c.industry \
order by c.symbol;'

app.use("/list", (req, res, next) => {
    var sqlite3 = require('sqlite3').verbose();
    var db = new sqlite3.Database('/Users/Gagan/trendstock_data/trendstock.db');

    db.serialize(function() {
        
        db.all(sql, (err, results) => {
          if(err)
          {
              res.json({
                errors: ['Failed to fetch stocks data: ' + err]
              });
              throw err;
          }
          res.setHeader('Content-Type','application/json')
          res.json(JSON.stringify(results));
        });

      });

      db.close();
});

module.exports = app;