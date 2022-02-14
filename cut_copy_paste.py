import tkinter

def make_textmenu(root, ttk):
	global the_menu
	the_menu = ttk.Menu(root, tearoff=0)
	the_menu.add_command(label="Cut")
	the_menu.add_command(label="Copy")
	the_menu.add_command(label="Paste")


def show_textmenu(event):
	e_widget = event.widget
	the_menu.entryconfigure("Cut",command=lambda: e_widget.event_generate("<<Cut>>"))
	the_menu.entryconfigure("Copy",command=lambda: e_widget.event_generate("<<Copy>>"))
	the_menu.entryconfigure("Paste",command=lambda: e_widget.event_generate("<<Paste>>"))
	the_menu.tk.call("tk_popup", the_menu, event.x_root, event.y_root)


