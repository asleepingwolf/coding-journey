import json
import os

# Define the target directory and filename
# Using os.path.join for cross-platform compatibility (Windows/Mac/Linux)
#target_dir = os.path.join("extra_exercises", "JSON_Experiments")
#file_path = os.path.join(target_dir, "Highscore_List.txt")

highscores = '{"Kalle": 150, "Lisa": 300, "Pelle": 50, "Julia": 999999}'

y = json.loads(highscores)

for p in y:
    print(p, y[p])
print(y["Kalle"])