import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Display
        self.display = tk.Entry(root, font=('Arial', 20), bd=10, 
                               insertwidth=2, width=14, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        row = 1
        col = 0
        
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(root, text=button, width=5, height=2, font=('Arial', 14),
                     command=cmd).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def click(self, key):
        if key == '=':
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
                self.expression = result
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        elif key == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        else:
            self.expression += str(key)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
