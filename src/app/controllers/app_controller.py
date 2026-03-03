"""------------------------------------------------------------------------------------------------
    Main App Controller File - Controls the event logic and execution flow for the app
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
from re import match
from customtkinter import CTk
from views.home_view import HomeView
from views.predictor_view import PredictorView
from models.visualizer_model import VisualizerModel
from models.predictor_model import PredictorModel

BG_COLOR_LIGHT = "#28253b"
BG_COLOR_DARK  = "#13121e"


class AppController:
    """
    Initializes a Tkinter root object, and a dictionary of inherited Tkinter Frame objects
    decorated with various widgets. The controller connects the views to the event logic used
    by the app, which connects to the models to maintain the business logic thus, acting like
    a bridge between the views and the models.
    """
    def __init__(self) -> None:
        self.__window = CTk()
        self.__window.title("Film Success Predictor")
        self.__window.geometry("1280x720")
        self.__window.resizable(width=False, height=False)
        self.__window.configure(fg_color=(
            BG_COLOR_LIGHT,
            BG_COLOR_DARK
        ))
        self.__views = {
            "home view": HomeView(self, self.get_window()),
            "predictor view": PredictorView(self, self.get_window()),
        }
        self.predictor  = PredictorModel()
        self.visualizer = VisualizerModel()
    
    
    # ---------- main application methods ----------
    def get_window(self):
        return self.__window

    
    def launch(self):
        self.__views["home view"].pack(expand=True, fill="both")
        self.__window.mainloop()
    
    

    # ---------- button event methods ----------
    def home_view_handle_changing_views(self):
        self.__views["home view"].pack_forget()
        self.__views["predictor view"].pack(expand=True, fill="both")
    

    def predict_view_handle_going_back(self):
        self.__views["predictor view"].pack_forget()
        self.__views["home view"].pack(expand=True, fill="both")
        
    
    def predict_view_handle_clearing_form(self):
        view = self.__views["predictor view"]
        view.dir_name_ebox.delete(0, "end")
        view.genre_name_ebox.delete(0, "end")
        view.prod_bgt_ebox.delete(0, "end")
        view.actor_name_ebox.delete(0, "end")
        view.writer_name_ebox.delete(0, "end")
        self.helper_clear_form_errors(view)
        
    
    def predict_view_handle_making_prediction(self):
        view = self.__views["predictor view"]
        valid = True
        error_text = "ERROR: Add valid responses to highlighted boxes."
        error_text = error_text + " Only enter valid names or numbers/decimals."
        re_name = r"^[A-Za-z\s\-\']+$"
        re_num = r"^\d+(\.\d{1,2})?$"
        self.helper_clear_form_errors(view)
        valid = self.helper_validate_input(view.dir_name_ebox, re_name) and valid
        valid = self.helper_validate_input(view.genre_name_ebox, re_name) and valid
        valid = self.helper_validate_input(view.prod_bgt_ebox, re_num) and valid
        valid = self.helper_validate_input(view.actor_name_ebox, re_name) and valid
        valid = self.helper_validate_input(view.writer_name_ebox, re_name) and valid
        if not valid:
            view.input_err_label.configure(text=error_text)
            return
        user_msg_text = "Making predictions please wait, this takes some time"
        view.users_msg_label.configure(text=user_msg_text)
    
    
    
    # ---------- application wide helper methods ----------
    def helper_clear_form_errors(self, view):
        view.input_err_label.configure(text="")
        view.users_msg_label.configure(text="")
        view.dir_name_ebox.configure(border_color="#110f24")
        view.genre_name_ebox.configure(border_color="#110f24")
        view.prod_bgt_ebox.configure(border_color="#110f24")
        view.actor_name_ebox.configure(border_color="#110f24")
        view.writer_name_ebox.configure(border_color="#110f24")
    
    
    def helper_validate_input(self, input_box, regex):
        valid = match(regex, input_box.get().strip())
        if not valid:
            input_box.configure(border_color="#b42b68")
        return valid
