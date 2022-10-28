# Program To Read video
# and Extract Frames
import cv2
# from urllib.parse import urlparse
import os

# Check for common, supported video formats

def check_format(url):

    accepted_formats = ['.MOV']#, '.MP4', '.WMV'] # <- need to be tested.
    _, ext = os.path.splitext(url)
    ext = ext.upper()

    if ext not in accepted_formats:
        return False
    else:
        return True
    

# Function to extract frames
def make_frames(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()
        
        if success == False: break

        # Saves the frames with frame-count
        root, ext = os.path.splitext(path)
        which_video = root.split('/')[2]
        # print(which_video) # <- can be useful for debugging purposes
        
        cv2.imwrite(f"/pfs/out/{which_video}_frame_{count}.jpg", image)

        count += 1

# walk /pfs/images and call make_frames on every file found
# To run locally, wrap this bit in the if __name__ == '__main__':
print("About to run the os.walk")
for dirpath, dirs, files in os.walk("/pfs/video_tf-frames-demo"):
    print(dirpath, dirs, files)
    for file in files:
        file_path = os.path.join(dirpath, file)
        print(file_path)
        do_we_work_with_this_file_type = check_format(file_path)
        if not do_we_work_with_this_file_type: # Lots of room for asserts, try/excepts here.
            print(f"We don't support the extension for {file_path}. Check the extension and try again.")
            continue

        make_frames(file_path)