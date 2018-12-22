import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
//import malestock from './static/person-male.png'
import benjipic from './static/Team_Pics_4900/benji4900.png'
import benpic from './static/Team_Pics_4900/kats4900.png'
import vladPic from './static/Team_Pics_4900/vlad4900.png'
import borisPic from './static/Team_Pics_4900/boris4900.png'
import {Row, Col} from 'reactstrap'

const Ben= {
    name: 'Benjamin Kats',
    college: 'Brooklyn College Senior',
    github: 'github.com/benkats',
    email: 'katsbenjamin@gmail.com',
    linkedin: 'linkedin.com/in/benkats',
    pic: benpic
}

const Benji= {
    name: 'Benjamin Karasik',
    college: 'Brooklyn College Senior',
    github: 'youtube.com/bitunusual',
    email: 'Karasik.benjamin28@gmail.com ',
    linkedin: 'linkedin.com/in/benjamin-k-798a0687',
    pic: benjipic
}

const Boris= {
    name: 'Boris Avrumov',
    college: 'Brooklyn College Senior',
    github: 'bavrumov.github.io',
    email: 'bavrumov@hotmail.com ',
    linkedin: 'linkedin.com/in/bavrumov',
    pic: borisPic
}

const Vlad= {
    name: 'Vlad Borisov',
    college: 'Brooklyn College Senior',
    github: 'github.com/vladborisov',
    email: 'vladborisov.vbnyc@gmail.com ',
    linkedin: 'vladborisov.com',
    pic: vladPic
}

// const Prof={
//     name: 'Kletenik',
//     github: 'google.com',
//     pic: malestock
// }

var team = [Boris, Vlad, Benji, Ben]//, Prof];

export default class Carousel extends Component {
    createCarousel = () => {
        let elements = [];

        for(let i = 0; i<team.length; i++) {
             elements.push(
             <Col sm={12} md={6} lg={6} key={i}>
                <div style={{width:"100%"}}><img
                src={team[i].pic}
                alt={team[i].name}
                width="75%"
                />
                </div>
                 <h1>{team[i].name}</h1>
                 <h3><a className="App-link" href={"https://"+team[i].github}>{team[i].github}</a></h3>
                 <h5><a href={"https://www."+team[i].linkedin} style={{color:"goldenrod"}}>{team[i].linkedin}</a></h5>
                 <br></br><br></br>
              </Col>
             )
        }
        return elements;
    }
  
  render() {
    return (
      <div className="container">
        <Row>
          {this.createCarousel()}
        </Row>
      </div>
    )
  }
}