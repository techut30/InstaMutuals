import instaloader
import os
import sys

def download_profile_info(username):
    L = instaloader.Instaloader()

    try:
        L.login("your_username", "your_password")
        profile = instaloader.Profile.from_username(L.context, username)
        main_folder = f"{username}_data"
        os.makedirs(main_folder, exist_ok=True)

        followers_file = os.path.join(main_folder, "followers.txt")
        following_file = os.path.join(main_folder, "following.txt")

        with open(followers_file, 'w') as file:
            followers = [follower.username for follower in profile.get_followers()]
            file.write('\n'.join(followers))

        with open(following_file, 'w') as file:
            followings = [followee.username for followee in profile.get_followees()]
            file.write('\n'.join(followings))

        print(f"Data for {username} has been downloaded successfully.")

        return followers, followings

    except instaloader.exceptions.InstaloaderException as e:
        print(f"An error occurred: {e}")
        return [], []

def save_mutuals(username1, followers1, followings1, username2, followers2, followings2):
    mutual_followers = set(followers1) & set(followers2)
    mutual_followings = set(followings1) & set(followings2)

    main_folder = f"{username1}_and_{username2}_mutuals"
    os.makedirs(main_folder, exist_ok=True)

    mutual_followers_file = os.path.join(main_folder, "mutual_followers.txt")
    with open(mutual_followers_file, 'w') as file:
        file.write('\n'.join(mutual_followers))

    mutual_followings_file = os.path.join(main_folder, "mutual_followings.txt")
    with open(mutual_followings_file, 'w') as file:
        file.write('\n'.join(mutual_followings))

    print(f"Mutual followers and followings between {username1} and {username2} have been saved.")

def process_usernames(username1, username2):
    if username1 and username2:
        try:
            print("Downloading...")
            followers1, followings1 = download_profile_info(username1)
            print("Downloading...")
            followers2, followings2 = download_profile_info(username2)
            save_mutuals(username1, followers1, followings1, username2, followers2, followings2)
        except KeyboardInterrupt:
            print("\nProcess interrupted.")
            sys.exit(0)
    else:
        print("One or both usernames are missing. Exiting...")

def main():
    username1 = input("Enter the first username: ").strip()
    username2 = input("Enter the second username: ").strip()
    process_usernames(username1, username2)

if __name__ == "__main__":
    main()
