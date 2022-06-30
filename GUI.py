from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import KMeans_Calc
import Preprocessing
import chart_studio.plotly as py
from PIL import ImageTk, Image


class KMeansClustering:

    def __init__(self, master):
        master.title("K Means Clustering")
        master.geometry('1450x700')

        py.sign_in('rubil', '7J0jCcvRv7HTq0cCvff4')
        self.preprocessing = Preprocessing.Preprocessing()
        self.kmeans = KMeans_Calc.KMeans_Calc()

        # path choosing
        self.path = StringVar()
        self.lbl_path = Label(window, text="Choose path:")
        self.lbl_path.grid(column=0, row=0)
        self.txt_path = Entry(window, width=40, textvariable=self.path, state="disabled")
        self.txt_path.grid(column=1, row=0)
        self.btn_path = Button(window, text="Browse", command=lambda: self.clicked_browse())
        self.btn_path.grid(column=2, row=0)
        self.txt_path.update()

        # label for Number of clusters k
        self.lbl_num_clusters = Label(window, text="Number of clusters k:")
        self.lbl_num_clusters.grid(column=0, row=1)
        self.txt_num_clusters = Entry(window, width=40)
        self.txt_num_clusters.grid(column=1, row=1)

        # label for Number of runs
        self.lbl_num_runs = Label(window, text="Number of runs:")
        self.lbl_num_runs.grid(column=0, row=2)
        self.txt_num_runs = Entry(window, width=40)
        self.txt_num_runs.grid(column=1, row=2)

        self.btn_pre_process = Button(window, text="Pre-process", command=lambda: self.clicked_pre_process())
        self.btn_cluster = Button(window, text="Cluster", command=lambda: self.clicked_cluster(self.txt_num_clusters, self.txt_num_runs))

        self.btn_pre_process.grid(column=0, row=3)
        self.btn_cluster.grid(column=1, row=3)

    def clicked_pre_process(self):
        res = self.preprocessing.pre_process()
        if res == False:
            messagebox.showerror(title="K Means Clustering", message="Error while preprocessing.")
        else:
            messagebox.showinfo(title="K Means Clustering", message="Preprocessing completed successfully!")

    def clicked_pre_process_after_cluster(self):
        res = self.preprocessing.pre_process()
        if res == False:
            messagebox.showerror(title="K Means Clustering", message="Error while preprocessing.")

    def clicked_cluster(self, num_of_clusters, num_of_runs):
        try:
            num_of_clusters = int(num_of_clusters.get())
            num_of_runs = int(num_of_runs.get())
        except Exception as e:
            messagebox.showerror(title="K Means Clustering", message="Error: invalid number of clusters or number of runs.")
            return
        if self.preprocessing.get_grouped_df() is None:
            messagebox.showwarning(title="K Means Clustering", message="Warning: Preprocessing has not been done on the data.")
        else:
            if len(self.preprocessing.get_grouped_df().columns) > 14:
                self.clicked_pre_process_after_cluster()
            res = self.kmeans.calc_k_means(self.preprocessing.get_grouped_df(), num_of_clusters, num_of_runs)
            if "Error" in res:
                messagebox.showerror(title="K Means Clustering", message=res)
            else:
                scatter_plt, fig = self.kmeans.plot_scatter()
                # presenting the charts
                py.image.save_as(fig, filename='fig.png')
                scatter_plt.savefig('scatter.png')
                scatter_plt.close()

                char_photo = ImageTk.PhotoImage(Image.open("fig.png"))
                ch_label = Label(window, image=char_photo)
                ch_label.image = char_photo
                ch_label.grid(padx=20, row=4, columnspan=2, column=0)

                scatter_photo = ImageTk.PhotoImage(Image.open("scatter.png"))
                scatter_label = Label(window, image=scatter_photo)
                scatter_label.image = scatter_photo
                scatter_label.grid(row=4, columnspan=2, column=5)

                messagebox.showinfo(title="K Means Clustering", message="Clustering process is done successfully!")



    def clicked_browse(self):
        path = filedialog.askopenfile(mode='rb', title='K Means Clustering', filetypes=(("Excel files", "*.xlsx"),))
        if path is None:
            messagebox.showerror(title="K Means Clustering", message="Error: Please choose a path.")
            return
        self.path.set(path.name)
        res = self.preprocessing.load_dataset_to_df(self.path.get())
        if res == False:
            messagebox.showerror(title="K Means Clustering", message="Error while trying to open data file: \n" + self.path.get())



window = Tk()

myGUI = KMeansClustering(window)



window.mainloop()
