import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { FormGroup, FormControl, Button } from "react-bootstrap";
import { API_BASE_URL } from "../config";

function ConductTransaction() {
  const [recipient, setRecipient] = useState("");
  const [amount, setAmount] = useState(0);
  const [knownAddresses, setKnownAddresses] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}/known-addresses`)
      .then((response) => response.json())
      .then((json) => setKnownAddresses(json));
  }, []);

  const updateRecipient = (event) => {
    setRecipient(event.target.value);
  };

  const updateAmount = (event) => {
    setAmount(Number(event.target.value));
  };

  const submitTransaction = () => {
    fetch(`${API_BASE_URL}/wallet/transact`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ recipient, amount }),
    })
      .then((response) => response.json())
      .then((json) => {
        console.log("submitTransaction json", json);
        alert("Success!");
        setRecipient("");
        setAmount(0);
      });
  };

  return (
    <div className="ConductTransaction">
      <Link to="/">Home</Link>
      <hr />
      <h3>Conduct a Transaction</h3>
      <br />
      <FormGroup>
        <FormControl
          input="text"
          placeholder="recipient"
          value={recipient}
          onChange={updateRecipient}
        />
      </FormGroup>
      <br />
      <FormGroup className="mt-2">
        <FormControl
          input="number"
          placeholder="amount"
          value={amount}
          onChange={updateAmount}
        />
      </FormGroup>

      <div>
        <br />
        <Button variant="danger" size="sm" onClick={submitTransaction}>
          Submit
        </Button>

        <br />
        <h4>Known Addressess</h4>
        <div>
          {knownAddresses.map((knownAddress, index) => (
            <span key={knownAddress}>
              <u>{knownAddress}</u>
              {index !== knownAddresses.length - 1 ? ", " : ""}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}
export default ConductTransaction;
