
# Query to get 90 day trends.
select c.symbol, c.name, c.sector, c.industry,
round(avg(c.market_cap)) avg_market_cap, min(s.adjusted_close) min_stock_price,
max(s.adjusted_close) max_stock_price, round(avg(s.adjusted_close), 2) avg_stock_price,
round(avg(s.volume)) avg_volume
from company_list c, stocks_raw s
where c.symbol = s.symbol and
	s.timestamp > date('now', '-90 days')
group by c.symbol, c.name, c.sector, c.industry
order by c.symbol;


CREATE TABLE "company_list" (
  `symbol`        TEXT NOT NULL UNIQUE,
  `name`          TEXT,
  `exchange_name` TEXT,
  `stock_price`   NUMERIC,
  `market_cap`    NUMERIC,
  `ipo_year`      INTEGER,
  `sector`        TEXT,
  `industry`      TEXT,
  `summary_quote` TEXT,
  PRIMARY KEY (`symbol`)
);


CREATE TABLE "stocks_raw" (
  `symbol`          TEXT,
  `timestamp`       DATETIME,
  `open`            NUMERIC,
  `high`            NUMERIC,
  `low`             NUMERIC,
  `close`           NUMERIC,
  `adjusted_close`  NUMERIC,
  `volume`          NUMERIC,
  `dividend_amount` NUMERIC,
  `load_timestamp`  DATETIME,
  PRIMARY KEY (`symbol`, `timestamp`)
)