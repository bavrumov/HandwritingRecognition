import React, { Component } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
// import { UncontrolledCarousel } from 'reactstrap';

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
    github: '',
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
    linkedin: 'vladborisov.com'
}

var team = [Boris, Vlad, Benji, Ben];

// var items = [
//     {
//       src: slide1,
//       altText: 'enword',
//       caption: 'Boris.github',
//       header: Boris.name
//     },
//     {
//       src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa20%20text%20%7B%20fill%3A%23444%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa20%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23666%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22247.3203125%22%20y%3D%22218.3%22%3ESecond%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
//       altText: 'Slidvhgjhghe 2',
//       caption: 'Slid////e 2',
//       header: 'Slide 2 Hegfgfdffbgader'
//     },
//     {
//       src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa21%20text%20%7B%20fill%3A%23333%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa21%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23555%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22277%22%20y%3D%22218.3%22%3EThird%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
//       altText: 'Slide 3',
//       caption: 'Slide 3',
//       header: 'Slide 3 Header'
//     },
//     {
//       src: 'data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22800%22%20height%3D%22400%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20800%20400%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_15ba800aa21%20text%20%7B%20fill%3A%23333%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A40pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_15ba800aa21%22%3E%3Crect%20width%3D%22800%22%20height%3D%22400%22%20fill%3D%22%23555%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%22277%22%20y%3D%22218.3%22%3EThird%20slide%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E',
//       altText: 'Slide 4',
//       caption: 'Slide 4',
//       header: 'Slide 4 Header'
//     }
//   ];

  const style = 
    {
        width:"90%",
        marginLeft:"5%"
    }

export default class Carousel extends Component {
    createCarousel = () => {
        let elements = [];

        for(let i = 0; i<team.length; i++) {
          
             elements.push(
             <div className="col-md-3 col-s-6">
                
                 <h1>{team[i].name}</h1>
                 <h3>{team[i].github}</h3>
                 <h5><a href={"https://www."+team[i].linkedin}>{team[i].linkedin}</a></h5>
                 <br></br>
             </div>
             )
            // items[i].header=team[i].name;
            // items[i].src=`./images/slide${i+1}`;
            // items[i].caption=team[i].github;
        

        }
        return elements;
    }
  
    //items = this.createCarousel();
  render() {
    //console.log(items);
    return (
      <div className="row" style = {style}>
        {this.createCarousel()}
      </div>
    )
  }
}