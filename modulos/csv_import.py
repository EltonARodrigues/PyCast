import csv

class CSVfeed:
    def file_csv(self):
        import os.path
        file = os.path.isfile('Podcasts.csv')
        if not file:
            with open('Podcasts.csv', 'a') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(['0','0','0'])

    def new_feed(id_p,name,feed):

        id_p = 0
        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                print(row)
                id_p = int(row[0])
            if id_p != 0:
                id_p += 1
        with open('Podcasts.csv', 'a') as file_handler:
            csv_writer = csv.writer(file_handler)
            csv_writer.writerow([id_p,name,feed])

    def select(self):
        cont = 0

        print("\tID\tPodCast\t")
        print("-" * 39)
        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                print('|\t{}\t{}\t{}\t'.format(row[0], row[1]))
                cont = cont + 1

        return cont

    def verify(self, feed):
        check_url = 1

        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                if row[2] == feed:
                    check_url = 0

        return check_url

    def get_url(self,id_p):
        i = 0
        with open('Podcasts.csv') as csvfile:
            users_reader = csv.reader(csvfile)
            for row in users_reader:
                if(row[0] == id_p):
                    return row[2]
