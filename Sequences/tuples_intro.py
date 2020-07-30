albumms = [
    ("Welcome to my Nightmare", "Alice Cooper", 975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
]
print(len(albumms))

for name, artist, year in albumms:
    print("Album:{:<23}, Artist:{:12}, Year:{:<4}"
          .format(name,artist,year))




