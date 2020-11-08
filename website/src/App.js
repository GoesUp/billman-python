import React, { Component } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
import './scss/style.scss';

const loading = (
  <div className="pt-3 text-center">
    <div className="sk-spinner sk-spinner-pulse"></div>
  </div>
)

// Containers
const TheLayout = React.lazy(() => import('./containers/TheLayout'));

class App extends Component {

  render() {
    return (
      <HashRouter>
          <React.Suspense fallback={loading}>
            <Switch>
              <Route path="/" name="Home" render={props => <TheLayout data={this.state} {...props}/>} />
            </Switch>
          </React.Suspense>
      </HashRouter>
    );
  }

  state = {};

  componentDidMount() {
    fetch("http://localhost:5000/user/0/bills/recent")
      .then((res) => res.json())
      .then((data) => {
        fetch("http://localhost:5000/statistics/0/dict")
          .then((res) => res.json())
          .then((stat) => {
            fetch("http://localhost:5000/user/0/bills")
              .then((res) => res.json())
              .then((unp) => {
                fetch("http://localhost:5000/user/0/bills/paid")
                  .then((res) => res.json())
                  .then((pp) => {
                    fetch("http://localhost:5000/user/0/family")
                      .then((res) => res.json())
                      .then((familymembers) => {
                        fetch("http://localhost:5000/community/active")
                          .then((res) => res.json())
                          .then((revezi) => {
                            this.setState({urgent: data, cake1: stat.cake1, cake2: stat.cake2, transactions: stat.transactions, metric2: stat.for_month, metric1: stat.for_week, metric3: stat.credits, metric4: stat.donations, unpaid: unp, paid: pp, family: familymembers, poor: revezi});
                          })
                      })
                  })
              })
          })
      });
  };


}

export default App;
