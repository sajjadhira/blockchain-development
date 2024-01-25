**Setup the virtual environment**

```
python -m venv blockchain-env
```

**Activate the virtual environment**

```
source blockchain-env/Scripts/activate
```

**Install all packages**

```
pip install -r requirements.txt
```

**Run the tests**
Make sure to activate the virtual environmnet.

```
python -m pytest backend/test
```

**Run the application and API**
Make sure to activate virtual environmnet

```
python -m backend.app
```

**Run a peer instanace**

Make sure to activate virtual environmnet

```
export PEER=True && python -m backend.app
```

**Seeding Data to BlockChain**

Use tjos command to seeding data to the blockchain. Make sure virtual environment is running on your machine.

```
export SEED_DATA=True && python -m backend.app
```

**Install ReactJS for frontend**
For install ReactJS for frontend make sure you have install `npm` in your machine.
If you make sure `npm` is installe in your machine then run command for installing ReactJS as frontend from your root directory,

```
npx create-react-app frontend
```

After installing react run your project for running reactjs enter into frontend directory by using command `cd frontend` and then run the command for run react.

```
npm run start
```
