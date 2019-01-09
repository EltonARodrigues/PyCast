#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import os.path
import csv


class Feed:

    def search_file(self):
        podcsv = os.path.isfile('Podcasts.csv')
        if not podcsv:
            f = open('Podcasts.csv', 'w')
            f.close()

    def new(self, name, feed, url):
        if self.verify(url):
            podcast_id = 0
            with open('Podcasts.csv') as csvfile:
                cast_reader = csv.reader(csvfile)
                for row in cast_reader:
                    podcast_id = int(row[0])
                podcast_id += 1

            with open('Podcasts.csv', 'a') as file_handler:
                csv_writer = csv.writer(file_handler)
                csv_writer.writerow([podcast_id, name, feed])
            return True
        return False

    def number_of_podcasts(self):
        cont = -1

        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                print('|\t{}\t{}\t'.format(row[0], row[1]))
                cont += 1
        return cont

    def verify(self, feed):
        with open('Podcasts.csv') as csvfile:
            cast_reader = csv.reader(csvfile)
            for row in cast_reader:
                if row[2] == feed:
                    return False
        return True

    def url(self, podcast_id):
        with open('Podcasts.csv') as csvfile:
            users_reader = csv.reader(csvfile)
            for row in users_reader:
                if(row[0] == podcast_id):
                    return row[2]
        return False

    def remove(self, id_remove):
        podcast_list = list()
        with open('Podcasts.csv', 'r') as csvfile:
            users_reader = csv.reader(csvfile)
            for row in users_reader:
                if row[0] != id_remove:
                    podcast_list.append(row)

        with open('Podcasts.csv', 'w') as file_handler:
            csv_writer = csv.writer(file_handler)
            for row in podcast_list:
                csv_writer.writerow(row)

    def remove_all(self):
        os.remove('./Podcasts.csv')
        self.search_file()
