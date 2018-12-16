import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {LiterallyCanvasReactComponent, tools, ClearButton} from 'literallycanvas';
import {Button} from 'reactstrap'
// import { BrowserDownloads } from '@tensorflow/tfjs-core/dist/io/browser_files';

var clr =<ClearButton></ClearButton>;
var LC;

export class SavableCanvas extends Component {
  static propTypes = {
    initialize : PropTypes.bool,
  }
  
  clear = () => {
    //let clr = document.getElementsByClassName("lc-clear");
    console.log("This is our clear button:")
    console.log(clr);
  }

  submit = () => {
    console.log("TensorFlow is going to take the following canvas as a parameter:");
    console.log(document.getElementById("test").firstChild.firstChild.childNodes[1]);
    //console.log(document.getElementsByClassName("lc-drawing")[0]);
  }
  
  componentDidMount() {
    document.getElementsByClassName("with-gui")[0].style.left=0;
  }

  render() {
    console.log(this.props.initialize);
    var size = {width: "420", height: "420"};
    LC = 
    <LiterallyCanvasReactComponent
      imageURLPrefix = "./static/canvas/"
      keyboardShortcuts = "false"
      backgroundColor = "white"
      imageSize = {size}
      onInit = {(lc) => {console.log("initialized with", lc);}}
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
      </div>
    )
  }
}

export default SavableCanvas
