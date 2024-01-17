import time
from backend.blockchain.blockchain import BlockChain
from backend.config import SECONDS, MINE_RATE

blockchain = BlockChain()

times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_mine = (end_time - start_time) / SECONDS
    times.append(time_to_mine)

    average_time = sum(times) / len(times)

    print(f"last block timestamp: {blockchain.chain[-2].timestamp}")
    print(f"new block timestamp: {blockchain.chain[-1].timestamp}")
    print(
        f"timestamp difference: {blockchain.chain[-1].timestamp - blockchain.chain[-2].timestamp}")
    print(
        f"time less then mine rate: {blockchain.chain[-1].timestamp - blockchain.chain[-2].timestamp < MINE_RATE}")

    print(f"new block difficulty: {blockchain.chain[-1].dificulty}")
    print(f"time to mine new block: {time_to_mine}s")
    print(f"average time to add blocks: {average_time}s\n")
    time.sleep(3)
