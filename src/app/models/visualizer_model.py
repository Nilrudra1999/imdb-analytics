"""------------------------------------------------------------------------------------------------
    Visualizer Model File - Takes machine learning model outputs and visualizes them
    --------------------------------------------------------------------------------------------
    Author: Nilrudra Mukhopadhyay
    Email: nilrudram@gmail.com
    Github: github.com/Nilrudra1999
------------------------------------------------------------------------------------------------"""
import matplotlib.pyplot as plt

BG_COLOR = "transparent"
PRIMARY_TEXT = "#b01756"
SECONDARY_TEXT = "#b42b68"
TILE_BG_COLOR = "#201d35"


class VisualizerModel():
    """
    Responsible for visualizing the outputs from machine learning models and presenting them to
    users in a clear and understandable manner. All revenue related metrics such as box-office,
    domestic or international gross will be presented in a line graph format with thresholds.
    Any ratings related metrics will be presented in a pie graph format.
    """
    def __init__(self) -> None:
        pass
    