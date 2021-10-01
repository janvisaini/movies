import moviepy.editor as mp 

  
inp_path = input("enter video path")
out_path = input("enter audio path to save")
# Insert Local Video File Path  

clip = mp.VideoFileClip(inp_path) 



# Insert Local Audio File Path 

clip.audio.write_audiofile(out_path) 
