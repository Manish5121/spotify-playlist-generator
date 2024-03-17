from project import *
import pytest

def main():
    test_get_last_played_tracks()
    test_parse_multiple_songs()
    test_get_recommended_tracks()


def test_parse_multiple_songs():
    assert parse_multiple_songs("sicko mode, Superhero") == ["sicko mode", " Superhero"]
    assert parse_multiple_songs("sicko mode") == ["sicko mode"]

def test_get_last_played_tracks():
    with pytest.raises(ValueError):
        get_last_played_tracks("manish")

def test_get_recommended_tracks():
    with pytest.raises(ValueError):
        get_recommended_tracks(5)
