import csv
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
                print(''.join(row))

        return titles,cmds,stay_in_menu

    def make_menu(self,titles,cmds):
        menu_items = []
        for title,cmd in zip(titles,cmds):
            temp_tuple = (str(title),str(cmd))
            menu_items.append(temp_tuple)
        return menu_items


csv_obj = csv_shit()

titles,cmds,stay_in_menu = csv_obj.read("one.csv")
menu_items = csv_obj.make_menu(titles,cmds)
print(menu_items)
