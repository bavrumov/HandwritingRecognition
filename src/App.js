import React, { Component } from 'react';
import logo from './tf.png';
import './App.css';
import './lit.css';
import SavableCanvas from './SavableCanvas';

class App extends Component {
  render() {
    return (
      <div className="App">
        <img src={logo} className="App-logo" alt="logo" />
        
        <header className="App-header">
          <p>
            Anything we want can go here. Anything about tensor, or a component that will let us draw and export an input.
          </p>
          
          <a
            className="App-link"
            href="https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks/2499936#2499936"
            target="_blank"
            rel="noopener noreferrer"
          >
            A good explanation on weights and bias
          </a>

        </header>

      {/* <div class="container-fluid">
        <div class="row"> */}
          <div className="col-m-6-offset-3" id="canvasContainer"><SavableCanvas initialize={true}></SavableCanvas></div>
        {/* </div>
      </div> */}
        
      </div>
    );
  }
}

export default App;
