## How to run
```
1. python3 -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. python -m uvicorn hospital_A.app:app --reload --port 8001 #In one terminal run the hospital A API 
4. python -m uvicorn hospital_B.app:app --reload --port 8002 #In another terminal run the hospital B API
5. python -m uvicorn main_api.main:app --reload --port 8003 # In another terminal, run the aggregator API
6. #In another terminal navigate to main_api using
   cd main_api
   #and run
   python3 query.py
8. Enter one of the listed conditions and one of the listed buyer IDs and run
```
## Repo layout
```
├── hospital_A
│   ├── app.py
│   └── requirements.txt
├── hospital_B
│   ├── app.py
│   └── requirements.txt
├── main_api
│   ├── main.py
│   ├── query.py
│   └── utils.py
└── requirements.txt
```

