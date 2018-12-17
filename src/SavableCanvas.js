import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {LiterallyCanvasReactComponent, tools, ClearButton} from 'literallycanvas';
import {Button} from 'reactstrap'
//import * as tf from '@tensorflow/tfjs';

var clr =<ClearButton></ClearButton>;
var LC;

//An array that should be of size 1, this is a hack to store the imported model globally
//var models = [];

// eslint-disable-next-line
async function modelLoader() {
  //const model = await tf.loadModel('http://0.0.0.0:8000/src/tfjs_model/model.json');
  //const model = await tf.loadModel('https://github.com/bavrumov/HandwritingRecognition/blob/master/src/tfjs_model/model.json');
  //console.log(model);
  //models.push(model);


  // var request = new XMLHttpRequest();
  // request.open('GET', 'http://127.0.0.1:5000/', true);
  // request.onload = () => {
  //   var data = JSON.parse(this.response);

  //   if (request.status >= 200 && request.status < 400) {
  //     console.log(data);
  //   } else {
  //     console.log("Error");
  //   }
  // }

  // request.send();
}

export class SavableCanvas extends Component {
  static propTypes = {
    initialize : PropTypes.bool
  }
  
  clear = () => {
    //let clr = document.getElementsByClassName("lc-clear");
    // let clr = document.getElementsByTagName("canvas");
    
    // for (let i = 0; i<clr.length; i++){
    //   console.log(clr[i].style.cssText);
    //   clr[i].style.color="white";
    //   //console.log(clr[i]);
    // }
    // console.log("This is our clear button: Right now it prints out the delete button");
    // //clr.dispatchEvent(new Event('onClick'));
    //console.log(clr);
    //console.log(models[0]);
    window.location.reload();
  }

  submit = () => {
    console.log("Here is the image URL:");
    //console.log(document.getElementById("test").firstChild.firstChild.childNodes[1]);
    //console.log(document.getElementsByTagName("canvas")[0].toDataURL("image/png"));
    let image = document.getElementsByTagName("canvas")[1].toDataURL("image/png");
    //console.log(image);
    fetch('http://0.0.0.0:5000/random')
       .then(res => res.json())
       .then(json => document.getElementById("output").innerHTML=json);
  }
  
  componentDidMount() {
    document.getElementsByClassName("with-gui")[0].style.left = 0;
  }

  
  render() {
    //modelLoader();
    
    var size = {width: "420", height: "420"};
    LC = 
    <LiterallyCanvasReactComponent
      imageURLPrefix = "./static/canvas/"
      keyboardShortcuts = "false"
      backgroundColor = "white"
      imageSize = {size}
      onInit = {(lc) => {if (this.props.initialize===true) console.log("initialized with", lc.canvas.attributes);}}
      strokeWidths = {[65]}
      tools = {[tools.Pencil]}
      toolbarPosition = "hidden"
      defaultStrokeWidth = {65}
    >
    {clr}
    </LiterallyCanvasReactComponent>;

    return (
      <div id="test">
        {LC}
        <div>
          <Button onClick={this.clear} className="canvasButtons" id="clearButton" color="danger">Clear Letter</Button>
          <Button onClick={this.submit} className="canvasButtons" id="submitButton" color="success">Submit Letter</Button>
        </div>
        <h2 id="output">Click "Submit Letter" to get a prediction here.</h2>
      </div>
    )
  }
}

export default SavableCanvas
