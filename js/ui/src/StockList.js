import React, { Component } from 'react';
import './App.css';
import Data from "./data/data.json";

import axios from 'axios';

class StockList extends Component {
  state = {
        stocks: []
  };

  componentDidMount() {
    axios.get(`http://localhost:5000/list`)
      .then(res => {
        console.log(res.data)
        this.setState({stocks: JSON.parse(res.data)});
      });
  }

  render() {
    return (
      <div class="ui container">
        <div class="ui huge header striped center aligned">Stocks</div>
          <table key="stocklist" class="ui celled striped table">
            <thead>
              <tr>
                <th>Ticker</th>
                <th>Company Name</th>
                <th>Sector</th>
                <th>Industry</th>
                <th>Avg Mkt Cap</th>
                <th>Min Stock Price</th>
                <th>Max Stock Price</th>
                <th>Avg Stock Price</th>
                <th>Avg Volume</th>
              </tr>
            </thead>
            <tbody>
              {
                this.state.stocks.map(stock => (
                <tr>
                  <td>{stock.symbol}</td>
                  <td>{stock.name}</td>
                  <td>{stock.sector}</td>
                  <td>{stock.industry}</td>
                  <td>{stock.avg_market_cap}</td>
                  <td>{stock.min_stock_price}</td>
                  <td>{stock.max_stock_price}</td>
                  <td>{stock.avg_stock_price}</td>
                  <td>{stock.avg_volume}</td>
                </tr>
                )
              )}
              </tbody>
            </table>
        </div>
      );
    }
  }

export default StockList;