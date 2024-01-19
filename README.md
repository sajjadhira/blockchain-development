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
