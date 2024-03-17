# Spotify Playlist Generator

#### Description:
 Spotify Playlist Generator simplifies music discovery by enabling users to swiftly create customized and shareable Spotify playlists based on mood, genre, or artist preferences. This innovative solution combines ease-of-use, intelligent recommendations, and real-time collaboration features, offering a fresh perspective on digital entertainment. Dive into a richer audio experience with Spotify Playlist Generator at your fingertips.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Contribution Guidelines](#contribution-guidelines)


<a name="features"></a>
## Features
- Personalized playlists generated according to mood, genre, or artist preferences
- Real-time collaboration between multiple users during playlist editing
- Command-line and Graphical User Interface (GUI) options for maximum compatibility
- Seamless integration with existing Spotify accounts
- Advanced AI algorithms providing accurate song suggestions

<a name="requirements"></a>
## Requirements
To run the Spotify Playlist Generator locally, ensure you meet the following prerequisites:

- Python >= 3.7
- pip package manager
- Required libraries installed (see [`requirements.txt`](./requirements.txt))

For optimal performance, consider installing the recommended packages listed in [`requirements.txt`].

To do so, execute the following commands:

```bash
pip install --user -r requirements.txt
```


### Prerequisites

- [Python 3.6+](https://www.python.org/downloads/)
- [Spotify](https://www.spotify.com/)



<a name="installation"></a>
## Installation
1. Make a application at [https://developer.spotify.com](https://developer.spotify.com)
2. Add a Redirect URI to the application and set is as `http://localhost:8000`
3. Clone this repository
4. Install all dependencies (`pip install -r requirements.txt`)
5. Set two environment variables, `CLIENT_ID`, `CLIENT_SECRET`and `REDIRECT_URI`
6. Authenticate by running `main.py`
7. Run `main.py` to use


<a name="contribution-guidelines"></a>
## Contribution Guidelines
Pull requests are welcome!
