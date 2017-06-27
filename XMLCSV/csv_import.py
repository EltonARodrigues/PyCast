import csv
import os.path


class CSVfeed(object):
    def file_csv(self):
        podcsv = os.path.isfile('Podcasts.csv')
        if not podcsv:
            f = open('Podcasts.csv', 'w')
            f.close()

    def new_feed(self, name, feed):

        id_p = 0
        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                id_p = int(row[0])
            id_p += 1
        with open('Podcasts.csv', 'a') as file_handler:
            csv_writer = csv.writer(file_handler)
            csv_writer.writerow([id_p, name, feed])

    def select(self):
        cont = -1

        print("\tID\tPodCast\t")
        print("-" * 39)
        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                print('|\t{}\t{}\t'.format(row[0], row[1]))
                cont += 1
        return cont

    def verify(self, feed):
        check_url = False

        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                if row[2] == feed:
                    check_url = True

        return check_url

    def get_url(self, id_p):
        with open('Podcasts.csv') as csvfile:
            users_reader = csv.reader(csvfile)
            for row in users_reader:
                if(row[0] == id_p):
                    return row[2]

    def remove(self, id_remove):
        teste = list()
        with open('Podcasts.csv', 'r') as csvfile:
            users_reader = csv.reader(csvfile)
            for row in users_reader:
                if row[0] != id_remove:
                    teste.append(row)

        with open('Podcasts.csv', 'w') as file_handler:
            csv_writer = csv.writer(file_handler)
            for row in teste:
                csv_writer.writerow(row)
    
    def removeAll(self, id_remove):
        os.remove('./Podcasts.csv')