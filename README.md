# Codebase Navigation & Adaptation Exercise - Binder Setup

## Files to upload to a NEW public GitHub repo (root level)
- Codebase_Navigation_Exercise.ipynb
- environment.yml
- helpers/  <- upload this as a FOLDER (drag the whole folder, not the loose files inside it,
  so GitHub preserves the helpers/ structure). It must contain:
  - __init__.py
  - campaign_loader.py
  - metrics_engine.py
  - data_quality.py
  - segmentation.py

## Steps
1. Create a new public GitHub repo (separate from any previous interview repo).
2. Add file > Upload files > drag in Codebase_Navigation_Exercise.ipynb and environment.yml,
   then separately drag in the helpers folder (as a folder) so it lands as helpers/ at the root.
3. Commit to main.
4. Go to mybinder.org, paste the new repo URL, branch = main,
   path to notebook = Codebase_Navigation_Exercise.ipynb, click Launch.
5. First build takes several minutes (Java + PySpark). Warm it up well before the interview.
6. Copy the generated mybinder.org/v2/gh/... URL (with ?labpath=Codebase_Navigation_Exercise.ipynb)
   - that is the link to send the candidate.

## After the interview
Delete this repo entirely rather than reusing or leaving it public - this is the clean way to
make sure the candidate (or anyone else who saw the link) has no further access. Create a fresh
repo from the same master files for the next candidate.
