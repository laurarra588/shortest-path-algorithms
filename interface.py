import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from graph_loader import load_graph
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from utils import reconstruct_path, draw_path
import time


class ShortestPathGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Shortest Path")
        self.root.configure(bg="#1e1e2f")
        self.matrix = None
        self.last_path = None

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Segoe UI", 11))
        style.configure("TEntry", font=("Segoe UI", 11), padding=5)
        style.configure("TButton",
                        background="#4CAF50", foreground="white",
                        font=("Segoe UI", 11, "bold"), padding=6)
        style.map("TButton",
                  background=[("active", "#45a049")],
                  relief=[("pressed", "sunken"), ("!pressed", "raised")])

        self.frame = ttk.Frame(root, padding=20, style="TFrame")
        self.frame.grid()

        # Buttons and input
        self.btn_load = ttk.Button(self.frame, text="Load Graph", command=self.load_graph)
        self.btn_load.grid(column=0, row=0, columnspan=2, pady=5)

        ttk.Label(self.frame, text="🔵 Origin Vertex:").grid(column=0, row=1, sticky="e")
        self.entry_origin = ttk.Entry(self.frame, width=10)
        self.entry_origin.grid(column=1, row=1)

        ttk.Label(self.frame, text="🔴 Target Vertex:").grid(column=0, row=2, sticky="e")
        self.entry_target = ttk.Entry(self.frame, width=10)
        self.entry_target.grid(column=1, row=2)

        ttk.Button(self.frame, text="▶ Run Dijkstra",
                   command=lambda: self.run_algo(dijkstra, "Dijkstra")).grid(column=0, row=3, columnspan=2, pady=5)

        ttk.Button(self.frame, text="▶ Run Bellman-Ford",
                   command=lambda: self.run_algo(bellman_ford, "Bellman-Ford")).grid(column=0, row=4, columnspan=2, pady=5)

        ttk.Button(self.frame, text="📊 Show Path",
                   command=self.show_path).grid(column=0, row=5, columnspan=2, pady=5)

        self.output = tk.Text(self.frame, width=58, height=12, bg="#2b2b3a", fg="white",
                              insertbackground="white", relief="flat", borderwidth=8)
        self.output.grid(column=0, row=6, columnspan=2, pady=15)
        self.output.config(font=("Consolas", 11), wrap="word")

    def load_graph(self):
        path = filedialog.askopenfilename(filetypes=[["Text Files", "*.txt"]])
        if path:
            try:
                self.matrix = load_graph(path)
                messagebox.showinfo("Success", "Graph loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Could not load graph:\n{e}")

    def run_algo(self, algorithm, name):
        if not self.matrix:
            messagebox.showwarning("Warning", "Please load a graph first and then the algorithm.")
            return

        try:
            origin = int(self.entry_origin.get())
            target = int(self.entry_target.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid vertex numbers.")
            return

        try:
            start = time.time()
            dist, pred = algorithm(self.matrix, origin)
            elapsed = time.time() - start

            if dist[target] == float('inf'):
                result = f"{name} → No path found."
                self.last_path = None
            else:
                path = reconstruct_path(pred, target)
                self.last_path = path
                result = (
                    f"{name} Result:\n"
                    f"⏱️ Time: {elapsed:.4f} seconds\n"
                    f"💰 Cost: {dist[target]}\n"
                    f"🧭 Path: {path}"
                )
        except Exception as e:
            result = f"{name} → Error: {str(e)}"
            self.last_path = None

        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, result)

    def show_path(self):
        if self.matrix and self.last_path:
            draw_path(self.matrix, self.last_path, blink=True)
        else:
            messagebox.showwarning("Warning", "No path to display.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ShortestPathGUI(root)
    root.mainloop()
