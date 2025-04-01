__version__ = "1.1.0"

import json
from pathlib import Path


def load_config(json_path: Path, default_data: any = None):
    """
    Load configuration from a JSON file. If the file does not exist, create it with default data.

    Args:
        json_path (Path): Path to the JSON file.
        default_data (any, optional): Default data to write if the file does not exist. Defaults to None.

    Returns:
        any: Data loaded from the JSON file.
    """
    json_path = _verify_path_object(json_path)
    _verify_or_write_json(json_path, default_data)
    return _load_data_from_json(json_path)


def _verify_path_object(json_path: Path) -> Path:
    """
    Verify that the given path is a Path object. If not, convert it to one.

    Args:
        json_path (Path): Path to verify.

    Returns:
        Path: Verified Path object.
    """
    if not isinstance(json_path, Path):
        json_path = Path(json_path)
    return json_path


def _write_default_data(json_path: Path, default_data: any) -> None:
    """
    Write default data to a JSON file.

    Args:
        json_path (Path): Path to the JSON file.
        default_data (any): Default data to write.
    """
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(default_data, json_file, indent=2)


def _verify_or_write_json(json_path: Path, default_data: any = None) -> None:
    """
    Verify if a JSON file exists. If not, create it with default data or prompt the user.

    Args:
        json_path (Path): Path to the JSON file.
        default_data (any, optional): Default data to write if the file does not exist. Defaults to None.
    """
    if not json_path.exists():
        if not json_path.parent.is_dir():
            json_path.parent.mkdir(parents=True)

        if default_data:
            _write_default_data(json_path, default_data)
        else:
            input(f"\n File not found:\n {json_path}")


def _load_data_from_json(json_path: Path) -> any:
    """
    Load data from a JSON file.

    Args:
        json_path (Path): Path to the JSON file.

    Returns:
        any: Data loaded from the JSON file.
    """
    with open(json_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)
