import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {LiterallyCanvasReactComponent, tools, ClearButton} from 'literallycanvas';
import {Button} from 'reactstrap'

var clr =<ClearButton></ClearButton>;

export class SavableCanvas extends Component {
  static propTypes = {
    initialize : PropTypes.bool,
  }
  
  clear = () => {
    clr.click();
    console.log(clr);
  }
  

  render() {
    //var lc = LiterallyCanvasReactComponent.init({getElementById("test")}, {imageSize: {width: 300, height: 300}})
    console.log(this.props.initialize);
    var size = {width: "420", height: "420"};
    var LC = 
    <LiterallyCanvasReactComponent
          
    imageURLPrefix = "./static/canvas/"
    keyboardShortcuts = "false"
    backgroundColor = "white"
    imageSize = {size}
    onInit = {(lc) => {console.log("initialized with", lc);}}
    strokeWidths = {[65]}
    tools = {[tools.Pencil]}
    toolbarPosition = "bottom"
    defaultStrokeWidth = {65}
  >
  {clr}
  </LiterallyCanvasReactComponent>;

    return (
      <div id="test">
        {LC}
        <div>
          <Button onClick={this.clear} className="canvasButtons" id="clearButton" color="danger">Clear Letter</Button>
          <Button className="canvasButtons" id="submitButton" color="success">Submit Letter</Button>
        </div>
      </div>
    )
  }
}

export default SavableCanvas
