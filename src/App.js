import React, { Component } from 'react';
import logo from './tf.png';
import './App.css';
import './lit.css';
import SavableCanvas from './SavableCanvas';
import * as tf from '@tensorflow/tfjs';
import NavigationBar from './NavigationBar';
import Carousel from './Carousel'
import { Button } from 'reactstrap';
import ReactTooltip from 'react-tooltip'

const model = tf.loadModel('./tfjs_model/model.json');

class App extends Component {
  
  render() {
    console.log(tf.version);
    console.log(model);
    var aboutText = "Utilizing the MNIST dataset, a neural network will be trained using machine learning principles to translate handwritten text into alphanumeric digits. The project will include the use of Python libraries such as Keras and TensorFlow to create, train, and refine a model that will perform this conversion at an acceptable success rate. We will also construct a front-end application that accepts user handwriting (via trackpad/mouse) within a browser, exports and feeds it to our model, and displays the recognized character(s)."
    return (
      <div className="App">
        <NavigationBar></NavigationBar>
       
      
        <header className="App-header">
          
          <p id="about">
            {aboutText}
          </p>
          
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

        <div className="col-m-6-offset-1" id="canvasContainer"><SavableCanvas initialize={true}></SavableCanvas></div>
          <br></br>
          
          <Button id="submitButton" color="success">Submit Letter</Button>

      <div id="carouselContainer"> <Carousel></Carousel></div>
      <br></br><br></br><br></br><br></br>
      
      <a href="#navi" ><img src={logo} data-tip="Back to top" className="App-logo" alt="logo" /></a>
      <ReactTooltip />
        {/* <button onClick={() => {console.log(model)}}>click</button> */}
      </div>
    );
  }
}

export default App;