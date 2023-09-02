import tkinter as tk
from tkinter import filedialog
from blind_watermark import WaterMark

class WatermarkGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("水印嵌入与提取工具")
        
        self.label = tk.Label(root, text="选择操作：")
        self.label.pack(pady=10)
        
        self.operation_var = tk.StringVar(value="添加")
        self.operation_radio_frame = tk.Frame(root)
        self.add_radio = tk.Radiobutton(self.operation_radio_frame, text="添加", variable=self.operation_var, value="添加")
        self.extract_radio = tk.Radiobutton(self.operation_radio_frame, text="提取", variable=self.operation_var, value="提取")
        self.add_radio.pack(side=tk.LEFT, padx=10)
        self.extract_radio.pack(side=tk.LEFT, padx=10)
        self.operation_radio_frame.pack()
        
        self.word_label = tk.Label(root, text="水印内容：")
        self.word_label.pack(pady=5)
        
        self.word_entry = tk.Entry(root)
        self.word_entry.pack(pady=5)
        
        self.in_fi_label = tk.Label(root, text="原图路径：")
        self.in_fi_label.pack(pady=5)
        
        self.in_fi_entry = tk.Entry(root)
        self.in_fi_entry.pack(pady=5)
        
        self.in_fi_browse_button = tk.Button(root, text="浏览", command=self.browse_input_image)
        self.in_fi_browse_button.pack()
        
        self.out_fi_label = tk.Label(root, text="输出路径（添加操作）：")
        self.out_fi_label.pack(pady=5)
        
        self.out_fi_entry = tk.Entry(root)
        self.out_fi_entry.pack(pady=5)
        
        self.out_fi_browse_button = tk.Button(root, text="浏览", command=self.browse_output_image)
        self.out_fi_browse_button.pack()
        
        self.len_wm_label = tk.Label(root, text="水印长度：")
        self.len_wm_label.pack(pady=5)
        
        self.len_wm_result_var = tk.StringVar(value="")
        self.len_wm_result_entry = tk.Entry(root, textvariable=self.len_wm_result_var, state="readonly")
        self.len_wm_result_entry.pack(pady=5)
        
        self.fi_label = tk.Label(root, text="图片路径（提取操作）：")
        self.fi_label.pack(pady=5)
        
        self.fi_entry = tk.Entry(root)
        self.fi_entry.pack(pady=5)
        
        self.fi_browse_button = tk.Button(root, text="浏览", command=self.browse_image)
        self.fi_browse_button.pack()
        
        self.submit_button = tk.Button(root, text="执行", command=self.execute_operation)
        self.submit_button.pack(pady=10)
        
        self.operation_var.trace_add("write", self.update_elements_state)  # 追踪操作选择的变化
        
    def update_elements_state(self, *args):
        operation = self.operation_var.get()
        if operation == "添加":
            self.len_wm_result_var.set("")
            self.len_wm_result_entry.config(state="normal")
            self.fi_entry.config(state="disabled")
        elif operation == "提取":
            self.len_wm_result_var.set("")
            self.len_wm_result_entry.config(state="normal")
            self.fi_entry.config(state="normal")
        
    def add_watermark(self, word, in_fi, out_fi):
        bwm1 = WaterMark(password_img=1, password_wm=1)
        bwm1.read_img(in_fi)
        bwm1.read_wm(word, mode='str')
        bwm1.embed(out_fi)
        len_wm = len(bwm1.wm_bit)
        self.len_wm_result_var.set(len_wm)  # 更新水印长度显示
        print(f'暗水印的长度(宽)为 {len_wm}')
        
    def browse_input_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        self.in_fi_entry.delete(0, tk.END)
        self.in_fi_entry.insert(0, file_path)
        
    def browse_output_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        self.out_fi_entry.delete(0, tk.END)
        self.out_fi_entry.insert(0, file_path)
        
    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")])
        self.fi_entry.delete(0, tk.END)
        self.fi_entry.insert(0, file_path)
        
    def execute_operation(self):
        operation = self.operation_var.get()
        if operation == "添加":
            word = self.word_entry.get()
            in_fi = self.in_fi_entry.get()
            out_fi = self.out_fi_entry.get()
            self.add_watermark(word, in_fi, out_fi)
        elif operation == "提取":
            fi = self.fi_entry.get()
            self.extract_watermark(fi)
            
    def extract_watermark(self, fi):
        bwm1 = WaterMark(password_img=1, password_wm=1)
        wm_extract = bwm1.extract(filename=fi, wm_shape=None, mode='str')
        print(wm_extract)

if __name__ == '__main__':
    root = tk.Tk()
    app = WatermarkGUI(root)
    root.mainloop()