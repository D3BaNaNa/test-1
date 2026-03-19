
def aperture_runner():
    system = platform.system()
    
    if system == "Windows":
        path = "./Aperture.exe"
    elif system == "Darwin":  # macOS
        path = "./Aperture.app"
    else:  # Linux and other Unix-like systems
        path = "./Aperture"
    
    if os.path.exists(path):
        if system == "Windows":
            subprocess.run([path])
        elif system == "Darwin":
            subprocess.run(["open", "-a", path])
        else:
            subprocess.run([path])
    else:
        print(f"Aperture file not found at {path}")

def server_send(content_type, content):
    data = {"type": content_type, "content": content}
    json_data = json.dumps(data)
    byte_data = json_data.encode('utf-8')
    length = len(byte_data)
    
    message = f"{length}\n{json_data}"
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8080))
    sock.send(message.encode('utf-8'))
    sock.close()

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
        server_send("UI_show", "main.py_line10")
        server_send("UI_show", "main.py_line16")
        
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
            server_send("UI_show", f"main.py_line{16 + row * 4 + col}")
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
                server_send("add_popup", f"Result: {result}")
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
                server_send("add_popup", "Error in calculation")