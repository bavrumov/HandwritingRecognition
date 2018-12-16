import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import pic from './static/person-male.png'
import {Row, Col} from 'reactstrap'

const Ben= {
    name: 'Benjamin Kats',
    college: 'Brooklyn College Senior',
    github: 'github.com/benkats',
    email: 'katsbenjamin@gmail.com',
    linkedin: 'linkedin.com/in/benkats'
}

const Benji= {
    name: 'Benjamin Karasik',
    college: 'Brooklyn College Senior',
    github: 'youtube.com/bitunusual',
    email: 'Karasik.benjamin28@gmail.com ',
    linkedin: 'linkedin.com/in/benjamin-k-798a0687'
}

const Boris= {
    name: 'Boris Avrumov',
    college: 'Brooklyn College Senior',
    github: 'bavrumov.github.io',
    email: 'bavrumov@hotmail.com ',
    linkedin: 'linkedin.com/in/bavrumov'
}

const Vlad= {
    name: 'Vlad Borisov',
    college: 'Brooklyn College Senior',
    github: 'github.com/vladborisov',
    email: 'vladborisov.vbnyc@gmail.com ',
    linkedin: 'vladborisov.com'
}

var team = [Boris, Vlad, Benji, Ben];

export default class Carousel extends Component {
    createCarousel = () => {
        let elements = [];

        for(let i = 0; i<team.length; i++) {
          
             elements.push(
             <Col sm={12} md={6} lg={6} key={i}>
                <div style={{width:"100%"}}><img
                src={pic}
                alt={team[i].name}
                width="100%"
                />
                </div>
                 <h1>{team[i].name}</h1>
                 <h3><a className="App-link" href={"https://"+team[i].github}>{team[i].github}</a></h3>
                 <h5><a href={"https://www."+team[i].linkedin} style={{color:"goldenrod"}}>{team[i].linkedin}</a></h5>
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