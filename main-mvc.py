from tkinter import *

from controllers.publisher import PublisherController
from models.publisher import Publisher
from views.publisher import PublisherView

if __name__ == '__main__':
    root = Tk()
    view = PublisherView(root)
    model = Publisher()
    controller = PublisherController(model, view)
    root.mainloop()