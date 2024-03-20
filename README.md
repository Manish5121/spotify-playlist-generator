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

### Step 1: Create a Spotify Application
1. Go to the  [https://developer.spotify.com](https://developer.spotify.com)
2. Log in with your Spotify account or sign up if you don't have one.
3. Click on "Create an App" and fill in the required information to create your application.
4. Once created, note down the Client ID and Client Secret. You'll need these later.

### Step 2: Add Redirect URI
1. In your Spotify application settings, add a Redirect URI and set it to `http://localhost:8000`
2. Save your changes.
   
### Step 3: Clone the Repository
1. Clone this repository
   
### Step 4: Install Dependencies
1. Ensure you have Python 3.6 or above installed.
2. Install all dependencies (`pip install -r requirements.txt`)
3. Set two environment variables, `CLIENT_ID`, `CLIENT_SECRET`and `REDIRECT_URI`
```bash
FOR Linux/Mac

export CLIENT_ID="your_client_id"
export CLIENT_SECRET="your_client_secret"
export REDIRECT_URI="http://localhost:8000"
```
```bash
FOR Windows

set CLIENT_ID="your_client_id"
set CLIENT_SECRET="your_client_secret"
set REDIRECT_URI="http://localhost:8000"

```

### Step 6: Authenticate
1. Run the main.py script to authenticate your Spotify account: `python main.py`
2. Follow the authentication prompts to authorize the application with your Spotify account.

### Step 7: Run the Application
1. Once authenticated, you can run the main application: `python main.py`


<a name="contribution-guidelines"></a>
## Contribution Guidelines
Pull requests are welcome!