# Instagram Profile Info Downloader and Mutual Followers Finder

This Python script uses the [Instaloader](https://github.com/instaloader/instaloader) library to download the list of followers and followings for two Instagram profiles. It also compares the two profiles to find mutual followers and followings, saving the results in text files.

## Features
- Download followers and followings for any Instagram user.
- Compare two Instagram users and find their mutual followers and followings.
- Save the results in organized text files for easy access.

## Requirements
- Python 3.x
- [Instaloader](https://pypi.org/project/instaloader/)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/instagram-profile-info-downloader.git
    cd instagram-profile-info-downloader
    ```

2. **Install the dependencies:**
    ```bash
    pip install instaloader
    ```

3. **Login to Instagram:**
   - Open the `download_profile_info` function in the script.
   - Replace `"your_username"` and `"your_password"` with your Instagram credentials.

## Usage

1. **Run the script:**

    ```bash
    python script.py
    ```

2. **Enter the Instagram usernames** when prompted:
    - The script will ask for two Instagram usernames.
    - It will then download their followers and followings and find their mutual followers and followings.

3. **Results:**
    - The script will create a folder for each username, storing their followers and followings in `followers.txt` and `following.txt`.
    - A folder for mutuals will be created, containing `mutual_followers.txt` and `mutual_followings.txt`.

## Example

```bash
Enter the first username: user1
Enter the second username: user2
