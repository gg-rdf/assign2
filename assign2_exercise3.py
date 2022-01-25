import datetime
from datetime import datetime, timedelta
from operator import itemgetter
import statistics as s
from statistics import mean


class GgQueues:
    fullGClist = []
    minorGClist = []
    first_line = 0
    last_line = 0

    def read_file(self):
        with open('wk2_test2_in.log', "r") as logfile:

            for i, line in enumerate(logfile): # for each line in log file
                if i == 0:
                    self.first_line = line # keep first line to calc file time range

                line = line.replace(',','').replace('[','').replace(']','') # remove ,[]
                if "Full" in line: # if full GC queue store it at full GC list
                    linef = line.split(' ') # split on spaces
                    self.fullGClist.append([linef[0],linef[1], linef[2]+' '+linef[3]+' '+linef[4], linef[5]])
                else: # else store it at minor GC list
                    linem = line.split(' ') # slpit on spaces
                    self.minorGClist.append([linem[0],linem[1], linem[2]+' '+linem[3], linem[4]])

            self.last_line = line # keep last line to calc file time range

    def count_minor_gc(self): # print num of minor gc
            print("The num of Minor GCs queues are %d\n"%len(self.minorGClist))

    def count_full_gc(self): # print num of full gc
            print("The num of Full GCs queues are %d\n"%len(self.fullGClist))

    def calc_file_time_range(self): # calculate file time range
        d1 = datetime.strptime(self.first_line.split(' ')[0][:-1], '%Y-%m-%dT%H:%M:%S.%f+0000') # convert timestamps to datetime format
        d2 = datetime.strptime( self.last_line.split(' ')[0][:-1], '%Y-%m-%dT%H:%M:%S.%f+0000')
        print("The time range of the file is %s\n"%(d2 - d1)) # subtract them

    def print_lists(self):
        print(self.minorGClist[0:3])
        #print(self.fullGClist)

    # sort both lists
    def cacl_top3_minor_gc(self): # calc top 3 minor gc
        self.calc_top3(self.minorGClist,'Minor')

    def cacl_top3_full_gc(self): # cacl top 3 full gc
        self.calc_top3(self.fullGClist,'Full')

    def calc_top3(self,list,str): # calc top 3 of list
        list = sorted(list, key=lambda x: x[3], reverse=True) # sort list
        print("Top 3 %s GCs are:" % str)
        top3 = list[0:3] # keep 3 first queues in list
        for l in top3:
            '''
            timestamp = datetime.strptime(l[0][:-1], '%Y-%m-%dT%H:%M:%S.%f+0000') # remove ':' from timestamp and convert it to datetime
            secs = float(l[3]) # convert the time that queue spend to float
            time_occurred = timestamp - timedelta(seconds=secs) # subtract time spend from timestamp
            # print(l[2], "Time spend:", l[3], "Timestamp: ", l[0][:-1], "Time occurred:", time_occurred)
            '''
            print("%s, Time spend: %s, Timestamp: %s" % (l[2], l[3], l[0][:-1]))
        print()

    def calc_avg_minor_gc(self): # calc average time that a minor gc spends
        avg = self.calc_avg(self.minorGClist)
        print("The average time a minor GC queue spends is %f seconds\n" % avg)

    def calc_avg_full_gc(self):
        avg = self.calc_avg(self.fullGClist) # calc average time that a full gc spends
        print("The average time a full GC queue spends is %f seconds\n" % avg)

    # calculate avg time of list
    def calc_avg(self, list):
        sum = 0
        for i in range(0, len(list)):
            try:
               list[i][3] = float(list[i][3]) # convert time spend string to actual float
            except ValueError: # if is not a number
                return ('No number found.')

            sum += list[i][3] # sum all times
        avg = sum / len(list) # divide them with the length of the list
        return avg


queues = GgQueues()
queues.read_file()
queues.calc_file_time_range()
queues.count_minor_gc()
queues.count_full_gc()
queues.cacl_top3_minor_gc()
queues.cacl_top3_full_gc()
queues.calc_avg_minor_gc()
queues.calc_avg_full_gc()
