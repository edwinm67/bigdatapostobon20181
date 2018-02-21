
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        userid, movieid, genero, rating, date = line.decode('utf-8','ignore').split(',')
        yield date, 1

    def reducer(self, date, values):
        yield 1, (sum(values), date)

    def reducer2(self, any, values):
        l = list(values)
        minimo = min(l)
        maximo = max(l)
        yield 1, (minimo, maximo)

    def steps(self):
    		return [
    			MRStep(mapper = self.mapper, reducer = self.reducer),
    			MRStep(reducer = self.reducer2)
    		]

if __name__ == '__main__':
    MRWordFrequencyCount.run()
