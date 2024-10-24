import pickle
import joblib
from tqdm import tqdm

SUBJECT_IDS = [i for i in range(2, 18) if i != 12]

for subject_id in tqdm(SUBJECT_IDS):
    try:
        with open(f'WESAD/S{subject_id}/S{subject_id}.pkl', 'rb') as f:
            data = pickle.load(f, encoding = 'latin1')
            
        joblib.dump(data, f'WESAD/S{subject_id}/S{subject_id}.joblib')
    except Exception as e:
        print(f"Error in S{subject_id}: {e}")