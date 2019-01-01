import React, { Component } from 'react';
import './App.css';
import StockList from "./StockList";

class App extends Component {

  render() {
    return (
        <div className="div">
            <StockList />
        </div>
        );
      }
  }
export default App;