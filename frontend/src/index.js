import React from "react";
import ReactDOM from "react-dom/client";
import { Router, Switch, Route } from "react-router-dom";
import { createBrowserHistory } from "history";
import "./index.css";
import App from "./components/App";

import Blockchain from "./components/Blockchain";
import ConductTransaction from "./components/ConductTransaction";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Router history={createBrowserHistory()}>
    <Switch>
      <Route exact path="/" component={App} />
      <Route path="/blockchain" component={Blockchain} />
      <Route path="/conduct-transaction" component={ConductTransaction} />
    </Switch>
  </Router>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
