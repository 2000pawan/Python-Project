from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector as sql

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "db"

con = sql.connect(
    host="localhost",
    user="root",
    password=mypass,
    port=3306,
    database=mydatabase,
    auth_plugin="mysql_native_password"
)
cur = con.cursor()

# Enter Table Name here
bookTable = "booktable"

# Global variable to keep track of the window instance and window status
view_window = None
window_open = False

def View():
    global view_window, window_open
    
    # If window is already open, destroy it before creating a new one
    if window_open and view_window is not None:
        try:
            view_window.destroy()  # Try to destroy the window if it's still open
        except:
            pass  # Ignore any errors if the window is already destroyed
        window_open = False  # Reset the window status
    
    # Create a new window if it's not open
    if not window_open:
        view_window = Tk()
        view_window.title("Library")
        view_window.minsize(width=400, height=400)
        view_window.geometry("600x500")

        Canvas1 = Canvas(view_window) 
        Canvas1.config(bg="#12a4d9")
        Canvas1.pack(expand=True, fill=BOTH)

        headingFrame1 = Frame(view_window, bg="#FFBB00", bd=5)
        headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

        headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier', 15))
        headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

        labelFrame = Frame(view_window, bg='black')
        labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

        Label(labelFrame, text="%-10s" % 'BID', bg='black', fg='white').place(relx=0.05, rely=0.1)
        Label(labelFrame, text="%-30s" % 'Title', bg='black', fg='white').place(relx=0.35, rely=0.1)
        Label(labelFrame, text="%-30s" % 'Author', bg='black', fg='white').place(relx=0.65, rely=0.1)

        Label(labelFrame, text="----------------------------------------------------------------------------", bg='black', fg='white').place(relx=0.05, rely=0.2)

        try:
            # Fetch the books from the database
            getBooks = "SELECT * FROM " + bookTable
            cur.execute(getBooks)
            books = cur.fetchall()

            y = 0.25  # starting position for first book
            for i in books:
                Label(labelFrame, text="%-10s" % (i[0]), bg='black', fg='white').place(relx=0.05, rely=y)
                Label(labelFrame, text="%-30s" % (i[1]), bg='black', fg='white').place(relx=0.35, rely=y)
                Label(labelFrame, text="%-30s" % (i[2]), bg='black', fg='white').place(relx=0.65, rely=y)
                y += 0.1

        except Exception as e:
            messagebox.showinfo("Failed to fetch files from database", f"Error: {str(e)}")

        quitBtn = Button(view_window, text="Quit", bg='#f7f1e3', fg='black', command=view_window.destroy)
        quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

        # Set the window status to open
        window_open = True
        view_window.mainloop()
