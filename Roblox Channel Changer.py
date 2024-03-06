import os
import json

def update_settings(settings_file_path, channel, channel_change_mode):
    if os.path.isfile(settings_file_path):
        with open(settings_file_path, 'r+') as file:
            settings = json.load(file)
            settings["Channel"] = channel
            settings["ChannelChangeMode"] = channel_change_mode
            settings["OhHeyYouFoundMe"] = True
                
            file.seek(0)
            json.dump(settings, file, indent=4)
            file.truncate()
            
        print(f"Your channel has now been set to {channel}. Roblox will {'always prompt' if channel_change_mode == 1 else 'never change'} your preferred channel.")
        input("Click Enter to exit.")
    else:
        print("Cannot find settings.json file for Bloxstrap. Make sure you have Bloxstrap installed!")  
        input("Click Enter to exit.")

def main():
    settings_file_path = os.path.expanduser('~') + "\\AppData\\Local\\Bloxstrap\\Settings.json"
    channel = input("Enter the channel you want (e.g., Live): ").strip()
    channel_change_mode = int(input("Select the channel change mode:\n1 - Always Prompt\n2 - Never Change\nEnter your choice: ").strip())
    update_settings(settings_file_path, channel, channel_change_mode)

if __name__ == "__main__":
    main()
