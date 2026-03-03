"""------------------------------------------------------------------------------------------------
    Predictor View File - UI class for machine learning prediction screen
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from customtkinter import CTkFrame
from customtkinter import CTkButton
from customtkinter import CTkLabel
from customtkinter import CTkEntry

BG_COLOR = "transparent"
PRIMARY_TEXT = "#b01756"
SECONDARY_TEXT = "#b42b68"
TILE_BG_COLOR = "#201d35"
FOCUSED_BTN  = "#292450"
FORM_BTN_BG = "#110f24"
FORM_BTN_HOVER = "#090714"


class PredictorView(CTkFrame):
    """
    Predictor UI class inherited from Custom Tkinter Frame class, contains UI elements for 
    predicting the success of movies when presented with information. The view contains a form
    section to accept movie info and data visualization zone to display predictive analytics.
    """
    def __init__(self, controller, window) -> None:
        super().__init__(window, fg_color=BG_COLOR)
        self.controller = controller
        self.form = CTkFrame(self, fg_color=TILE_BG_COLOR, width=340, height=680)
        self.rev  = CTkFrame(self, fg_color=TILE_BG_COLOR, width=840, height=440)
        self.rtg  = CTkFrame(self, fg_color=TILE_BG_COLOR, width=840, height=220)
        
        self.dir_name_ebox = self.make_entry_box(self.form, "Enter Director Name")
        self.genre_name_ebox = self.make_entry_box(self.form, "Enter Genre Name")
        self.prod_bgt_ebox = self.make_entry_box(self.form, "Enter Production Budget")
        self.actor_name_ebox  = self.make_entry_box(self.form, "Enter Lead Actor Name")
        self.writer_name_ebox = self.make_entry_box(self.form, "Enter Writer Name")
        self.input_err_label  = self.make_label(self.form, "", 20, 260)
        self.users_msg_label  = self.make_label(self.form, "", 20, 260)

        self.make_prediction_btn = self.make_button(self.form, "Make Prediction",
            lambda: self.controller.predict_view_handle_making_prediction())
        self.clear_form_btn = self.make_button(self.form, "Clear Form",
            lambda: self.controller.predict_view_handle_clearing_form())
        self.go_back_btn = CTkButton(self, text="B\nA\nC\nK", font=("System", 26),
            text_color=PRIMARY_TEXT, fg_color=BG_COLOR, width=20, height=50, hover=False,
            command=lambda: self.controller.predict_view_handle_going_back())
        self.go_back_btn.bind("<Enter>", lambda e:
            self.go_back_btn.configure(fg_color=FOCUSED_BTN))
        self.go_back_btn.bind("<Leave>", lambda e:
            self.go_back_btn.configure(fg_color=BG_COLOR))
        self.set_view_widgets()
    
    
    
    # ---------- constructor helper ----------
    def set_view_widgets(self):
        self.form.pack_propagate(False)
        self.form.place(x=20, y=20)
        self.rev.pack_propagate(False)
        self.rev.place(x=380, y=20)
        self.rtg.pack_propagate(False)
        self.rtg.place(x=380, y=480)
        
        self.dir_name_ebox.pack(pady=(20, 0))
        self.genre_name_ebox.pack(pady=(10, 0))
        self.prod_bgt_ebox.pack(pady=(10, 0))
        self.actor_name_ebox.pack(pady=(10, 0))
        self.writer_name_ebox.pack(pady=(10, 0))
        self.input_err_label.pack(pady=(20, 0))
        
        self.make_prediction_btn.pack(pady=(20, 0))
        self.clear_form_btn.pack(pady=(10, 10))
        self.users_msg_label.pack(pady=(40, 0))
        self.go_back_btn.place(x=1233, y=20)
        
        
        
    # ---------- widget creation helpers ----------
    def make_label(self, root, text: str, font_size: int, wrap: int):
        return CTkLabel(
            master=root, text=text, font=("System", font_size),
            text_color=SECONDARY_TEXT, wraplength=wrap, justify="left"
        )
    
    
    def make_button(self, root, text: str, function):
        btn =  CTkButton(
            master=root, width=260, height=35, text=text,
            font=("Terminal", 18), text_color=PRIMARY_TEXT,
            fg_color=FORM_BTN_BG, hover=False, command=function
        )
        btn.bind("<Enter>", lambda e: btn.configure(fg_color=FORM_BTN_HOVER))
        btn.bind("<Leave>", lambda e: btn.configure(fg_color=FORM_BTN_BG))
        return btn
    
    
    def make_entry_box(self, root, placeholder: str):
        return CTkEntry(
            master=root, font=("System",18), placeholder_text=placeholder,
            placeholder_text_color=FOCUSED_BTN,
            text_color=SECONDARY_TEXT, fg_color=FORM_BTN_BG,
            border_color=FORM_BTN_BG, width=260, height=35
        )
    