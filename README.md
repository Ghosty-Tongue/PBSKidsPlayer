# PBSKidsPlayer

PBSKidsPlayer is a Python package that allows you to fetch and display episode information for various PBS Kids shows using the PBS Kids API.

## Installation

1. Clone the repository or download the source code.
2. Navigate to the `PBSKidsPlayer` directory.
3. Install the package using pip:
    ```
    pip install .
    ```

## Usage

Here is an example of how to use the `PBSKidsPlayer` package to fetch and display episodes for a specific show.

### Example Script

```python
from pbskidsplayer import PBSKidsAPI

def main():
    api = PBSKidsAPI()
    show_name = input("Enter the show name: ")

    # Fetch episodes by show name
    episodes = api.get_episodes_by_show(show_name)

    if not episodes:
        print(f"No episodes found for show: {show_name}")
    else:
        for episode in episodes:
            title = episode.get("title")
            description = episode.get("description")
            print(f"Title: {title}")
            print(f"Description: {description}")
            print("-" * 40)

if __name__ == "__main__":
    main()
```

### Running the Example

1. Save the above example script to a file, e.g., `example.py`.
2. Run the script:
    ```
    python example.py
    ```
3. Enter the name of the show when prompted.

## Testing

To run the tests, navigate to the `PBSKidsPlayer` directory and run:
```
python -m unittest discover tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
