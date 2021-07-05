from youtubesearchpython import VideosSearch
videosSearch = VideosSearch('NoCopyrightSounds', limit = 1)
print(videosSearch.result()['result'][0]['link'])
