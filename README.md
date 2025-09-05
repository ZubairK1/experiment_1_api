### How to run
1. python3 -m venv .venv && source .venv/bin/activate
2. pip install -r requirements.txt
3. In one terminal run the hospital A API using: python -m uvicorn hospital_A.app:app --reload --port 8001
4. In another terminal run the hospital B API using: python -m uvicorn hospital_B.app:app --reload --port 8002
5. In another terminal, run the aggregator API: python -m uvicorn main_api.main:app --reload --port 8003
6. In another terminal navigate to main_api using cd main_api and run python3 query.py
7. Enter one of the listed conditions and one of the listed buyer IDs and run
