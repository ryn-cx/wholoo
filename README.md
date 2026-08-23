# wholoo

Hulu API wrapper.

```python
from get_around import build_client_automatically
from wholoo import Wholoo

client = Wholoo(build_client_automatically())

results = client.search("The Bear")
first = results.groups[0].results[0]

series = client.tv(str(first.metrics_info.target_id))
season = client.season(str(series.id), 1)
print(series.name, [episode.name for episode in season.items])

movie = client.movies("4ee4f57e-19bd-493f-96f9-ad3e753af981")
print(movie.name, movie.details.entity.duration)
```

Each endpoint is also a download and a load: `client.movies.download(id)` returns
the response as it was served, and `client.movies.load(data)` reads it into its
model.

Models are generated from the responses recorded under `tests/_files` with
`uv run python -m tests.generate_models`.
