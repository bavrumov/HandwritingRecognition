import React, { Component } from 'react'

const Ben= {
    name: 'Benjamin Kats',
    college: 'Brooklyn College Senior',
    phone: '347-601-5317',
    github: 'github.com/benkats',
    email: 'katsbenjamin@gmail.com',
    linkedin: 'linkedin.com/in/benkats'
}

const Benji= {
    name: 'Benjamin Karasik',
    college: 'Brooklyn College Senior',
    phone: '201-912-7821',
    github: 'github.com/benjaminkarasik28',
    email: 'Karasik.benjamin28@gmail.com ',
    linkedin: 'linkedin.com/in/benjamin-k-798a0687'
}

const Boris= {
    name: 'Boris Avrumov',
    college: 'Brooklyn College Senior',
    phone: '347-248-1966',
    github: 'github.com/bavrumov',
    email: 'bavrumov@hotmail.com ',
    linkedin: 'linkedin.com/in/bavrumov'
}

const Vlad= {
    name: 'Vlad Borisov',
    college: 'Brooklyn College Senior',
    phone: '347-751-4955',
    github: 'github.com/vladborisov',
    email: 'vladborisov.vbnyc@gmail.com ',
    linkedin: ''
}

var team = [Boris, Vlad, Benji, Ben];


export default class Carousel extends Component {
    createCarousel = () => {
        let elements = [];

        for(let i = 0; i<team.length; i++) {
            elements.push(
            <div>
                <h1>{team[i].name}</h1>
                <h3>{team[i].github}</h3>
                <h5>{team[i].email}</h5>
                <br></br>
            </div>
            )
        }

        return elements;
    }

  render() {
    return (
      <div>
        {this.createCarousel()}
      </div>
    )
  }
}