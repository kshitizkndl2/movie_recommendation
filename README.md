# Movie Recommender System

This is a **portfolio project** to show how I approach a content-based recommendation problem: cleaning TMDB metadata, building text tags, vectorizing them, and serving similar-movie suggestions in a small demo UI.

It is **not a production or final deployment**. There is no user accounts, no live TMDB API, no collaborative filtering, and no hosted backend. It is a local demo you can run to try the idea.

## What it can do

- Recommend **5 similar movies** when you pick a title from the catalog
- Walk through the full pipeline in the notebook:
  - Load TMDB 5000 movies and credits (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`)
  - Merge on title and keep genres, keywords, overview, cast, and crew
  - Parse JSON-like fields into lists (genre names, keywords, top cast, director)
  - Build a `tags` string per movie and stem the words
  - Vectorize tags with `CountVectorizer` (5,000 features, English stop words)
  - Compute **cosine similarity** between movie vectors
- Serve recommendations in a Streamlit app using `movies_list.pkl` and `similarity.pkl`

This is content-based similarity (movies that share similar tags), not “people who watched this also watched…”.

## How to run the demo

The app needs `similarity.pkl`. That cosine similarity matrix is large, so it is often left out of GitHub and regenerated locally. If the file is missing, open `Movie-recomender.ipynb` and run it through the pickle-dump cells first.

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Pick a movie, click **Recommend**, and the app lists five similar titles.

## Project files

| File | Role |
| --- | --- |
| `Movie-recomender.ipynb` | Data cleaning, tag building, similarity, evaluation of the flow |
| `app.py` | Streamlit demo |
| `requirements.txt` | Python packages for the notebook and app |
| `tmdb_5000_movies.csv` / `tmdb_5000_credits.csv` | TMDB 5000 source data |
| `movies_list.pkl` | Saved movie id / title / tags table |
| `similarity.pkl` | Saved cosine similarity matrix (created by the notebook; usually not on GitHub because it is large — regenerate it locally) |

## What this is not

- Not Netflix, Letterboxd, or any live streaming catalog
- Not personalized to a user’s watch history
- Not a finished product with tests, monitoring, or a deployed backend

If you are reviewing this as a hiring sample, treat it as evidence of NLP, sklearn, and a content-based recommender workflow, not as a shipping recommendation engine.
