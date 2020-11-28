# API Documentation

## Users

Usage

```python
from _8a_scraper.users import get_user_info, get_recommended_ascents, get_user_ascents
```

### `get_user_info(user)`

Parameters:

- `user` - Climber name (e.g. `'Adam Ondra'`)

Returns:

A dictionary containing the following keys:

```python
['location', 'age', 'website', 'sponsors', 'started_climbing', 'occupation',
  'other_interests', 'best_climbing_area', 'known_areas']
  ```

If a user did not input a field, the value for the corresponding key will be `None`.

### `get_recommended_ascents(user)`

Parameters:

- `user` - Climber name (e.g. `'Adam Ondra'`)

Returns:

A list of dictionaries containing the following keys for each ascent:

```python
['areaName', 'areaSlug', 'countrySlug', 'cragName', 'cragSlug', 'difficulty', 'gradeIndex', 'sectorSlug', 'zlaggableName', 'zlaggableSlug', 'category']
```

If a user did not input a field, the value for the corresponding key will be `None`.

### `get_user_ascents(user, category)`

Parameters:

- `user` - Climber name (e.g. `'Adam Ondra'`)
- `category` - `'bouldering' | 'sportclimbing'`

Returns:

A list of dictionaries containing the following keys for each ascent:

```python
['ascentId', 'areaName', 'areaSlug', 'cragName', 'cragSlug', 'sectorSlug', 'zlaggableName', 'zlaggableSlug', 'countrySlug', 'userAvatar', 'userName', 'userSlug', 'date', 'difficulty', 'gradeIndex', 'comment', 'isHard', 'isEasy', 'firstAscent', 'secondGo', 'type', 'notes', 'rating']
```

If a user did not input a field, the value for the corresponding key will be `None`.

## Ascents

Usage

```python
from _8a_scraper.ascents import get_ascents
```

### `get_ascents(name, category)`

Parameters:

- `name` - Climb name (e.g. `'Midnight Lightning'`)
- `category` - `'bouldering' | 'sportclimbing'`

Returns:

A list of dictionaries containing the following keys for each climber who ascented the climb:

```python
['userAvatar', 'userName', 'userSlug', 'date', 'difficulty', 'isHard', 'isEasy', 'type', 'notes', 'rating', 'userPrivate', 'firstAscent', 'secondGo']
```

If a user did not input a field, the value for the corresponding key will be `None`.
