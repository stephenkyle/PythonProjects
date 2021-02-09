# This program converts temperatures to and from
# Fahrenheit and Celsius

import tkinter

class TempConverterGUI:
    def __init__(self):

        # Create the main window
        self.main_window = tkinter.Tk()

        # Create three frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame,
                                                   text = 'Enter the termperature:')
        self.temp_entry = tkinter.Entry(self.top_frame,
                                                 width=10)
        # Pack the top frame's widgets
        self.prompt_label.pack(side='left')
        self.temp_entry.pack(side='left')

        # Create the widgets for the middle frame
        self.descr_label = tkinter.Label(self.mid_frame,
                                                  text='Converted to:')
        # Create a StringVar object to associate with output label
        self.value = tkinter.StringVar()

        # Create a label and associate it with StringVar object
        self.temp_label = tkinter.Label(self.mid_frame,
                                                 textvariable=self.value)

        # Pack the middle frame's widgets
        self.descr_label.pack(side='left')
        self.temp_label.pack(side='left')

        # Create the button widgets for the bottom frame
        self.far_calc_button = tkinter.Button(self.bottom_frame,
                                                       text='Convert to Celsius',
                                                       command=self.far_convert)
        self.cel_calc_button = tkinter.Button(self.bottom_frame,
                                                       text='Conver to Farenheit',
                                                       command=self.cel_convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                                   text='Quit',
                                                   command=self.main_window.destroy)

        # Pack the bottom frame widgets
        self.far_calc_button.pack(side='left')
        self.cel_calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

    # This conversion is a callback for the Convert to Celsius button
    def far_convert(self):
        
        farenheit = float(self.temp_entry.get())
        celsius = (farenheit-32)*(5/9)
        self.value.set(celsius)

    # This conversion is a callbacl for the Convert to Farenheit button
    def cel_convert(self):
        celsius = float(self.temp_entry.get())
        farenheit = (celsius*(9/5))+32
        self.value.set(farenheit)

# Create an instance of the TempConverterGUI class
temp_conv = TempConverterGUI()

# Stephen Oakford
                                                
    
