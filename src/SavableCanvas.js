import React, { Component } from 'react';
import PropTypes from 'prop-types';
import {LiterallyCanvasReactComponent, tools, ClearButton} from 'literallycanvas';

export class SavableCanvas extends Component {
  static propTypes = {
    initialize : PropTypes.bool,
  }
  
  render() {
    //var lc = LiterallyCanvasReactComponent.init({getElementById("test")}, {imageSize: {width: 300, height: 300}})
    console.log(this.props.initialize);
    var size = {width: "420", height: "420"};
    return (
      <div id="test">
        <LiterallyCanvasReactComponent
          
          imageURLPrefix = "./static/canvas/"
          keyboardShortcuts = "false"
          backgroundColor = "white"
          imageSize = {size}
          onInit = {(lc) => {console.log("initialized with", lc);}}
          strokeWidths = {[30]}
          tools = {[tools.Pencil]}
          toolbarPosition = "bottom"
          
        >
        <ClearButton></ClearButton>
        </LiterallyCanvasReactComponent>
        
      </div>
    )
  }
}

export default SavableCanvas
