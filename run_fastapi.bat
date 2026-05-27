cd /d "C:\ProgramData\Jenkins\.jenkins\workspace\IrisDataset1"

python -m uvicorn app:app --host 127.0.0.1 --port 8091 --reload

pause