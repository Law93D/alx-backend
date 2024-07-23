0x01. Caching
Back-end

### `base_caching.py`

This module contains the `BaseCaching` class, which provides a base for caching systems with the following features:

- `MAX_ITEMS`: A constant defining the maximum number of items allowed in the cache.
- `__init__`: Initializes an empty cache.
- `print_cache`: Prints the current state of the cache.
- `put`: Placeholder method to add an item to the cache. Must be implemented in a subclass.
- `get`: Placeholder method to retrieve an item from the cache by its key. Must be implemented in a subclass.

## How to Use

1. Create a subclass of `BaseCaching`.
2. Implement the `put` and `get` methods in your subclass.
