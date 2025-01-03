from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import mysql.connector as sql


# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = sql.connect(
    host="localhost",
    user="root",
    password="root",
    port=3306,
    database=mydatabase,
    auth_plugin="mysql_native_password"
)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" #Issue Table
bookTable = "booktable" #Book Table

allBid = [] #List To store all Book IDs

def returnn():
    global SubmitBtn, labelFrame, lb1, bookInfo1, quitBtn, root, Canvas1, status

    bid = bookInfo1.get().strip()  # Ensure no leading/trailing spaces
    allBid.clear()  # Clear the list before reusing

    try:
        # Fetch all Book IDs from the issue table
        extractBid = "SELECT bid FROM " + issueTable
        cur.execute(extractBid)
        allBid.extend([str(i[0]) for i in cur.fetchall()])
        
        if bid in allBid:
            # Check availability in bookTable
            checkAvail = "SELECT status_book FROM " + bookTable + " WHERE bid = %s"
            cur.execute(checkAvail, (bid,))
            result = cur.fetchone()

            if result:
                check = result[0]
                if check == 'issued':
                    status = True
                else:
                    status = False
            else:
                raise ValueError("Book ID not found in bookTable.")
        else:
            messagebox.showinfo("Error", "Book ID not present in issue table.")
            return

    except Exception as e:
        messagebox.showinfo("Error", f"Can't fetch Book IDs: {str(e)}")
        return

    # If book is issued, process the return
    issueSql = "DELETE FROM " + issueTable + " WHERE bid = %s"
    updateStatus = "UPDATE " + bookTable + " SET status_book = 'avail' WHERE bid = %s"

    try:
        if bid in allBid and status:
            cur.execute(issueSql, (bid,))
            con.commit()
            cur.execute(updateStatus, (bid,))
            con.commit()
            messagebox.showinfo('Success', "Book Returned Successfully")
        else:
            messagebox.showinfo('Message', "Please check the book ID")
    except Exception as e:
        messagebox.showinfo("Error", f"Error in returning book: {str(e)}")
    finally:
        allBid.clear()
        root.destroy()

def returnBook(): 
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()