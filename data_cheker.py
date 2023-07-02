# import pandas as pd
import numpy as np
import os
file_path = "/Users/mohammadreza/Documents/3-sem/ps/data/Kuken_videos/Kuken_videos-00_1/gt/gt.txt"  # Specify the path to your text file

# Open the file in "read" mode
with open(file_path, "r") as file:
    # Read the entire contents of the file
    file_contents = file.read()

# data = pd.DataFrame(file_contents)
# print(file_contents)
lines = file_contents.split("\n")
data = np.matrix(lines)
# print((data[0,0][0]))
# print(data.shape[1])
counter = 1
t = 0
imge_path = "/Users/mohammadreza/Documents/3-sem/ps/data/Kuken_videos/Kuken_videos-00_1/img1"
imgs = list(sorted(os.listdir(imge_path)))
print(len(imgs))
for i in range(len(imgs)):


    
    file_name = f"/Users/mohammadreza/Documents/3-sem/ps/data/Kuken_videos/Kuken_videos-00_1//annnot/{imgs[i][:-4]}.txt"

    num = data[0,t].split(",")
    print(num)
    print(num[0])
    with open(file_name, "w") as file:
        while int(num[0]) == counter :
            
        
            file.write(data[0,t] + "\n")
            # print(data[0,t])    
            t += 1
            num = data[0,t].split(",")
    counter += 1




