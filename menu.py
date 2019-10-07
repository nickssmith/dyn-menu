import sys
import curses
from curses import panel
import csv
import os

global target
target = ""

global current_title
current_title = ""

global title_to_cmd
title_to_cmd = dict()

class Menu(object):

    def __init__(self, items, stdscreen):
        #TODO auto detect letters and bind letter to the item
        # make new container auto turned into
        # [m]ake new container

        self.window = stdscreen.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        self.panel.hide()
        panel.update_panels()
        global target
        self.target = target

        self.position = 0

        #get numbers to exectue
        self.numbers_to_listen_to = list(range(1,len(items)+2))
        self.letters_to_listen_to = []

        self.temp_items = []
        for item in items:
            i = 0
            title = item[0]
            next_item = False
            for letter in title:

                if letter not in set(self.letters_to_listen_to) and not next_item:
                    self.letters_to_listen_to.append(letter.lower())

                    new_title = str(title[:i])+"["+letter+"]"+str(title[i+1:])
                    self.temp_items.append((new_title,item[1]))


                    next_item = True
                    break
                i+=1

        self.items = self.temp_items

        runner = sys_runner()
        self.items.append(('exit',runner.exit))

    def navigate(self, n):
        self.position += n
        if self.position < 0:
            self.position = 0
        elif self.position >= len(self.items):
            self.position = len(self.items)-1

    def get_target(self):
        #TODO make rm the .json or .csv and just name of what the menu is
        return str(self.target)

    def display(self):
        self.panel.top()
        self.panel.show()
        self.window.clear()
        self.window.addstr("The target is "+self.get_target())
        global current_title

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.position:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = '%d. %s' % (index+1, item[0])
                self.window.addstr(1+index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord('\n')]:
                if self.position == len(self.items)-1:#if its the exit button
                    break
                else:
                    #TODO make it call a thing instead

                    #TODO 1st make it print what the cmd is
                    self.target = self.items[self.position]
                    print(self.target)
                    current_title = self.items[self.position][0]
                    self.items[self.position][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)

            elif key == curses.KEY_DOWN:
                self.navigate(1)

            else:
                print("key was",key)
                #print(self.letters_to_listen_to)
                #print(self.items)
                for n in self.numbers_to_listen_to:
                    if key == ord(str(n)):
                        #print("dIng")
                        #print(self.position)
                        #run item at n
                        current_title = self.items[n-1][0]
                        self.items[n-1][1]()

                for l in self.letters_to_listen_to:
                    if key == ord(str(l)):
                        # print("dIng")
                        # print(self.position)
                        # run item at n
                        current_title = self.items[self.letters_to_listen_to.index(l)][0]
                        self.items[self.letters_to_listen_to.index(l)][1]()

                #if key in [for n in self.numbers_to_listen_to:ord(n)]

        self.window.clear()
        self.panel.hide()
        panel.update_panels()
        curses.doupdate()

class csv_shit(object):
    def write_test(self):
        with open('eggs.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
            spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    def read(self,file_to_read):
        titles = []
        cmds = []
        stay_in_menu = []

        with open(file_to_read, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            print("contents of one.csv")
            for row in reader:
                titles.append(row[0])
                cmds.append(row[1])
                stay_in_menu.append([2])
                title_to_cmd[row[0]] = row[1]
                print(''.join(row))

        return titles,cmds,stay_in_menu

    def make_menu(self,titles,cmds):
        runner = sys_runner()
        menu_items = []
        #TODO make menu objects callable things
        for title,cmd in zip(titles,cmds):
            temp_tuple = (str(title),runner.run)
            menu_items.append(temp_tuple)
        return menu_items


class sys_runner(object):
    def run(self,stay_in_menu=0):
        #TODO if stay in menu then print output in display fucntion
        # if not then exit menu and run
        print("running")
        global current_title,title_to_cmd
        #put title back to normal
        current_title = current_title.replace("[","").replace("]","")
        print(current_title)
        print(title_to_cmd[current_title])
        #TODO make it make temp


    def exit(self):
        exit(0)
        return

class MyApp(object):

    def __init__(self, stdscreen):
        self.screen = stdscreen
        curses.curs_set(0)

        csv_obj = csv_shit()

        titles, cmds, stay_in_menu = csv_obj.read(target)
        menu_items = csv_obj.make_menu(titles, cmds)

        main_menu = Menu(menu_items, self.screen)
        main_menu.display()



if __name__ == '__main__':
    print ("This is the name of the script: ", sys.argv[0])
    if len(sys.argv) >= 2:
        target = sys.argv[1]
    curses.wrapper(MyApp)