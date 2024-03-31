#!/usr/bin/python3

import re

def extract_youtube_links(file_path, output_file_path):
    pattern = r'href="/@([^"]+)"'
    youtube_base_url = "https://www.youtube.com"
    
    links = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        matches = re.finditer(pattern, content)
        
        for match in matches:
            # Extract the user/channel part from the match
            user_channel_part = match.group(0).split('"')[1]  # splits href="/@YoutubeChannelName" and takes /@YoutubeChannelName
            full_url = youtube_base_url + user_channel_part
            links.append(full_url)
    
    # Write links to the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for link in links:
            output_file.write(link + '\n')


file_path = 'ytsubrip.html'
output_file_path = 'channel_list.txt'
extract_youtube_links(file_path, output_file_path)

print(f"Links have been written to {output_file_path}.")
