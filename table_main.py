import customtkinter as ctk
import pyodbc
import tkinter

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("500x500")
app.title("CREATE TABLE")

entry_table_name = ctk.CTkEntry(app, placeholder_text="TABLE NAME", width=190)
entry_table_name.place(relx=0.1, rely=0.1)

entry_column1 = ctk.CTkEntry(app, placeholder_text="COLUMN_1", width=190)
entry_column1.place(relx=0.1, rely=0.2)

entry_column2 = ctk.CTkEntry(app, placeholder_text="COLUMN_2", width=190)
entry_column2.place(relx=0.1, rely=0.3)

entry_column3 = ctk.CTkEntry(app, placeholder_text="COLUMN_3", width=190)
entry_column3.place(relx=0.1, rely=0.4)


def create():
    try:
        connection = pyodbc.connect(
            "DRIVER={SQL SERVER};"
            "Server=HP\\SQLEXPRESS;"
            "Database=caldb;"  # Add a semicolon after Database name
            "Trusted_Connection=True"
        )

        connection.autocommit = True
        sql_create_table = (
            f"CREATE TABLE {entry_table_name.get()} ("
            f"{entry_column1.get()} {radio_var_col1.get()}, "
            f"{entry_column2.get()} {radio_var_col2.get()}, "
            f"{entry_column3.get()} {radio_var_col3.get()}"
            ")"
        )
        connection.execute(sql_create_table)
        info_label.configure(text="Table Created")
    except pyodbc.Error as ex:
        print("Error:", ex)
        info_label.configure(text="Error: Table Creation Failed")


create_button = ctk.CTkButton(app, text="CREATE", command=create)
create_button.place(relx=0.1, rely=0.5)

radio_var_col1 = tkinter.StringVar(value="")
col1_rd_varchar50 = ctk.CTkRadioButton(
    app, text="varchar(50)", variable=radio_var_col1, value="varchar(50)"
)
col1_rd_varchar50.place(relx=0.5, rely=0.2)

col1_rd_int = ctk.CTkRadioButton(
    app, text="Integer", variable=radio_var_col1, value="Integer"
)
col1_rd_int.place(relx=0.7, rely=0.2)

radio_var_col2 = tkinter.StringVar(value="")
col2_rd_varchar50 = ctk.CTkRadioButton(
    app, text="varchar(50)", variable=radio_var_col2, value="varchar(50)"
)
col2_rd_varchar50.place(relx=0.5, rely=0.3)

col2_rd_int = ctk.CTkRadioButton(
    app, text="Integer", variable=radio_var_col2, value="Integer"
)
col2_rd_int.place(relx=0.7, rely=0.3)

radio_var_col3 = tkinter.StringVar(value="")
col3_rd_varchar50 = ctk.CTkRadioButton(
    app, text="varchar(50)", variable=radio_var_col3, value="varchar(50)"
)
col3_rd_varchar50.place(relx=0.5, rely=0.4)

col3_rd_int = ctk.CTkRadioButton(
    app, text="Integer", variable=radio_var_col3, value="Integer"
)
col3_rd_int.place(relx=0.7, rely=0.4)

info_label = ctk.CTkLabel(app, text="datadb")
info_label.place(relx=0.1, rely=0.6)

app.mainloop()
