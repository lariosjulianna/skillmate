import mysql.connector
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox, Tk, Label, Button

# Make a connection to your MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Skillmate1!",
    database="FinanceTracker",
    auth_plugin='mysql_native_password'
)
 # test
