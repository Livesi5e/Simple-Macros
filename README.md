# Simple Macros
 A simple program in python to create and use your own macros. The hotkeys work globally.
 This program is still in development and has some quirks. Most of them are fixed via saving and restarting the application.

## License
 This software is licensed under the GNU GPL-3.0 license. What this does read [here](https://github.com/Livesi5e/Simple-Macros/blob/main/LICENSE)

## Dependencies
 If you want to work on this yourself you need to have these libraries installed:
 - PySimpleGUI (pip install PySimpleGUI)
 - pyautogui (pip install pyautogui)
 - keyboard (pip install keyboard)

## Usage

After opening the program you have a list of your macros. Beneath the list you have some buttons for navigating. While having an entry selected you can delete it with 'Delete'. Currently you need to restart the program to deactivate the hotkey. With 'Run' you can run your Macro without using your hotkey. 'Load' and 'Save' are used to load and save .macros files wich stores your macros. To create a new macro, press 'New'

![New](https://user-images.githubusercontent.com/109060918/203250211-75912fbf-57ea-4165-bcb8-53258afd75bc.png)

It then opens up the menu for creating new Macros. At first you need to choose a type of input you want to simulate

![Input Type](https://user-images.githubusercontent.com/109060918/203250818-c3d8a64a-f63b-4dd0-8ee3-2f127d15f6f2.png)

Let's say you've chosen 'Mouse Movement'. After that your menu looks like this and wants a x and y coordinate. You can look them up i.e. with taking a screenshot and look at it in Paint. I'm working on providing a way to also see it in the program itself but that's not finished til now.

![MM](https://user-images.githubusercontent.com/109060918/203252222-fe224ede-f992-4faa-b3c4-a5be04980674.png)

Now I've added a mouse movement to 1, 1, wich is in the top left of the screen. In 'Current Macro' you now have a list containing your added steps. Beneath it you have 'Create' which finishes the process and adds the new macro. The white box is where the name of the macro is entered. With 'Hotkey' you add the hotkey to the macro. It opens a little window and listens to your inputs. After pressing 'Finished' the window closes and your selected hotkey appears next to the button 'Hotkey'. 'Delete' deletes the selected entry. 

![Hotkey](https://user-images.githubusercontent.com/109060918/203256105-63bd3b70-0707-4261-9c17-de12e6117fff.png)

![set](https://user-images.githubusercontent.com/109060918/203256118-04056b2a-a0e0-4889-b0ee-3bdfdb0ceb0d.png)

We can now enter a name and hit create to finish making the macro. If you want to add more to it, just select the type on the left and redo the steps above. If you're happy with what you have, hit 'Create'. But be careful. Without knowing how savefiles work, you have no way of changing your macros. You'll need to start from scratch if you've made a mistake.

![Create](https://user-images.githubusercontent.com/109060918/203257130-e8d69c6d-956c-4d88-8077-5498a4708069.png)

Now you have a new entry in your macro list and can use it globally. If you've found bugs or have some ideas you can use the GitHub [Bugreports](https://github.com/Livesi5e/Simple-Macros/issues) to submit them.
