class Path:
    def __init__(self, path=None):
        if path is None:
            path = []
        self.path = path

    def __getattr__(self, name):
        # Every time an attribute is accessed, extend the path with that attribute name
        return Path(self.path + [name])

    def __getitem__(self, index):
        # Allow indexing to also form part of the path
        return Path(self.path + [index])

    def __call__(self, data):
        # Navigate through the data according to the path
        result = data
        for step in self.path:
            if isinstance(result, dict) and step in result:
                result = result[step]
            elif isinstance(result, list) and isinstance(step, int) and 0 <= step < len(result):
                result = result[step]
            else:
                # If the path is invalid or inaccessible, return None or raise an error
                raise KeyError(f"Invalid path or index '{step}' at {result}")
        return result

    def __repr__(self):
        # Helpful for debugging: show the path
        return f"Path({self.path})"
