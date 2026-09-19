import BookworkAutomatorDictsBackend as backend
import customtkinter as ctk

class app(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sparx Maths Bookwork Automator")
        self.geometry("400x300")
        frame = ctk.CTkFrame(self)
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        task = ctk.CTkLabel(frame, text=f"Task is: {backend.taskCounter}\nQuestion is: {backend.questionCounter}")
        task.grid(row=0, column=0, padx=10, pady=10)

        def new_task_command():
            task.configure(text=backend.increment_task())
        new_task = ctk.CTkButton(frame, text="New Task", command=new_task_command)
        new_task.grid(row=1, column=0, padx=10, pady=10)

        def new_answer_command():
            task.configure(text=backend.new_answer(new_answer.get()))
        new_answer = ctk.CTkEntry(frame, placeholder_text="New answer")
        new_answer.grid(row=2, column=0, padx=10, pady=10)
        new_answer.bind("<Return>", lambda event: new_answer_command())

        view_answer_frame = ctk.CTkFrame(frame)
        view_answer_frame.grid(row=3, column=0, padx=10, pady=10)
        view_answer_label = ctk.CTkLabel(view_answer_frame, text="Answer will appear here")
        view_answer_label.grid(row=4, column=0, padx=10, pady=10)
        view_answer = ctk.CTkEntry(view_answer_frame, placeholder_text="View answer")
        view_answer.grid(row=3, column=0, padx=10, pady=10)
        view_answer.bind("<Return>", lambda event: view_answer_label.configure(text=backend.view_answer(view_answer.get()[0], view_answer.get()[1].upper())))



app = app()
app.mainloop()

print(backend.bookwork)