# config.py

# Grid and Room Settings
ROOM_WIDTH = 800
ROOM_HEIGHT = 600


# Player Settings
PLAYER_SPEED = 100
PLAYER_IMAGE_PATH = "./squirrel.png"   # relative to project root
PLAYER_IMAGE_SIZE = (60,60)             # w, h in pixels
PLAYER_RADIUS = 24                   #  collision/visual radius

# Apple Settings
APPLE_SIZE = (60, 60)
APPLE_IMAGE_PATH = "./apple.png"
APPLES = {
    "apple1": {"pos" : (150,100)},
    "apple2": {"pos" : (400,250)},
    "apple3": {"pos" : (600,350)},
    "apple4": {"pos" : (200,450)},
    "apple5": {"pos" : (700,500)},
    "apple6": {"pos" : (350,150)},
    "apple7": {"pos" : (500,400)},
    "apple8": {"pos" : (250,300)},
    "apple9": {"pos" : (550,200)},
    "apple10": {"pos" : (100,350)}
}

# Screen Size
WIDTH = ROOM_WIDTH
HEIGHT = ROOM_HEIGHT 

# Colors (R, G, B)
BG_COLOR = (130, 181, 96) # Draw a background on ipad (800, 600)
PLAYER_COLOR = (100, 200, 255)
PLAY_SCREEN = (242, 213, 255)
TEXT_COLOR = (72, 45, 84)
BOX_COLOR = (179, 108, 209)
# Frames Per Second
FPS = 60

# Display Screen
GAME_OVER = "./game_over.png"
YOU_WIN = "./you_win1.png"