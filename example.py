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
