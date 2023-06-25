import instaloader

ig = instaloader.Instaloader()

dp = input("Enter Instagram username: ")

ig.download_profile(dp , profile_pic_only=True)
