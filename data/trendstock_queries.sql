
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


CREATE TABLE "COMPANY_LIST" (
  `SYMBOL`               TEXT    NOT NULL UNIQUE,
  `NAME`                 TEXT,
  `EXCHANGE_NAME`        TEXT,
  `PRICE_2017_05_27`     NUMERIC,
  `MARKETCAP_2017_05_27` NUMERIC,
  `IPOYEAR`              INTEGER,
  `SECTOR`               TEXT,
  `INDUSTRY`             TEXT,
  `SUMMARY_QUOTE`        TEXT,
  `ROW_ID`               INTEGER NOT NULL UNIQUE,
  PRIMARY KEY (`ROW_ID`)
);

CREATE TABLE `companylist` (
  `Symbol`,
  `Name`,
  `EXCHANGE_NAME`,
  `LastSale`,
  `MarketCap`,
  `IPOyear`,
  `Sector`,
  `Industry`,
  `SummaryQuote`,
  `field10`
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
);

CREATE TABLE "stocks_raw1" (
  `timestamp`       DATE,
  `open`            NUMERIC,
  `high`            NUMERIC,
  `low`             NUMERIC,
  `close`           NUMERIC,
  `adjusted_close`  NUMERIC,
  `volume`          NUMERIC,
  `dividend_amount` NUMERIC
);