
from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        se, idemp, salario, year = line.decode('utf-8','ignore').split()
        yield se, int(salario)

    def reducer(self, se, values):
        l = list(values)
        avg = sum(l) / len(l)
        yield se, avg

if __name__ == '__main__':
    MRWordFrequencyCount.run()
