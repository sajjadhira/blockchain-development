import React, { useState } from "react";
import { FormGroup, FormControl, Button } from "react-bootstrap";
import { API_BASE_URL } from "../config";

function ConductTransaction() {
  const [recipient, setRecipient] = useState("");
  const [amount, setAmount] = useState(0);

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
      </div>
    </div>
  );
}
export default ConductTransaction;
