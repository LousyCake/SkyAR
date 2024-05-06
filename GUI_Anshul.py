import sys
import os
import cv2
from os.path import abspath, split, join
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import Tk, Button, StringVar, IntVar, Radiobutton, Checkbutton, Scale, HORIZONTAL, BooleanVar, DoubleVar
from tkinter.ttk import Progressbar


from PIL import ImageTk, Image
from threading import Thread
from SkyAR import SkyAR
import pyglet
import customtkinter
pyglet.font.add_file('OpenSans-SemiBold.ttf')
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
def file_select(item, types, is_save=False):
    if not is_save:
        item.set(askopenfilename(title='choose an video', filetypes=types))
        if item == skybox_img:
            skybox_video.set('')
        elif item == skybox_video:
            skybox_img.set('')
    else:
        item.set(asksaveasfilename(title='save result', filetypes=types))

def run(configs):
    skyar = SkyAR()
    skyar.MagicSky(**configs)
    bar.stop()
    start_button['bg'] = 'SystemButtonFace'
    start_button['state'] = 'normal'
    start_button['text'] = 'start'

def start():
    if skybox_video.get():
        is_video_sky = True
    else:
        is_video_sky = False
    configs = {
        'video_path': video_path.get(),
        'save_path': save_path.get(),
        'config': config_list[config_choose.get()],
        'is_rainy': is_rainy.get(),
        'preview_frames_num': 0,
        'is_video_sky': is_video_sky,
        'is_show': preview.get(),
        'skybox_img': skybox_img.get(),
        'skybox_video': skybox_video.get(),
        'rain_cap_path': rain_cap_path.get(),
        'halo_effect': halo_effect.get(),
        'auto_light_matching': auto_light_matching.get(),
        'relighting_factor': relighting_factor.get(),
        'recoloring_factor': recoloring_factor.get(),
        'skybox_center_crop': skybox_center_crop.get()
    }
    print(configs)
    start_button['bg'] = 'red'
    start_button['text'] = 'wait'
    start_button['state'] = 'disabled'
    bar.start()
    t = Thread(target=run, args=(configs,))
    t.start()

def reset():
    video_path.set('')
    save_path.set('result.mp4')
    skybox_img.set('')
    skybox_video.set('')
    rain_cap_path.set('')
    config_choose.set(4)
    is_rainy.set(False)
    halo_effect.set(True)
    preview.set(True)
    auto_light_matching.set(False)
    relighting_factor.set(0.8)
    recoloring_factor.set(0.5)
    skybox_center_crop.set(0.5)

def set_skybox_img():
    skybox_image_file = customtkinter.CTkImage(Image.open(skybox_img.get()),size=(640,360))
    skybox_preview = customtkinter.CTkLabel(root.image_prev_frame, text="", image=skybox_image_file)
    skybox_preview.grid(row=1, column=0, padx=5)
    
def set_video_prev():
    getFirstFrame(video_path.get())
    
def getFirstFrame(videofile):
    vidcap = cv2.VideoCapture(videofile)
    success, image = vidcap.read()
    if success:
        cv2.imwrite("videoPrev.jpg", image)
        videopath_preview_image_file = customtkinter.CTkImage(Image.open("videoPrev.jpg"),size=(640,360))
        videopath_preview = customtkinter.CTkLabel(root.video_prev_frame, text="", image=videopath_preview_image_file)
        videopath_preview.grid(row=1, column=0, padx=5)

if __name__ == "__main__":
    try:
        base_path = sys._MEIPASS
    except:
        base_path = split(abspath(__file__))[0]

    global config_list
    config_list = [
        'rainy', 'sunny', 'cloudy', 'galaxy', 'jupiter', 'sunset',
        'supermoon', 'floatingcastle', 'thunderstorm', 'district9ship', None
    ]

    #root = Tk()
    root = customtkinter.CTk()
    root.title('SkyAR GUI')
    root.iconbitmap(join(base_path, 'favicon.ico'))
    root.geometry('1920x1080')
    width = root.winfo_screenwidth
    root.state('zoomed')
    
    root.grid_columnconfigure((0,1), weight=4)
    root.grid_columnconfigure(2, weight=1)
    root.grid_rowconfigure(0, weight=3)
    root.grid_rowconfigure(1, weight=1)
    
   

    
    #image panel
    root.image_prev_frame = customtkinter.CTkFrame(root,width=150)
    root.image_prev_frame.grid(row=0,column=0, padx=20, pady=20,sticky="nsew")
    root.image_prev_frame.grid_columnconfigure(0, weight=1)
    
    image_preview_label = customtkinter.CTkLabel(root.image_prev_frame, text="Selected Skybox Image Preview :", font=customtkinter.CTkFont(size=15, weight="bold"))
    image_preview_label.grid(row=0, column=0, padx=5)
   
    skybox_img = StringVar()
    skybox_img_button = customtkinter.CTkButton(root.image_prev_frame, text='Custom skybox image',font=customtkinter.CTkFont(size=15), command=lambda: [file_select(
    skybox_img, (("image", "*.jpg; *.png; *.bmp; *.jpeg"), ("all", "*"))),set_skybox_img() ])
    skybox_img_button.grid(row=2,column=0,padx=20, pady=(20, 10),sticky = 'ew')
    
    #video panel
    root.video_prev_frame = customtkinter.CTkFrame(root,width=150)
    root.video_prev_frame.grid(row=0,column=1, padx=20, pady=20,sticky="nsew")
    root.video_prev_frame.grid_columnconfigure(0, weight=1)

    video_preview_label = customtkinter.CTkLabel(root.video_prev_frame, text="Selected Video Preview Thumbnail :", font=customtkinter.CTkFont(size=15, weight="bold"))
    video_preview_label.grid(row=0, column=0, padx=5)
    
    video_path = StringVar()
    video_button = customtkinter.CTkButton(root.video_prev_frame, text='Video path',font=customtkinter.CTkFont(size=15),command=lambda:[file_select(
    video_path, (("image", "*.mp4"), ("all", "*"))),set_video_prev()] )
    video_button.grid(row=2,column=0,padx=20, pady=(20, 10), sticky = 'ew')
    
    #side bar panel 
    root.sidebar_frame = customtkinter.CTkFrame(root,width=150)
    root.sidebar_frame.grid(row=0,column=2,rowspan=2, padx=20, pady=20,sticky="nsew")
    
    skybox_video = StringVar()
    skybox_video_button = customtkinter.CTkButton(root, text='custom skybox video',font=customtkinter.CTkFont(size=15), command=lambda: file_select(
        skybox_video, (("image", "*.mp4"), ("all", "*"))))

    rain_cap_path = StringVar()
    rain_video_button = customtkinter.CTkButton(root, text='custom rain effect video',font=customtkinter.CTkFont(size=15), command=lambda: file_select(
        rain_cap_path, (("image", "*.mp4"), ("all", "*"))))

    lastrow = 0
    premade_configs = customtkinter.CTkLabel(root.sidebar_frame, text="Premade Configs (Leave at custom if you are using a custom skybox):", font=customtkinter.CTkFont(size=15, weight="bold"))
    premade_configs.grid(row=0, padx=10, pady=10, sticky="nw")
    config_choose = IntVar()
    config_choose.set(10)
    for i, value in enumerate(config_list):
        if not value:
            value = 'custom'
        b = customtkinter.CTkRadioButton(root.sidebar_frame, text=value,font=customtkinter.CTkFont(size=15), variable=config_choose, value=i)
        b.grid(row=i+1,column =0,pady=5, padx=20,sticky="w")
        lastrow = i+1
       
    lastrow = lastrow + 1
    effects_label = customtkinter.CTkLabel(root.sidebar_frame, text="Color Grading Effects :", font=customtkinter.CTkFont(size=15, weight="bold"))
    effects_label.grid(row=lastrow, padx=10, pady=5, sticky="nw")
    is_rainy = BooleanVar()
    is_rainy.set(False)
    br = customtkinter.CTkCheckBox(root.sidebar_frame, text='Rainy Sky Color Grading',font=customtkinter.CTkFont(size=15), variable=is_rainy)
    br.grid(row=lastrow + 1, column=0, pady=(20, 0), padx=20, sticky="w")

    halo_effect = BooleanVar()
    halo_effect.set(True)
    bh = customtkinter.CTkCheckBox(root.sidebar_frame, text='Halo Effect',font=customtkinter.CTkFont(size=15), variable=halo_effect)
    bh.grid(row=lastrow + 2, column=0, pady=(20, 0), padx=20, sticky="w")

    preview = BooleanVar()
    preview.set(True)
    ba = customtkinter.CTkCheckBox(root.sidebar_frame, text='Enable Preview',font=customtkinter.CTkFont(size=15), variable=preview)
    ba.grid(row=lastrow + 3, column=0, pady=(20, 0), padx=20, sticky="w")

    auto_light_matching = BooleanVar()
    auto_light_matching.set(False)
    la = customtkinter.CTkCheckBox(root.sidebar_frame, text='Auto Light Matching',
                     variable=auto_light_matching)
    la.grid(row=lastrow + 4, column=0, pady=(20, 0), padx=20, sticky="w")

    relighting_label = customtkinter.CTkLabel(root.sidebar_frame, text="Relighting Factor (0.00 - 1.00) :", font=customtkinter.CTkFont(size=15, weight="bold"))
    relighting_label.grid(row=lastrow + 5, padx=10, pady=10, sticky="nw")
    relighting_factor = DoubleVar()
    relighting_factor.set(0.8)
    slider_1 = customtkinter.CTkSlider(root.sidebar_frame, from_=0.00, to=1.00, number_of_steps=100,variable=relighting_factor)
    slider_1.grid(row=lastrow + 6, padx=(20, 10), pady=(10, 10), sticky="ew")


    recoloring_label = customtkinter.CTkLabel(root.sidebar_frame, text="Recolouring Factor (0.00 - 1.00) :", font=customtkinter.CTkFont(size=15, weight="bold"))
    recoloring_label.grid(row=lastrow + 7, padx=10, pady=10, sticky="nw")
    recoloring_factor = DoubleVar()
    recoloring_factor.set(0.5)
    slider_2 = customtkinter.CTkSlider(root.sidebar_frame, from_=0.00, to=1.00, number_of_steps=100,variable=recoloring_factor)
    slider_2.grid(row=lastrow + 8, padx=(20, 10), pady=(10, 10), sticky="ew")


    skybox_center_crop_label = customtkinter.CTkLabel(root.sidebar_frame, text="Sky Box Center Crop (0.00 - 1.00) :", font=customtkinter.CTkFont(size=15, weight="bold"))
    skybox_center_crop_label.grid(row=lastrow + 9, padx=10, pady=10, sticky="nw")
    skybox_center_crop = DoubleVar()
    skybox_center_crop.set(0.5)
    slider_3 = customtkinter.CTkSlider(root.sidebar_frame, from_=0.00, to=1.00, number_of_steps=100,variable=skybox_center_crop)
    slider_3.grid(row=lastrow + 10, padx=(20, 10), pady=(10, 10), sticky="ew")
    
    #bottom control panel
    root.bottom_controls_frame = customtkinter.CTkFrame(root,width=150)
    root.bottom_controls_frame.grid(row=1,column=0,columnspan=2,padx=20, pady=20,sticky="nsew")
    root.bottom_controls_frame.grid_columnconfigure(0, weight=1)
    root.bottom_controls_frame.grid_columnconfigure(1, weight=1)
    root.bottom_controls_frame.grid_columnconfigure(2, weight=1)
    root.bottom_controls_frame.grid_rowconfigure(1, weight=2)

    reset_button = customtkinter.CTkButton(root.bottom_controls_frame, text='reset',font=customtkinter.CTkFont(size=15), command=reset)
    reset_button.grid(row=1,column=0,padx=20, pady=20,sticky = 'ew')
    
    start_button = customtkinter.CTkButton(root.bottom_controls_frame, text='start',font=customtkinter.CTkFont(size=15), command=start)
    start_button.grid(row=1,column=1,padx=20, pady=20,sticky = 'ew')
    
    save_path = StringVar()
    save_path.set('result.mp4')
    save_button = customtkinter.CTkButton(root.bottom_controls_frame, text='Save Path',font=customtkinter.CTkFont(size=15), command=lambda: file_select(
        save_path, (("image", "*.mp4"), ("all", "*")), True))
    save_button.grid(row=1,column=2,padx=20, pady=20,sticky = 'ew')
    
    bar = customtkinter.CTkProgressBar(root.bottom_controls_frame, mode="indeterminate")
    bar.grid(row=0, column=0, columnspan = 3, padx=20, pady=20, sticky = 'ew')

    root.mainloop()
