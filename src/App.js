import React, { Component } from 'react';
import logo from './tf.png';
import './App.css';
import './lit.css';
import SavableCanvas from './SavableCanvas';
//import * as tf from '@tensorflow/tfjs';
import NavigationBar from './NavigationBar';
import Carousel from './Carousel'
import ReactTooltip from 'react-tooltip'
//import jsonModel from './tfjs_model/model.json'

//const hostIP = "'192.168.1.5:3000/src/tfjs_model/model.json'"
//const model = tf.loadModel('0.0.0.0:8000/tfjs_model/model.json');


// fetch('http://0.0.0.0:3000/src/tfjs_model/model.json')
//     .then(res => res.json())
//     .then(json => console.log(json));

class App extends Component {

  render() {
    //console.log(tf.version);
    
    var aboutText = "Utilizing the MNIST dataset, a neural network will be trained using machine learning principles to translate handwritten text into alphanumeric digits. The project will include the use of Python libraries such as Keras and TensorFlow to create, train, and refine a model that will perform this conversion at an acceptable success rate. We will also construct a front-end application that accepts user handwriting (via trackpad/mouse) within a browser, exports and feeds it to our model, and displays the recognized character(s)."
    return (
      <div className="App">
        <NavigationBar></NavigationBar>
        
        <header className="App-header">
          <h1>About Our Project</h1>
          <hr />
          <p id="Project-Summary">
            {aboutText}
            <br></br>
            <a
            className="App-link"
            href="https://github.com/bavrumov/HandwritingRecognition"
            target="_blank"
            rel="noopener noreferrer"
            >
              Check out our GitHub repository
            </a>
          </p>
          <br></br>
          
          <div id="learnMore">
            {"If you want to make something of your own, here's where we started!"}
          </div>

          <a
            className="App-link"
            href="https://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks/2499936#2499936"
            target="_blank"
            rel="noopener noreferrer"
          >
            A good explanation on weights and bias
          </a>

        </header>

        <div className="col-m-6-offset-1" id="Interactive-Canvas">
          <SavableCanvas initialize={true}></SavableCanvas>
        </div>
        
        <div className="centered">

          <ReactTooltip />
          <a href="#top">
            <img src={logo} data-tip="Back to top" className="App-logo" alt="logo" />
          </a>
          
          <div id="About-Us">
            <Carousel></Carousel>
          </div>
          
          <a href="#top">
            <img src={logo} data-tip={"Back to top"} className="App-logo" alt="logo" />
          </a>
          
        </div>
      </div>
    );
  }
}

export default App;