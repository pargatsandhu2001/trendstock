import React, { Component } from 'react';
import './App.css';
import StockList from "./StockList";
import Test from "./Test";

class App extends Component {

  render() {
    return (
        <div class="ui container">
            <StockList />
        </div>
        );
      }
  }
export default App;