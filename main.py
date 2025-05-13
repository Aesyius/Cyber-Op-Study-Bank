import tkinter as tk
import os
import random

class FKSAStudyBank:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("FKSA Study Bank")
        
        self.window.geometry("800x300")
        self.window.resizable(False,False)

        # self.window.bind("<Configure>", self._resizeWindow)

        # GUI
        # Question Frame
        self.questionFrame = tk.Frame(self.window)
        self.questionFrame.grid(row=0,sticky="nw") 

        # Answer Frame
        self.answerFrame = tk.Frame(self.window)
        self.answerFrame.grid(row=1,sticky="nw") 

        # Button Frame
        self.buttonFrame = tk.Frame(self.window, height=50, width=200)
        self.buttonFrame.place(x=800, y=300, anchor="se")
        # self.buttonFrame.grid(row=2,sticky="se") 
          
        self._menubar()
        self._buttons()
        
        # Retrieve filepath
        self.assetPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "asset")
        self.assetFolders = [f for f in os.listdir(self.assetPath) if os.path.isdir(os.path.join(self.assetPath, f))]

        self.currentQuestion = None
        self.currentAnswer = None


        # main loop
        self.window.mainloop()

# ==================== GUI BEGIN ====================

    def _menubar(self):
        # Menu Bar
        menubar = tk.Menu(self.window)
        
        # Menu bar - File
        file = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label="File", menu = file)
        file.add_command(label="Topic Selector", command=self._topicSelector)

        # Menu bar - Help   
        help = tk.Menu(menubar, tearoff = 0)
        menubar.add_cascade(label="Help", menu = help)
        help.add_command(label="What do I do with all this?", command=self._placeholder)
        
        self.window.config(menu = menubar)

    def _buttons(self):

        self.randomize_button = tk.Button(self.buttonFrame, text="Randomize", command=self._randomizeQuestion)
        self.randomize_button.grid(row=1,column=0, padx=5)
        
        self.reveal_button = tk.Button(self.buttonFrame, text="Reveal", command=self._revealAnswer)
        self.reveal_button.grid(row=1,column=1, padx=5)


    # Topic selector window for the menu bar
    def _topicSelector(self):
        
        questionTopics = self.assetFolders
        
        self.topicState = {} # Empty dictionary to store state for on/off for toggling

        def selectAll():
            state = selectAllVar.get()
            for each in self.topicState.values():
                each.set(state)

        # Configures top window

        top = tk.Toplevel(self.window)
        top.title("Topic Selector")
        top.config(padx=10,pady=10)

        # Frame for select all

        selectAllFrame = tk.Frame(top)
        selectAllFrame.grid(sticky="nw", pady=20)

        # Frame for topics
        
        topicFrame = tk.Frame(top)
        topicFrame.grid()

        # Frame for confirm button
        
        confirmButtonFrame = tk.Frame(top)
        confirmButtonFrame.grid()
        
        # Confirm button
        confirmButton = tk.Button(top,text="Confirm",command=top.destroy)
        confirmButton.grid(sticky="se")        
        
        # Select all
        
        selectAllVar = tk.BooleanVar()
        selectAllButton = tk.Checkbutton(selectAllFrame, text= "Select All",variable=selectAllVar, command=selectAll)
        selectAllButton.grid()

        # Loops through all topics in assetFolders list, display it in window.
        for index, each in enumerate(sorted(questionTopics)):
            
            # Builds grid
            row = index // 3
            column = index % 3

            # Displays check buttons

            var = tk.BooleanVar()

            topicButton = tk.Checkbutton(topicFrame, text=each, variable=var)
            topicButton.grid(row= row, column= column, sticky="w")
            
            self.topicState[each] = var

        

# ==================== GUI END ==================== 

# ==================== FUNCTIONALITY BEGIN ====================

    def _questionDisplay(self, arg):
        # Chooses at random, the topics selected in the selector. Then chooses the questions?   

        if arg:

            if self.currentQuestion:
                self.currentQuestion.destroy()

            with open(arg, "r") as file:
                question = file.read()
            
            self.currentQuestion = tk.Label(self.questionFrame, text=question,wraplength=self.window.winfo_width(),justify="left")
            self.currentQuestion.grid(padx=20,pady=20,sticky="nw")
        
        else:
            pass  

    def _randomizeQuestion(self):
        
        # Builds list of all the topics selected
        try:
            selectedTopics = [topic for topic, var in self.topicState.items() if var.get()]
            
            if not selectedTopics:
                self._generateWindow(title="Error!",
                                 content=f"No topic selected",
                                 buttonText="Oh no!")
                
                
                # top = tk.Toplevel(self.window)
                # top.title("Error!")
                # top.config(padx=10,pady=10)
                # topText = tk.Label(top, text=f"No topics selected")
                # topText.pack()
                # button = tk.Button(top,text="Oh no!", command=top.destroy)
                # button.pack(pady=10)
            
            else:
                # Creates path to the selected topics
                questionFolder = os.path.join(self.assetPath, random.choice(selectedTopics))
                questionFolderList = os.listdir(os.path.join(questionFolder,"Questions"))
                questionChoice = random.randrange(1, len(questionFolderList))
        
                randomQuestionFullPath = os.path.join(questionFolder,"Questions", "Question"+str(questionChoice)+".txt")
                randomAnswerFullPath = os.path.join(questionFolder,"Answers", "Answer"+str(questionChoice)+".txt")
                
                self._questionDisplay(randomQuestionFullPath)
                self._answerDisplay(randomAnswerFullPath)
                
                
        except Exception as e:
            self._generateWindow(title="Error!",
                                 content=f"No topic selected\n{e}",
                                 buttonText="Oh no!")


        # except Exception as e:
        #     top = tk.Toplevel(self.window)
        #     top.title("Error!")
        #     top.config(padx=10,pady=10)
        #     topText = tk.Label(top, text=f"No topics selected")
        #     topText.pack()
        #     button = tk.Button(top,text="Oh no!", command=top.destroy)
        #     button.pack(pady=10)

        #     print(e)
            

    def _answerDisplay(self, arg):
        if arg:

            if self.currentAnswer:
                self.currentAnswer.destroy()

            with open(arg, "r") as file:
                question = file.read()
            
            self.currentAnswer = tk.Label(self.answerFrame, text=question,wraplength=self.window.winfo_width()-100,justify="left")
            self.currentAnswer.grid()
            self.currentAnswer.grid_forget()
        
        else:
            pass 


    def _revealAnswer(self):
        self.currentAnswer.grid(padx=20,pady=20,sticky="nsew")
        pass

    def _placeholder(self):
        print("_placeholder - it works!")
        pass

    def _generateWindow(self, **kwargs):
        """
        Generates a window 1 button window to fill with content
        
        Keyword Args:
            title (str): Title text for the window.
            content (str): Main content or message to display.
            buttonText (str): Label text for the button.
        """
        
        
        title = kwargs.get("title")
        label = kwargs.get("content")
        buttonText = kwargs.get("buttonText")

        top = tk.Toplevel(self.window)
        top.title(title)    
        top.config(padx=10,pady=10)

        topText = tk.Label(top, text=label)
        topText.pack()

        button = tk.Button(top,text=buttonText, command=top.destroy)
        button.pack(pady=10)






    # def _resizeWindow(self,event):
    #     width = event.width
    #     height = event.height

    #     if self.currentQuestion:
    #         self.currentQuestion.config(wraplength=width)

# ==================== FUNCTIONALITY END ====================

FKSAStudyBank()
