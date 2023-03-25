from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('PATH_TO_JSON_FILE')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('readable_data.json')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)