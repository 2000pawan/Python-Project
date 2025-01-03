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

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "booktable"

# List To store all Book IDs
allBid = [] 

def issue():
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid = inf1.get().strip()  # Get Book ID
    issueto = inf2.get().strip()  # Get student name

    allBid.clear()  # Clear the list of book IDs

    try:
        # Fetch all Book IDs from bookTable
        extractBid = f"SELECT bid FROM {bookTable}"
        cur.execute(extractBid)
        allBid.extend([str(i[0]) for i in cur.fetchall()])

        if bid not in allBid:
            messagebox.showinfo("Error", "Book ID not present")
            return

        # Check availability of the book
        checkAvail = f"SELECT status_book FROM {bookTable} WHERE bid = %s"
        cur.execute(checkAvail, (bid,))
        result = cur.fetchone()

        if not result:
            messagebox.showinfo("Error", "Book ID not found")
            return

        check = result[0]
        if check != 'avail':
            messagebox.showinfo("Message", "Book Already Issued or Not Available")
            return

        # Issue the book (Insert into books_issued table)
        issueSql = f"INSERT INTO {issueTable} (bid, issue_to) VALUES (%s, %s)"
        updateStatus = f"UPDATE {bookTable} SET status_book = 'issued' WHERE bid = %s"

        cur.execute(issueSql, (bid, issueto))  # Insert the issue record
        cur.execute(updateStatus, (bid,))  # Update the book's status to 'issued'
        con.commit()  # Commit the changes to the database

        messagebox.showinfo('Success', "Book Issued Successfully")  # Success message
    except Exception as e:
        messagebox.showinfo("Error", f"Error occurred: {str(e)}")  # Error message
    finally:
        root.destroy()  # Close the window after completing the operation


def issueBook(): 
    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    # Book ID
    lb1 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    # Issued To Student name 
    lb2 = Label(labelFrame, text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    # Issue Button
    issueBtn = Button(root, text="Issue", bg='#d1ccc0', fg='black', command=lambda: issue())
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # Quit Button
    quitBtn = Button(root, text="Quit", bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()