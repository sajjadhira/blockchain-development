import React, { useState, useEffect } from "react";
import { API_BASE_URL } from "../config";
import Block from "./Block";
import { Button } from "react-bootstrap";

const PAGE_RANGE = 3;

function Blockchain() {
  const [blockchain, setBlockchain] = useState([]);
  const [blockchainLength, setBlockchainLength] = useState(0);

  const fetechBlockchainPage = ({ start, end }) => {
    fetch(`${API_BASE_URL}/blockchain/range?start=${start}&end=${end}`)
      .then((response) => response.json())
      .then((json) => setBlockchain(json));
  };

  useEffect(() => {
    fetechBlockchainPage({ start: 0, end: PAGE_RANGE });

    fetch(`${API_BASE_URL}/blockchain/length`)
      .then((response) => response.json())
      .then((json) => setBlockchainLength(json));
  }, []);

  const buttonNumbers = [];
  for (let i = 0; i < Math.ceil(blockchainLength / PAGE_RANGE); i++) {
    buttonNumbers.push(i);
  }

  return (
    <div>
      <div className="Blockchain">
        <h3>Blockchain</h3>
        <div>
          {blockchain.map((block) => (
            <Block key={block.hash} block={block} />
          ))}
        </div>
      </div>
      <div>
        {buttonNumbers.map((number) => {
          const start = number * PAGE_RANGE;
          const end = (number + 1) * PAGE_RANGE;

          return (
            <span
              key={number}
              onClick={() => fetechBlockchainPage({ start, end })}
            >
              <Button size="sm" variant="danger" className="ms-2 me-2">
                {number + 1}
              </Button>
            </span>
          );
        })}
      </div>
    </div>
  );
}
export default Blockchain;
